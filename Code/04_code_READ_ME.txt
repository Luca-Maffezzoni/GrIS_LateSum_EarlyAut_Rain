-----------------------------------------------------Velocity Along Flowlines Script--------------------------------------

Overview This Python script, designed to run in QGIS with PyQGIS and GDAL, calculates ice velocity along flowlines. It performs the following steps:

1)Loads raster and flowline shapefiles.

2)Generates profiles along flowlines using SAGA GIS.

3)Creates buffers around the profiles.

4)Clips raster data using the buffers and calculates statistics (mean velocity and quadratic error).

5)Exports distances and mean velocities to a .txt file.

==========================================================MANUAL INPUTS==============================================
Raster Files

	The raster to be processed must be selected manually in the script.

	Example in the script:

raster_path = os.path.join(raster_data_folder, "22Aug13_02Sep13_alligned.tif")

	To process another period or site, replace this path with the desired raster file.

	For Site A, possible raster pairs include:

		22Aug13_02Sep13_alligned.tif

		02Sep13_13Sep13_alligned.tif

		13Sep13_24Sep13_alligned.tif

	For Site B, possible raster pairs include:

		08Aug15_19Aug15_alligned.tif

		19Aug15_30Aug15_alligned.tif

		30Aug15_09Sep15_alligned.tif

Flowline Shapefiles

	The flowline shapefile is also selected manually in the script:

flow_line_path = os.path.join(shape_data_folder, "flow_line_1.shp")

	Site A has 5 flowlines, Site B has 4. Update the filename according to the flowline to process.

==========================================================TXT OUPUTS==============================================

The output file for distances and mean velocities is defined manually:

txt_output = os.path.join(output_folder, "flow_1_22Aug13_02Sep13.txt")

	Important: Update the number after "flow_" to match the flowline number being processed.

	Update the date range (e.g., "22Aug13_02Sep13") to match the raster period.

	Note: Although .txt files for all flowlines are already present in the output folder, the script does not automatically select the correct one. You must specify it manually.

==============================================================NOTES===============================================

All file selections (raster and flowline) must be done manually in the script.

The script is designed for QGIS with PyQGIS, GDAL, NumPy, and SAGA installed.