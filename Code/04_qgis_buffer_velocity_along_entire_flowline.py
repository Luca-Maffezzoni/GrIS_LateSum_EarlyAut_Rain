# IMPORT LIBRARIES
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer, QgsProcessingFeatureSourceDefinition
from osgeo import gdal
import numpy as np
import numpy.ma as MA
import math
import os
from qgis import processing

# =========================
# DEFINE ROOT AND PROJECT FOLDERS
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))  # Root folder where this script is saved

shape_data_folder = os.path.join(ROOT, "..", "Data", "INPUT", "GIS_SITE_A", "SITE_A_flow_lines_shape")#change to "GIS_SITE_B/SITE_B_flow_lines_shape" if you want result from site B
raster_data_folder = os.path.join(ROOT, "..", "Data", "INPUT", "GIS_SITE_A", "RASTER_ICE_VELOCITY_SELECTED_SITE_A")#change to "GIS_SITE_B/RASTER_ICE_VELOCITY_SELECTED_SITE_B" if you want result from site B
output_folder = os.path.join(ROOT, "..", "Data", "PROCESSED", "VELOCITY_ALONG_FLOWLINES_SITE_A")#change to "VELOCITY_ALONG_FLOWLINES_SITE_B" if you want to put the results in site B folder

# =========================
# LOAD RASTER AND VECTOR LAYERS
# =========================
raster_path = os.path.join(raster_data_folder, "22Aug13_02Sep13_alligned.tif")#change the image pairs with 02Sep13_13Sep13_alligned.tif or 13Sep13_24Sep13_alligned.tif 
#to obtain output of the other periods investigated. If you are investigating site B the three image pairs analysed to put here are 08Aug15_19Aug15_alligned.tif, 
#19Aug15_30Aug15_alligned.tif and 30Aug15_09Sep15_alligned.tif
flow_line_path = os.path.join(shape_data_folder, "flow_line_1.shp") #there are 5 flowlines for site A and 4 flowlines at site B. Change them manually.

layer = QgsRasterLayer(raster_path, "22Aug13_02Sep13_alligned")
if not layer.isValid():
    raise ValueError("DEM layer failed to load")
QgsProject.instance().addMapLayer(layer)

layer2 = QgsVectorLayer(flow_line_path, "flow_line_1", "ogr")
if not layer2.isValid():
    raise ValueError("Flow line layer failed to load")
QgsProject.instance().addMapLayer(layer2)

# =========================
# GENERATE PROFILES ALONG FLOW LINES USING SAGA
# =========================
profile_shp = os.path.join(output_folder, "Profile.shp")
profiles_shp = os.path.join(output_folder, "Profiles.shp")

parameters = {
    'DEM': layer.id(),
    'LINES': layer2.id(),
    'NAME': 'id',
    'SPLIT': True,
    'PROFILE': profile_shp,
    'PROFILES': profiles_shp
}

processing.runAndLoadResults("saga:profilesfromlines", parameters)

# =========================
# LOAD GENERATED PROFILE LAYER
# =========================
layer3 = QgsVectorLayer(profile_shp, "Profile", "ogr")
if not layer3.isValid():
    raise ValueError("Profile layer failed to load")
QgsProject.instance().addMapLayer(layer3)

# =========================
# CREATE BUFFER AROUND PROFILE LINES
# =========================
buffered_shp = os.path.join(output_folder, "Buffered.shp")
buffer_params = {
    'INPUT': layer3.id(),
    'DISTANCE': 500,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2.0,
    'DISSOLVE': False,
    'OUTPUT': buffered_shp
}

processing.runAndLoadResults("native:buffer", buffer_params)

# =========================
# LOAD BUFFERED LAYER
# =========================
layer4 = QgsVectorLayer(buffered_shp, "Buffered", "ogr")
if not layer4.isValid():
    raise ValueError("Buffered layer failed to load")
QgsProject.instance().addMapLayer(layer4)

# =========================
# INITIALIZE STATISTICS LISTS
# =========================
stat_mean = []
stat_errors = []

# =========================
# CLIP RASTER USING BUFFER AND CALCULATE STATISTICS
# =========================
raster_template = os.path.join(output_folder, "raster{}.tif")

for i, feat in enumerate(layer4.getFeatures(), start=1):
    # Select the current buffer feature
    layer4.selectByExpression(f'"ID" = {i}"')

    # Clip raster to the current buffer
    clip_params = {
        'INPUT': layer.id(),
        'MASK': QgsProcessingFeatureSourceDefinition(layer4.id(), True),
        'SOURCE_CRS': 'EPSG:3413',
        'TARGET_CRS': 'EPSG:3413',
        'CROP_TO_CUTLINE': False,
        'DATA_TYPE': 0,
        'OUTPUT': raster_template.format(i)
    }

    processing.run("gdal:cliprasterbymasklayer", clip_params)
    layer4.removeSelection()

    # Read clipped raster and calculate statistics
    ds = gdal.Open(raster_template.format(i))
    band1 = ds.GetRasterBand(1).ReadAsArray()
    ma_data = MA.masked_where(band1 < 0.0, band1)  # mask invalid values
    ma_data_masked = MA.filled(ma_data, np.nan)

    mean_val = np.nanmean(ma_data_masked)
    stat_mean.append(mean_val)

    # Quadratic error (safe from division by zero)
    count = np.count_nonzero(~np.isnan(ma_data_masked))
    quad_error = math.sqrt(np.nansum(ma_data_masked**2)) / count if count > 0 else np.nan
    stat_errors.append(quad_error)

# =========================
# EXTRACT DISTANCES AND EXPORT TO TXT
# =========================
distances = [feat["DIST"] for feat in layer4.getFeatures()]
txt_output = os.path.join(output_folder, "flow_1_22Aug13_02Sep13.txt")  
# Update the number after "flow_" according to the flowline number used above.
# Also, update the date range (e.g., "22Aug13_02Sep13") to match the period of the raster specified on line 22.

with open(txt_output, 'w') as f:
    # Write headers
    f.write("Distance;Velocity\n")
    
    # Write values for each row
    for z in range(len(stat_mean)):
        f.write(f"{distances[z]:.2f};{stat_mean[z]:.2f}\n")