# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:22:56 2020

@author: lucam
"""

import os
import numpy as N
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY
# =========================
# Get the directory where this script is located. 
# This allows using relative paths for input/output files.
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# VARIABLE TO EXTRACT
# =========================
# 'RF' represents rainfall in the NetCDF dataset
q = "RF"

# =========================
# OPEN INPUT NETCDF FILE
# =========================
# Open the MAR dataset for 2015 (or 2013, adjust filename if needed)
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc")
)

# =========================
# EXTRACT COORDINATES
# =========================
# 1D coordinate arrays for X and Y dimensions
Y21 = fileobj.variables["Y21_155"][:]  # Y-dimension indices
X12 = fileobj.variables["X12_84"][:]   # X-dimension indices

# 2D grids of latitude and longitude
latitudes = fileobj.variables["LAT"][:, :]
longitudes = fileobj.variables["LON"][:, :]

# =========================
# EXTRACT UNITS AND METADATA
# =========================
# Units for coordinates and variable
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[q].units

# Descriptive long name of the variable
variable_long_name = fileobj.variables[q].long_name

# =========================
# EXTRACT DATA AND COMPUTE TOTAL RAINFALL
# =========================
# Extract rainfall data for a specific time range (here, indices 239 to 248)
z = fileobj.variables[q][239:249, :, :]  # shape: (10, 135, 73)

# Reshape to ensure correct 3D structure (time, Y, X)
data = N.reshape(z, (10, 135, 73))

# Compute total rainfall over the selected period (sum along the time axis)
data_sum = N.sum(data, axis=0)

# Close the input NetCDF file
fileobj.close()

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_prova = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", 
                 "SITE_B", "Total_rainfall_during_event_28aug_6sep.nc"),
    "w",  # write mode
    format="NETCDF4_CLASSIC"
)

# =========================
# DEFINE DIMENSIONS
# =========================
# Define X and Y dimensions
lon_dim = file_prova.createDimension("X12_84", len(X12))
lat_dim = file_prova.createDimension("Y21_155", len(Y21))

# =========================
# DEFINE VARIABLES
# =========================
# 1D coordinate variables
lons = file_prova.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_prova.createVariable("Y21_155", N.int32, ("Y21_155",))

# 2D variable for total rainfall
data_var = file_prova.createVariable("RF", N.float32, ("Y21_155", "X12_84"))

# 2D latitude and longitude grids
lons2 = file_prova.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_prova.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# =========================
# ASSIGN UNITS AND METADATA
# =========================
lons.units = X12_units
lats.units = Y21_units
data_var.units = z_units
lons2.units = lon_units
lats2.units = lat_units
data_var.long_name = variable_long_name

# =========================
# WRITE DATA TO VARIABLES
# =========================
lons[:] = X12[:]
lats[:] = Y21[:]
data_var[:, :] = data_sum[:, :]
lons2[:, :] = longitudes[:, :]
lats2[:, :] = latitudes[:, :]

# Add a title to the NetCDF file
file_prova.title = "Total_rainfall_during_event"

# Close the file to save all changes
file_prova.close()