# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:55:42 2021

@author: Luca
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

# Output → Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_B
output_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "meltwater_may_2015.txt"
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
# MAIN LOOP
# =========================
for year in range(2015, 2016):
    a = N.array([])
    for j in range(61, 92):  # giorni di maggio-giugno
        spring_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SPRING_MAR_4_2015",
            f"spring_ME_MARv3.9.2_NCEP1-20km_{year}.nc"
        )

        fileobj1 = Dataset(spring_file)
        data_melt = fileobj1.variables["ME"][j, :, :]

        # Prima maschera: bacini 15–18
        ma_data_1 = MA.masked_where(((mask < 15) | (mask > 18)), data_melt)
        setattr(ma_data_1, "fill_value", float("NaN"))
        data_masked_melt = MA.filled(ma_data_1)

        # Seconda maschera: escludi bacino 17
        ma_data_2 = MA.masked_where(mask == 17, data_masked_melt)
        setattr(ma_data_2, "fill_value", float("NaN"))
        data_masked_melt_2 = MA.filled(ma_data_2)

        # Terza maschera: applica mask2
        ma_data_3 = MA.masked_where(N.isnan(mask2), data_masked_melt_2)
        setattr(ma_data_3, "fill_value", float("NaN"))
        data_masked_melt_3 = MA.filled(ma_data_3)

        # Media finale
        mean_value = N.nanmean(data_masked_melt_3)
        a = N.append(a, mean_value)

        fileobj1.close()

# =========================
# SAVE OUTPUT
# =========================
N.savetxt(output_file, a, fmt="%3.3f")