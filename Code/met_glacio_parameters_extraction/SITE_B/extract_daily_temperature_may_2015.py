"""
Created on Tue Mar  9 11:12:12 2021

@author: Luca
"""


#In this, I use the ELA to calculate the temperature below it

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
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "SMB_1985_2015_basins_site_B.nc"
)
with Dataset(mask2_file) as fileobj2:
    mask2 = fileobj2.variables["SMB"][:, :]

# =========================
# DEFINE OUTPUT FILE
# =========================
output_file = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "temperature_may_2015.txt"
)

# =========================
# MAIN LOOP: SPRING TEMPERATURE (TTZ)
# =========================
for year in range(2015, 2016):
    temperature_values = N.array([])  # store daily mean temperatures

    for j in range(61, 92):  # days in May
        spring_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SPRING_MAR_4_2015",
            f"spring_TTZ_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(spring_file) as fileobj1:
            data_temperature = fileobj1.variables["TTZ"][j, :, :]

        # Apply first mask: basins 15–18
        ma_data_1 = MA.masked_where((mask < 15) | (mask > 18), data_temperature)
        setattr(ma_data_1, "fill_value", float("NaN"))
        data_masked_1 = MA.filled(ma_data_1)

        # Apply second mask: exclude basin 17
        ma_data_2 = MA.masked_where(mask == 17, data_masked_1)
        setattr(ma_data_2, "fill_value", float("NaN"))
        data_masked_2 = MA.filled(ma_data_2)

        # Apply third mask: xclude areas above 0 in mask2 (ELA / SMB)
        ma_data_3 = MA.masked_where(mask2 > 0, data_masked_2)
        setattr(ma_data_3, "fill_value", float("NaN"))
        data_masked_3 = MA.filled(ma_data_3)

        # Compute daily mean temperature
        mean_value = N.nanmean(data_masked_3)
        temperature_values = N.append(temperature_values, mean_value)

# =========================
# SAVE OUTPUT
# =========================
N.savetxt(output_file, temperature_values, fmt="%3.3f")