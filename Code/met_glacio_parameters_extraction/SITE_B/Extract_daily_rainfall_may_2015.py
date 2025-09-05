# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:10:20 2021

@author: Luca
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
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B", "three_basins_RU_above_200_mm.nc"
)
with Dataset(mask2_file) as fileobj2:
    mask2 = fileobj2.variables["RU"][:, :]

# =========================
# DEFINE OUTPUT FILE
# =========================
output_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "rainfall_may_2015.txt"
)

# =========================
# MAIN LOOP: YEARS AND DAYS
# =========================
for year in range(2015, 2016):  # loop over years (here only 2015)
    a = N.array([])  # array to store daily means
    for j in range(61, 92):  # loop over days of May-June
        # Load daily rainfall data
        spring_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SPRING_MAR_4_2015",
            f"spring_RF_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(spring_file) as fileobj1:
            data_rain = fileobj1.variables["RF"][j, :, :]

        # =========================
        # APPLY FIRST MASK: BASINS 15–18
        # =========================
        ma_data_1 = MA.masked_where((mask < 15) | (mask > 18), data_rain)
        setattr(ma_data_1, "fill_value", float("NaN"))
        data_masked_1 = MA.filled(ma_data_1)

        # =========================
        # APPLY SECOND MASK: EXCLUDE BASIN 17
        # =========================
        ma_data_2 = MA.masked_where(mask == 17, data_masked_1)
        setattr(ma_data_2, "fill_value", float("NaN"))
        data_masked_2 = MA.filled(ma_data_2)

        # =========================
        # APPLY THIRD MASK: USE MASK2
        # =========================
        ma_data_3 = MA.masked_where(N.isnan(mask2), data_masked_2)
        setattr(ma_data_3, "fill_value", float("NaN"))
        data_masked_3 = MA.filled(ma_data_3)

        # =========================
        # COMPUTE DAILY MEAN
        # =========================
        mean_value = N.nanmean(data_masked_3)
        a = N.append(a, mean_value)

# =========================
# SAVE OUTPUT
# =========================
N.savetxt(output_file, a, fmt="%3.3f")