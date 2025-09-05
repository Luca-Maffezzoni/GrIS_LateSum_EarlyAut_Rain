"""
Created on [DATE]

@author: lucam
"""

import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY (relative to repo structure)
# =========================
ROOT = os.path.dirname(__file__)  

# Input mask file (basins) – same as in the first code
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")

# Input NetCDF with cumulative RU (Runoff)
ru_input_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "sum_RU_1985_2015.nc")

# Output file: masked RU for the two basins, only values above 200 mm
ru_output_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", "two_basins_RU_above_200_mm.nc")

# =========================
# OPEN MASK FILE (catchments)
# =========================
fileobj1 = Dataset(mask_file)
mask = fileobj1.variables["CHATCMENTS"][:, :]
fileobj1.close()

# =========================
# OPEN RU INPUT FILE
# =========================
fileobj = Dataset(ru_input_file)
Y21 = fileobj.variables["Y21_155"][:]
X12 = fileobj.variables["X12_84"][:]
latitude = fileobj.variables["LAT"][:, :]
longitude = fileobj.variables["LON"][:, :]

# Retrieve metadata (units, long_name)
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables["RU"].units
ru_long_name = fileobj.variables["RU"].long_name

# Extract RU variable (cumulative runoff)
data = fileobj.variables["RU"][:, :]

# =========================
# MASK DATA: select only basins 219–220
# =========================
ma_data = MA.masked_where((mask < 219) | (mask > 220), data)
setattr(ma_data, "fill_value", float("NaN"))
data_masked_1 = MA.filled(ma_data)

# =========================
# MASK DATA: select only values above 200 mm
# =========================
ma_data2 = MA.masked_where(data_masked_1 < 200, data_masked_1)
setattr(ma_data2, "fill_value", float("NaN"))
data_masked_2 = MA.filled(ma_data2)

# =========================
# CREATE OUTPUT FILE
# =========================
file_out = Dataset(ru_output_file, "w", format="NETCDF4_CLASSIC")

# Define dimensions
lon_dim = file_out.createDimension("X12_84", len(X12))
lat_dim = file_out.createDimension("Y21_155", len(Y21))

# Create variables
lons = file_out.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_out.createVariable("Y21_155", N.int32, ("Y21_155",))
ru_var = file_out.createVariable("RU", N.float32, ("Y21_155", "X12_84"))
lons2 = file_out.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_out.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# Assign units and metadata
lons.units = X12_units
lats.units = Y21_units
ru_var.units = z_units
lons2.units = lon_units
lats2.units = lat_units
ru_var.long_name = ru_long_name

# Write data
lons[:] = X12[:]
lats[:] = Y21[:]
ru_var[:, :] = data_masked_2[:, :]
lons2[:, :] = longitude[:, :]
lats2[:, :] = latitude[:, :]

# Close file
file_out.close()