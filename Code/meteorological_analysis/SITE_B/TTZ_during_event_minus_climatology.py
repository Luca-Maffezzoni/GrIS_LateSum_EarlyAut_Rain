# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:43:21 2020

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
# OPEN INPUT NETCDF FILES
# =========================
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "TTZ_mean_1985-2015.nc")
)
fileobj2 = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "TTZ_during_event.nc")
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
# EXTRACT VARIABLES
# =========================
# Climatology data
z = fileobj.variables[q][:, :]
# Event data
z2 = fileobj2.variables[q][:, :]

# Compute anomaly: event minus climatology
result = z2 - z

# Close input files
fileobj.close()
fileobj2.close()

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
output = os.path.join(
    ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "TTZ_during_event_minus_climatology.nc"
)
file_prova = Dataset(output, "w", format="NETCDF4_CLASSIC")

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
data1[:, :] = result[:, :]
lons2[:, :] = longitudine[:, :]
lats2[:, :] = latitudine[:, :]

# Add global attribute (title)
file_prova.title = "TTZ_during_event_minus_climatology"

# Close output file
file_prova.close()