# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:34:38 2021

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
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "two_basins_RU_above_200_mm.nc"
)

# Output
output_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "TABLE_1_RUNOFF_CALCULATION", "SITE_A",
    "runoff_pre_pre_event.txt"
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
    for i in range(2013,2014):
        summer_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION",
            f"SUMMER_MAR_3_{i}",
            f"sum_{q}_MARv3.9.2_NCEP1-20km_{i}.nc"
        )
        fileobj1=Dataset(summer_file)
        z1=fileobj1.variables[q][60:82,:,:]
        data1=N.reshape(z1,(22,135,73))
        data_sum1=N.sum(data1, axis=0)
        
        ma_data_2 = MA.masked_where(((mask < 219) | (mask > 220)),data_sum1)
        setattr(ma_data_2, "fill_value",float ("NaN"))
        data_masked_melt_2=MA.filled(ma_data_2)
        
        ma_data_3 = MA.masked_where(N.isnan(mask2), data_masked_melt_2)
        setattr(ma_data_3, "fill_value",float ("NaN"))
        ma_data_masked_melt_3=MA.filled(ma_data_3)

        mean_value2= N.nanmean(ma_data_masked_melt_3)
        a=N.append(a,mean_value2)
        fileobj1.close()
        
        
N.savetxt(output_file, a, fmt="%3.3f")