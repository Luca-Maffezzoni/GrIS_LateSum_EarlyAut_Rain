# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:25:40 2020

@author: lucam
"""

"""
Created on [DATE]

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
mask2_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "two_basins_RU_above_200_mm.nc"
)

# Output → Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_A
output_summer = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "rainfall_summer_2013.txt"
)

output_autumn = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "rainfall_autumn_2013.txt"
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
# SUMMER (June–August)
# =========================
summer_values = N.array([])
for j in range(0, 92):  # 92 giorni
    summer_file = os.path.join(
        ROOT, "..", "..", "..",
        "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SUMMER_MAR_3_2013",
        "sum_RF_MARv3.9.2_NCEP1-20km_2013.nc"
    )

    fileobj1 = Dataset(summer_file)
    data_rainfall = fileobj1.variables["RF"][j, :, :]

    ma_data_rainfall = MA.masked_where(((mask < 219) | (mask > 220)), data_rainfall)
    setattr(ma_data_rainfall, "fill_value", float("NaN"))
    ma_data_masked_rainfall = MA.filled(ma_data_rainfall)

    ma_data_2_rainfall = MA.masked_where(N.isnan(mask2), ma_data_masked_rainfall)
    setattr(ma_data_2_rainfall, "fill_value", float("NaN"))
    ma_data_masked_2_rainfall = MA.filled(ma_data_2_rainfall)

    mean_value = N.nanmean(ma_data_masked_2_rainfall)
    summer_values = N.append(summer_values, mean_value)
    fileobj1.close()

# =========================
# AUTUMN (September)
# =========================
autumn_values = N.array([])
for i in range(0, 30):  # 30 giorni
    autumn_file = os.path.join(
        ROOT, "..", "..", "..",
        "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2013",
        "autumn_RF_MARv3.9.2_NCEP1-20km_2013.nc"
    )

    fileobj2 = Dataset(autumn_file)
    data = fileobj2.variables["RF"][i, :, :]

    ma_data = MA.masked_where(((mask < 219) | (mask > 220)), data)
    setattr(ma_data, "fill_value", float("NaN"))
    ma_data_masked = MA.filled(ma_data)

    ma_data_3 = MA.masked_where(N.isnan(mask2), ma_data_masked)
    setattr(ma_data_3, "fill_value", float("NaN"))
    ma_data_masked_3 = MA.filled(ma_data_3)

    mean_value_2 = N.nanmean(ma_data_masked_3)
    autumn_values = N.append(autumn_values, mean_value_2)
    fileobj2.close()

# =========================
# SAVE OUTPUTS
# =========================
N.savetxt(output_summer, summer_values, fmt="%3.3f")
N.savetxt(output_autumn, autumn_values, fmt="%3.3f")   