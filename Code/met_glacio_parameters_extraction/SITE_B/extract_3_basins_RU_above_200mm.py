




import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY (relative to repo structure)
# =========================
ROOT = os.path.dirname(__file__)  

# Variable of interest
var_name = "RU"

# Input mask file (catchments)
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")

# Input cumulative runoff file
ru_input_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "sum_RU_1985_2015.nc")

# Output file: masked RU for Site B
ru_output_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B", "three_basins_RU_above_200_mm.nc")

# =========================
# LOAD BASIN MASK
# =========================
fileobj1 = Dataset(mask_file)
mask = fileobj1.variables["CHATCMENTS"][:, :]
fileobj1.close()

# =========================
# LOAD RUNOFF DATA
# =========================
fileobj = Dataset(ru_input_file)
Y21 = fileobj.variables["Y21_155"][:]
X12 = fileobj.variables["X12_84"][:]
latitude = fileobj.variables["LAT"][:, :]
longitude = fileobj.variables["LON"][:, :]

# Metadata
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[var_name].units
long_name = fileobj.variables[var_name].long_name

# Extract runoff data
data = fileobj.variables[var_name][:, :]

# =========================
# APPLY MASKS
# =========================
# Select basins 15–18
ma_data = MA.masked_where((mask < 15) | (mask > 18), data)
setattr(ma_data, "fill_value", float("NaN"))
data_masked_1 = MA.filled(ma_data)

# Exclude basin 17
ma_data_2 = MA.masked_where(mask == 17, data_masked_1)
setattr(ma_data_2, "fill_value", float("NaN"))
data_masked_2 = MA.filled(ma_data_2)

# Mask runoff values below 200 mm
ma_data_3 = MA.masked_where(data_masked_2 < 200, data_masked_2)
setattr(ma_data_3, "fill_value", float("NaN"))
data_masked_3 = MA.filled(ma_data_3)

# =========================
# SAVE RESULTS TO NEW NetCDF
# =========================
file_out = Dataset(ru_output_file, "w", format="NETCDF4_CLASSIC")

# Define dimensions
lon_dim = file_out.createDimension("X12_84", len(X12))
lat_dim = file_out.createDimension("Y21_155", len(Y21))

# Create variables
lons = file_out.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_out.createVariable("Y21_155", N.int32, ("Y21_155",))
ru_var = file_out.createVariable(var_name, N.float32, ("Y21_155", "X12_84"))
lons2 = file_out.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_out.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# Assign units and metadata
lons.units = X12_units
lats.units = Y21_units
ru_var.units = z_units
lons2.units = lon_units
lats2.units = lat_units
ru_var.long_name = long_name

# Write data
lons[:] = X12[:]
lats[:] = Y21[:]
ru_var[:, :] = data_masked_3[:, :]
lons2[:, :] = longitude[:, :]
lats2[:, :] = latitude[:, :]

# Close file
file_out.close()