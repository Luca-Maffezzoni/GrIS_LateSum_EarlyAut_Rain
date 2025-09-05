# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:36:58 2020

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
# EXTRACT THE SECOND MASK (ELA / SMB)
# =========================
mask2_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "SMB_1985_2015_basins_site_A.nc"
)
with Dataset(mask2_file) as fileobj2:
    mask2 = fileobj2.variables["SMB"][:, :]

# =========================
# DEFINE INPUT FILES
# =========================
summer_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SUMMER_MAR_3_2013",
    "sum_AL1_MARv3.9.2_NCEP1-20km_2013.nc"
)

autumn_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2013",
    "autumn_AL1_MARv3.9.2_NCEP1-20km_2013.nc"
)

# =========================
# DEFINE OUTPUT FILE
# =========================
output = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "SEB_PARAMETERS", "SITE_A",
    "aug_sept_2013_daily_AL1.txt"
)

a = N.array([])

# =========================
# SUMMER LOOP
# =========================
for i in range(84, 92):
    with Dataset(summer_file) as fileobj2:
        data = fileobj2.variables["AL1"][i, :, :]
        ma_data = MA.masked_where(((mask < 219) | (mask > 220)), data)
        setattr(ma_data, "fill_value", float("NaN"))
        ma_data_masked = MA.filled(ma_data)
        ma_data_2 = MA.masked_where(mask2 > 0, ma_data_masked)
        setattr(ma_data_2, "fill_value", float("NaN"))
        ma_data_masked_2 = MA.filled(ma_data_2)

        mean_value = N.nanmean(ma_data_masked_2)
        a = N.append(a, mean_value)

# =========================
# AUTUMN LOOP
# =========================
for j in range(0, 23):
    with Dataset(autumn_file) as fileobj3:
        data = fileobj3.variables["AL1"][j, :, :]
        ma_data_2 = MA.masked_where(((mask < 219) | (mask > 220)), data)
        setattr(ma_data_2, "fill_value", float("NaN"))
        ma_data_masked_2 = MA.filled(ma_data_2)
        ma_data_3 = MA.masked_where(mask2 > 0, ma_data_masked_2)
        setattr(ma_data_3, "fill_value", float("NaN"))
        ma_data_masked_3 = MA.filled(ma_data_3)

        mean_value = N.nanmean(ma_data_masked_3)
        a = N.append(a, mean_value)

# =========================
# SAVE OUTPUT
# =========================
N.savetxt(output, a, fmt="%3.3f")