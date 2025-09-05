# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:38:06 2020

@author: lucam
"""

import os
import numpy as np
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY
# =========================
# The folder where this script is located. This allows using relative paths for input/output files.
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# VARIABLE TO EXTRACT
# =========================
# 'q' is the name of the variable in the NetCDF file we want to extract.
q = "CM"

# =========================
# OPEN INPUT NETCDF FILE
# =========================
# Path to the raw MAR dataset for 2015
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc")
)

# =========================
# EXTRACT COORDINATES
# =========================
# Extract 1D coordinate arrays for Y and X dimensions
Y21 = fileobj.variables["Y21_155"][:]  # Y-dimension
X12 = fileobj.variables["X12_84"][:]   # X-dimension

# Extract 2D latitude and longitude grids
latitudes = fileobj.variables["LAT"][:, :]
longitudes = fileobj.variables["LON"][:, :]

# =========================
# EXTRACT UNITS AND METADATA
# =========================
# Units of coordinates and variable
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[q].units

# Long name (description) of the variable
variable_long_name = fileobj.variables[q].long_name

# =========================
# EXTRACT DATA AND COMPUTE MEAN
# =========================
# Extract the variable data for a specific time range (indices 239 to 248)
z = fileobj.variables[q][239:249, :, :]  # shape = (10, 135, 73)

# Reshape and compute the temporal mean
data = np.reshape(z, (10, 135, 73))
data_mean = np.mean(data, axis=0)

# Close the input NetCDF file
fileobj.close()

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
output_file = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "CM_during_event_28aug_6sep.nc"),
    "w",  # write mode
    format="NETCDF4_CLASSIC"
)

# =========================
# DEFINE DIMENSIONS
# =========================
lon_dim = output_file.createDimension("X12_84", len(X12))  # X dimension
lat_dim = output_file.createDimension("Y21_155", len(Y21))  # Y dimension

# =========================
# DEFINE VARIABLES
# =========================
# 1D coordinate variables
lons = output_file.createVariable("X12_84", np.int32, ("X12_84",))
lats = output_file.createVariable("Y21_155", np.int32, ("Y21_155",))

# 2D variable for the mean CM data
data_var = output_file.createVariable("TTZ", np.float32, ("Y21_155", "X12_84"))

# 2D latitude and longitude grids
lons2 = output_file.createVariable("LON", np.float32, ("Y21_155", "X12_84"))
lats2 = output_file.createVariable("LAT", np.float32, ("Y21_155", "X12_84"))

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
data_var[:, :] = data_mean[:, :]
lons2[:, :] = longitudes[:, :]
lats2[:, :] = latitudes[:, :]

# Add title metadata
output_file.title = "Mean_CM_during_event"

# Close the output file to save changes
output_file.close()



