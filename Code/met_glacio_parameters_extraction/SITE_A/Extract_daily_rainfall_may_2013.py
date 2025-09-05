# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:10:20 2021

@author: Luca
"""
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
mask2_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", "two_basins_RU_above_200_mm.nc")

# Output text file with rainfall results → same SITE_A folder
output_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", "rainfall_may_2013.txt")

# =========================
# LOAD MASKS
# =========================
fileobj = Dataset(mask_file)
mask = fileobj.variables["CHATCMENTS"][:,:]
fileobj.close()

fileobj2 = Dataset(mask2_file)
mask2 = fileobj2.variables["RU"][:,:]
fileobj2.close()

# =========================
# LOOP OVER YEAR AND DAYS
# =========================
for year in range(2013, 2014):  # Only year 2013
    a = N.array([])
    for j in range(61, 92):  # Days 61 to 91 (May)
        
        # Build path to daily MAR spring rainfall file
        spring_file = os.path.join(
            ROOT, "..", "..", "..", 
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SPRING_MAR_4_2013",
            f"spring_RF_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        
        # Open MAR NetCDF file
        fileobj1 = Dataset(spring_file)
        data_rain = fileobj1.variables["RF"][j, :, :]
        
        # Apply first mask (catchments between 219 and 220)
        ma_data_rain = MA.masked_where(((mask < 219) | (mask > 220)), data_rain)
        setattr(ma_data_rain, "fill_value", float("NaN"))
        ma_data_masked_rain = MA.filled(ma_data_rain)
        
        # Apply second mask (RU > 200mm basins)
        ma_data_2_rain = MA.masked_where(N.isnan(mask2), ma_data_masked_rain)
        setattr(ma_data_2_rain, "fill_value", float("NaN"))
        ma_data_masked_2_rain = MA.filled(ma_data_2_rain)
        
        # Compute daily mean rainfall value
        mean_value = N.nanmean(ma_data_masked_2_rain)
        a = N.append(a, mean_value)
        fileobj1.close()

    # =========================
    # SAVE RESULTS
    # =========================
    N.savetxt(output_file, a, fmt="%3.3f")