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
# DEFINE OUTPUT FILES
# =========================
output_summer = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "temperature_summer_2013.txt"
)

output_autumn = os.path.join(
    ROOT, "..", "..", "..",
    "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A",
    "temperature_autumn_2013.txt"
)

# =========================
# MAIN LOOP: SUMMER
# =========================
for year in range(2013, 2014):
    summer_values = N.array([])

    for j in range(0, 92):  # summer days
        summer_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "SUMMER_MAR_3_2013",
            f"sum_TTZ_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(summer_file) as fileobj1:
            data_temperature = fileobj1.variables["TTZ"][j, :, :]

        # Apply masks: basins 219–220 and mask2
        ma_data = MA.masked_where((mask < 219) | (mask > 220), data_temperature)
        ma_data = MA.masked_where(mask2 > 0, ma_data)

        mean_value = N.nanmean(ma_data)
        summer_values = N.append(summer_values, mean_value)

    # Save summer temperature output
    N.savetxt(output_summer, summer_values, fmt="%3.3f")

# =========================
# MAIN LOOP: AUTUMN
# =========================
for year in range(2013, 2014):
    autumn_values = N.array([])

    for i in range(0, 30):  # autumn days
        autumn_file = os.path.join(
            ROOT, "..", "..", "..",
            "Data", "RAW", "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION", "AUTUMN_MAR_4_2013",
            f"autumn_TTZ_MARv3.9.2_NCEP1-20km_{year}.nc"
        )
        with Dataset(autumn_file) as fileobj2:
            data_temperature = fileobj2.variables["TTZ"][i, :, :]

        # Apply masks: basins 219–220 and mask2
        ma_data = MA.masked_where((mask < 219) | (mask > 220), data_temperature)
        ma_data = MA.masked_where(mask2 > 0, ma_data)

        mean_value = N.nanmean(ma_data)
        autumn_values = N.append(autumn_values, mean_value)

    # Save autumn temperature output
    N.savetxt(output_autumn, autumn_values, fmt="%3.3f")