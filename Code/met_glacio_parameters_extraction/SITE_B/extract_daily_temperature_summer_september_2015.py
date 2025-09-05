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
# DEFINE OUTPUT FILES
# =========================
output_summer = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "temperature_summer_2015.txt"
)

output_autumn = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B",
    "temperature_autumn_2015.txt"
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
            f"sum_TTZ_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(summer_file) as fileobj1:
            data_temperature = fileobj1.variables["TTZ"][j, :, :]

        # Apply masks: basins 15–18, exclude basin 17, and mask2
        ma_data_1 = MA.masked_where((mask < 15) | (mask > 18), data_temperature)
        ma_data_2 = MA.masked_where(mask == 17, ma_data_1)
        ma_data_3 = MA.masked_where(mask2 > 0, ma_data_2)

        mean_value = N.nanmean(ma_data_3)
        summer_values = N.append(summer_values, mean_value)

    # Save summer temperature output
    N.savetxt(output_summer, summer_values, fmt="%3.3f")

# =========================
# MAIN LOOP: AUTUMN
# =========================
for year in range(2015, 2016):
    autumn_values = N.array([])

    for i in range(0, 30):  # autumn days
        autumn_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2015",
            f"autumn_TTZ_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(autumn_file) as fileobj2:
            data_temperature = fileobj2.variables["TTZ"][i, :, :]

        # Apply masks: basins 15–18, exclude basin 17, and mask2
        ma_data_1 = MA.masked_where((mask < 15) | (mask > 18), data_temperature)
        ma_data_2 = MA.masked_where(mask == 17, ma_data_1)
        ma_data_3 = MA.masked_where(mask2 > 0, ma_data_2)

        mean_value = N.nanmean(ma_data_3)
        autumn_values = N.append(autumn_values, mean_value)

    # Save autumn temperature output
    N.savetxt(output_autumn, autumn_values, fmt="%3.3f")