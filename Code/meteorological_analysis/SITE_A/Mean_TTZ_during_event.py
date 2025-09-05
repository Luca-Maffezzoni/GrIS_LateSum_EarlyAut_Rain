# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:38:06 2020

@author: lucam
"""

import os
import numpy as N
from netCDF4 import Dataset

# =========================
# ROOT DIRECTORY
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))

# Variable name to extract
q = "TTZ"

# =========================
# OPEN INPUT NETCDF FILE
# =========================
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2013.nc")
)

# Extract coordinate variables
Y21 = fileobj.variables["Y21_155"][:]
X12 = fileobj.variables["X12_84"][:]
latitudine = fileobj.variables["LAT"][:, :]
longitudine = fileobj.variables["LON"][:, :]

# =========================
# EXTRACT UNITS
# =========================
Y21_units = fileobj.variables["Y21_155"].units
X12_units = fileobj.variables["X12_84"].units
lat_units = fileobj.variables["LAT"].units
lon_units = fileobj.variables["LON"].units
z_units = fileobj.variables[q].units

# Long name of variable q
lon_name = fileobj.variables[q].long_name

# =========================
# EXTRACT VALUES
# =========================
# Select data for 7 time steps (247–253) at first vertical level (0)
z = fileobj.variables[q][247:254, 0, :, :]
# Reshape data into (time, lat, lon)
data = N.reshape(z, (7, 135, 73))
# Compute mean across the time dimension
data_mean = N.mean(data, axis=0)

# Close input file
fileobj.close()

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_prova = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "TTZ_during_event.nc"),
    "w",
    format="NETCDF4_CLASSIC"
)

# Create dimensions
lon = file_prova.createDimension("X12_84", len(X12))
lat = file_prova.createDimension("Y21_155", len(Y21))

# Create variables
lons = file_prova.createVariable("X12_84", N.int32, ("X12_84",))
lats = file_prova.createVariable("Y21_155", N.int32, ("Y21_155",))
data1 = file_prova.createVariable("TTZ", N.float32, ("Y21_155", "X12_84"))
lons2 = file_prova.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
lats2 = file_prova.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

# =========================
# ASSIGN UNITS AND ATTRIBUTES
# =========================
lons.units = X12_units
lats.units = Y21_units
data1.units = z_units
lons2.units = lon_units
lats2.units = lat_units
data1.long_name = lon_name

# =========================
# WRITE DATA INTO VARIABLES
# =========================
lons[:] = X12[:]
lats[:] = Y21[:]
data1[:, :] = data_mean[:, :]
lons2[:, :] = longitudine[:, :]
lats2[:, :] = latitudine[:, :]

# Add global attribute (title)
file_prova.title = "Mean_TTZ_during_event"

# Close output file
file_prova.close()



