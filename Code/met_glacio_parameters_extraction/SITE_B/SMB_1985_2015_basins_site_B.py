# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:47:19 2020

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

# Variable of interest
q = "SMB"

# Input mask file (catchments) – same root folder as before
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")

# Input SMB file
smb_input_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SMB_1985_2015.nc")

# Output file: masked SMB for Site B
smb_output_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_B", "SMB_1985_2015_basins_site_B.nc")

# =========================
# OPEN MASK FILE
# =========================
fileobj1 = Dataset(mask_file)
mask = fileobj1.variables["CHATCMENTS"][:, :]
fileobj1.close()

# =========================
# OPEN SMB INPUT FILE
# =========================
fileobj = Dataset(smb_input_file)
Y21 = fileobj.variables["Y21_155"][:]
X12 = fileobj.variables["X12_84"][:]
latitude = fileobj.variables["LAT"][:, :]
longitude = fileobj.variables["LON"][:, :]

# Retrieve metadata (units, long_name)
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[q].units
long_name = fileobj.variables[q].long_name

# Extract SMB variable
data = fileobj.variables[q][:, :]

# =========================
# MASK DATA: select only basins 15–18
# =========================
ma_data = MA.masked_where((mask < 15) | (mask > 18), data)
setattr(ma_data, "fill_value", float("NaN"))
ma_data_masked = MA.filled(ma_data)

# Further mask basin 17 specifically
ma_data2 = MA.masked_where(mask == 17, ma_data_masked)
setattr(ma_data2, "fill_value", float("NaN"))
ma_data_masked_2 = MA.filled(ma_data2)

# =========================
# CREATE OUTPUT FILE
# =========================
file_out = Dataset(smb_output_file, "w", format="NETCDF4_CLASSIC")

# Define dimensions
lon_dim = file_out.createDimension("X12_84", len(X12))
lat_dim = file_out.createDimension("Y21_155", len(Y21))

# Create variables
lons = file_out.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_out.createVariable("Y21_155", N.int32, ("Y21_155",))
smb_var = file_out.createVariable(q, N.float32, ("Y21_155", "X12_84"))
lons2 = file_out.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_out.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# Assign units and metadata
lons.units = X12_units
lats.units = Y21_units
smb_var.units = z_units
lons2.units = lon_units
lats2.units = lat_units
smb_var.long_name = long_name

# Write data
lons[:] = X12[:]
lats[:] = Y21[:]
smb_var[:, :] = ma_data_masked_2[:, :]
lons2[:, :] = longitude[:, :]
lats2[:, :] = latitude[:, :]

# Close file
file_out.close()