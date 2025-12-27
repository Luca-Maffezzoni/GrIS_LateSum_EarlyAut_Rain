# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:09:43 2021

@author: lucam
"""

import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# =========================
# ROOT
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# INPUT FILES
# =========================

# Mask of catchment basins → Data/RAW
mask_file = os.path.join(
    ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc"
)

# Second mask (three basins RU above 200 mm) → Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_B
mask2_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "three_basins_RU_above_200_mm.nc"
)

# Output
output_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "TABLE_1_RUNOFF_CALCULATION", "SITE_B",
    "runoff_week_before_event.txt"
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


a=N.array([])

for q in ["RU"]:
    for h in range(2015,2016):
        file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION",
            f"SUMMER_MAR_3_{h}",
            f"sum_{q}_MARv3.9.2_NCEP1-20km_{h}.nc"
        )
        fileobj1 = Dataset(file)
        z1=fileobj1.variables[q][81:88,:,:]
        data1=N.reshape(z1,(7,135,73))
        data_sum1=N.sum(data1, axis=0)
        
        ma_data_1 = MA.masked_where(((mask < 15) | (mask > 18)),data_sum1)
        setattr(ma_data_1, "fill_value",float ("NaN"))
        data_masked_melt=MA.filled(ma_data_1)
        
        ma_data_2 = MA.masked_where(mask == 17,data_masked_melt)
        setattr(ma_data_2, "fill_value",float ("NaN"))
        data_masked_melt_2=MA.filled(ma_data_2)
        
        ma_data_3 = MA.masked_where(N.isnan(mask2), data_masked_melt_2)
        setattr(ma_data_3, "fill_value",float ("NaN"))
        ma_data_masked_melt_3=MA.filled(ma_data_3)
        
        fileobj1.close()
        
mean_value2= N.nanmean(ma_data_masked_melt_3)
a=N.append(a,mean_value2)

N.savetxt(output_file, a, fmt="%3.3f")