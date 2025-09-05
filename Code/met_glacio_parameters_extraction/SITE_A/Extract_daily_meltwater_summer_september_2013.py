import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# Define ROOT as the folder where this script is located
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# INPUT FILES
# =========================

# Mask of catchment basins → Data/RAW
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")

# Second mask (RU above 200 mm) → Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_A
mask2_file = os.path.join(
    ROOT, "..", "..", "..", 
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", 
    "two_basins_RU_above_200_mm.nc"
)

# Output files → same SITE_A folder
output_file_summer = os.path.join(
    ROOT, "..", "..", "..", 
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", 
    "meltwater_summer_2013.txt"
)

output_file_autumn = os.path.join(
    ROOT, "..", "..", "..", 
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", 
    "meltwater_autumn_2013.txt"
)

# =========================
# LOAD MASKS
# =========================
fileobj = Dataset(mask_file)
mask = fileobj.variables["CHATCMENTS"][:, :]
fileobj.close()

fileobj2 = Dataset(mask2_file)
mask2 = fileobj2.variables["RU"][:, :]
fileobj2.close()

# =========================
# LOOP FOR SUMMER (June–August)
# =========================
for year in range(2013, 2014):  # Only year 2013
    a_summer = N.array([])
    for j in range(0, 92):  # approx. days June – August 
        
        summer_file = os.path.join(
            ROOT, "..", "..", "..", 
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SUMMER_MAR_3_2013",
            f"sum_ME_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        
        fileobj1 = Dataset(summer_file)
        data_me = fileobj1.variables["ME"][j, :, :]
        
        # Apply first mask (catchments 219–220)
        ma_data_me = MA.masked_where(((mask < 219) | (mask > 220)), data_me)
        setattr(ma_data_me, "fill_value", float("NaN"))
        ma_data_masked_me = MA.filled(ma_data_me)
        
        # Apply second mask (RU > 200mm basins)
        ma_data_2_me = MA.masked_where(N.isnan(mask2), ma_data_masked_me)
        setattr(ma_data_2_me, "fill_value", float("NaN"))
        ma_data_masked_2_me = MA.filled(ma_data_2_me)
        
        mean_value = N.nanmean(ma_data_masked_2_me)
        a_summer = N.append(a_summer, mean_value)
        fileobj1.close()
    
    N.savetxt(output_file_summer, a_summer, fmt="%3.3f")

# =========================
# LOOP FOR AUTUMN (September–November)
# =========================
for year in range(2013, 2014):  # Only year 2013
    a_autumn = N.array([])
    for j in range(0, 30):  # September
        
        autumn_file = os.path.join(
            ROOT, "..", "..", "..", 
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2013",
            f"autumn_ME_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        
        fileobj1 = Dataset(autumn_file)
        data_me = fileobj1.variables["ME"][j, :, :]
        
        # Apply first mask (catchments 219–220)
        ma_data_me = MA.masked_where(((mask < 219) | (mask > 220)), data_me)
        setattr(ma_data_me, "fill_value", float("NaN"))
        ma_data_masked_me = MA.filled(ma_data_me)
        
        # Apply second mask (RU > 200mm basins)
        ma_data_2_me = MA.masked_where(N.isnan(mask2), ma_data_masked_me)
        setattr(ma_data_2_me, "fill_value", float("NaN"))
        ma_data_masked_2_me = MA.filled(ma_data_2_me)
        
        mean_value = N.nanmean(ma_data_masked_2_me)
        a_autumn = N.append(a_autumn, mean_value)
        fileobj1.close()
    
    N.savetxt(output_file_autumn, a_autumn, fmt="%3.3f")