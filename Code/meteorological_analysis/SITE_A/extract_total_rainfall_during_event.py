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
# Get the directory where this script is located. This allows using relative paths.
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# VARIABLE TO EXTRACT
# =========================
# 'RF' is the variable for rainfall in the NetCDF file
q = "RF"

# =========================
# OPEN INPUT NETCDF FILE
# =========================
# Open the MAR dataset for 2013
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_ANNUAL", "RF", "annual_RF_MARv3.9.2_NCEP1-20km_2013.nc")
)

# =========================
# EXTRACT COORDINATES
# =========================
Y21 = fileobj.variables["Y21_155"][:]   # Y dimension indices
X12 = fileobj.variables["X12_84"][:]    # X dimension indices
latitudes = fileobj.variables["LAT"][:, :]   # 2D latitude grid
longitudes = fileobj.variables["LON"][:, :]  # 2D longitude grid

# =========================
# EXTRACT UNITS AND METADATA
# =========================
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[q].units  # units of rainfall
variable_long_name = fileobj.variables[q].long_name  # descriptive name

# =========================
# EXTRACT DATA AND COMPUTE TOTAL
# =========================
# Extract rainfall for days 247 to 253 (7 days)
z = fileobj.variables[q][247:254, :, :]
data = N.reshape(z, (7, 135, 73))      # reshape to explicit 3D array
data_sum = N.sum(data, axis=0)         # sum over the time dimension

fileobj.close()  # close input file

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_prova = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "Total_rainfall_during_event.nc"),
    "w",
    format="NETCDF4_CLASSIC"
)

# =========================
# DEFINE DIMENSIONS
# =========================
lon_dim = file_prova.createDimension("X12_84", len(X12))
lat_dim = file_prova.createDimension("Y21_155", len(Y21))

# =========================
# DEFINE VARIABLES
# =========================
lons = file_prova.createVariable("X12_84", N.int32, ("X12_84",))  # 1D X coordinate
lats = file_prova.createVariable("Y21_155", N.int32, ("Y21_155",))  # 1D Y coordinate
data_var = file_prova.createVariable("RF", N.float32, ("Y21_155", "X12_84"))  # rainfall
lons2 = file_prova.createVariable("LON", N.float32, ("Y21_155", "X12_84"))    # 2D longitude
lats2 = file_prova.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))    # 2D latitude

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

# Add file title
file_prova.title = "Total_rainfall_during_event"

# Close output file to save changes
file_prova.close()