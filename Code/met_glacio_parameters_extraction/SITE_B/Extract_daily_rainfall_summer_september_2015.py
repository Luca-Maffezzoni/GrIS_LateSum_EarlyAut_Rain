# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:25:40 2020

@author: lucam
"""

import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# EXTRACT THE FIRST MASK
# =========================
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")
with Dataset(mask_file) as fileobj:
    mask = fileobj.variables["CHATCMENTS"][:, :]

# =========================
# EXTRACT THE SECOND MASK
# =========================
mask2_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "three_basins_RU_above_200_mm.nc"
)
with Dataset(mask2_file) as fileobj2:
    mask2 = fileobj2.variables["RU"][:, :]

# =========================
# DEFINE OUTPUT FILES
# =========================
summer_output = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "rainfall_summer_2015.txt"
)

autumn_output = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "rainfall_autumn_2015.txt"
)

# =========================
# MAIN LOOP: SUMMER
# =========================
for year in range(2015, 2016):
    summer_values = N.array([])

    for j in range(0, 92):  # summer days
        summer_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SUMMER_MAR_3_2015",
            f"sum_RF_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(summer_file) as fileobj1:
            data_rain = fileobj1.variables["RF"][j, :, :]

        # Apply masks
        data_masked = MA.masked_where((mask < 15) | (mask > 18), data_rain)
        data_masked = MA.masked_where(mask == 17, data_masked)
        data_masked = MA.masked_where(N.isnan(mask2), data_masked)

        # Compute daily mean
        mean_value = N.nanmean(data_masked)
        summer_values = N.append(summer_values, mean_value)

    # Save summer rainfall output
    N.savetxt(summer_output, summer_values, fmt="%3.3f")

# =========================
# MAIN LOOP: AUTUMN
# =========================
for year in range(2015, 2016):
    autumn_values = N.array([])

    for i in range(0, 30):  # autumn days
        autumn_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2015",
            f"autumn_RF_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(autumn_file) as fileobj2:
            data_rain = fileobj2.variables["RF"][i, :, :]

        # Apply masks
        data_masked = MA.masked_where((mask < 15) | (mask > 18), data_rain)
        data_masked = MA.masked_where(mask == 17, data_masked)
        data_masked = MA.masked_where(N.isnan(mask2), data_masked)

        # Compute daily mean
        mean_value = N.nanmean(data_masked)
        autumn_values = N.append(autumn_values, mean_value)

    # Save autumn rainfall output
    N.savetxt(autumn_output, autumn_values, fmt="%3.3f")   