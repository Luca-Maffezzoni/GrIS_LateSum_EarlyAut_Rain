# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:50:39 2020

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

# Initialize empty array to store concatenated data
# Shape: (1, 135, 73) → later extended with data from all years
data_mean_concatenate = N.zeros((1, 135, 73))

# =========================
# LOOP OVER YEARS (1985–2015)
# =========================
for i in range(1985, 2016):
    # Open input NetCDF file for each year
    fileobj = Dataset(
        os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_ANNUAL", "TTZ", f"annual_TTZ_MARv3.9.2_NCEP1-20km_{i}.nc")
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
    # Select 7 time steps (247–253) at first vertical level (0)
    z = fileobj.variables[q][247:254, :, :]
    # Reshape data into (7, 135, 73)
    data = N.reshape(z, (7, 135, 73))
    # Concatenate new data to global container
    data_mean_concatenate = N.concatenate((data_mean_concatenate, data))

    # Close current year file
    fileobj.close()

# =========================
# PROCESS CONCATENATED DATA
# =========================
# Reshape into (218, 135, 73): 31 years × 7 days = 217 → plus initial dummy row
data_mean_concatenate_finali = N.reshape(data_mean_concatenate, (218, 135, 73))

# Remove first dummy row → final shape: (217, 135, 73)
data_mean_preparati = data_mean_concatenate_finali[1:, :, :]

# Compute mean climatology across all years
data_mean_finali = N.mean(data_mean_preparati, axis=0)

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_prova = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "TTZ_mean_1985-2015.nc"),
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
data1[:, :] = data_mean_finali[:, :]
lons2[:, :] = longitudine[:, :]
lats2[:, :] = latitudine[:, :]

# Add global attribute (title)
file_prova.title = "Mean_TTZ_during_event_climatology_1985-2015"

# Close output file
file_prova.close()