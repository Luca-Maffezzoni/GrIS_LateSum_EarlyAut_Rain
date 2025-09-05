# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:36:49 2020

@author: lucam
"""

import os
import numpy as N
import numpy.ma as MA
from netCDF4 import Dataset

# Define the variable of interest
q = "SMB"

# =========================
# FILE PATHS (relative to repo structure)
# =========================
ROOT = os.path.dirname(__file__)  

# Input mask file (basins)
mask_file = os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "Chatcment_Basins.nc")

# Input NetCDF with cumulative SMB (previously created)
smb_input_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SMB_1985_2015.nc")

# Output file: masked SMB for Site A
smb_output_file = os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "SITE_A", "SMB_1985_2015_basins_site_A.nc")

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
lon_name = fileobj.variables[q].long_name

# Extract SMB variable (already cumulative over 1985–2015)
data = fileobj.variables[q][:, :]

# Apply mask: select basins 219–220, fill other values with NaN
ma_data = MA.masked_where(((mask < 219) | (mask > 220)), data)
setattr(ma_data, "fill_value", float("NaN"))
ma_data_masked = MA.filled(ma_data)

# =========================
# CREATE OUTPUT FILE
# =========================
file_out = Dataset(smb_output_file, "w", format="NETCDF4_CLASSIC")

# Define dimensions
lon = file_out.createDimension("X12_84", len(X12))
lat = file_out.createDimension("Y21_155", len(Y21))

# Create variables
lons = file_out.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_out.createVariable("Y21_155", N.int32, ("Y21_155",))
data1 = file_out.createVariable(q, N.float32, ("Y21_155", "X12_84"))
lons2 = file_out.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_out.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# Assign units and metadata
lons.units = X12_units
lats.units = Y21_units
data1.units = z_units
lons2.units = lon_units
lats2.units = lat_units
data1.long_name = lon_name

# Write data
lons[:] = X12[:]
lats[:] = Y21[:]
data1[:] = ma_data_masked[:, :]
lons2[:] = longitude[:, :]
lats2[:] = latitude[:, :]

# Close file
file_out.close()