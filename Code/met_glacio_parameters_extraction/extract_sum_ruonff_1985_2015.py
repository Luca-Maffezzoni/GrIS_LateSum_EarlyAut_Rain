# -*- coding: utf-8 -*-
"""
Compute cumulative Runoff (RU) from MAR model NetCDF files
Years: 1985–2015
Author: lucam (adapted for repo structure)
"""
import os
import numpy as np
import numpy.ma as ma
from netCDF4 import Dataset

# Define repo root relative to this script
ROOT = os.path.dirname(__file__)

# Input folders
raw_dir = os.path.join(ROOT, "..", "..", "Data", "RAW", "MAR_ANNUAL", "RU")
mask_file = os.path.join(ROOT, "..", "..", "Data", "RAW", "Rignot_Mask_without_zero.nc")

# Output folder
output_file = os.path.join(ROOT, "..", "..", "Data", "PROCESSED", "MET_GLACIO_PARAMETERS", "sum_RU_1985_2015.nc")

# Initialize an array of zeros for cumulative runoff (grid size 135x73 in MAR)
z = np.zeros((135, 73))

# Variable of interest: Runoff
for q in ["RU"]:
    for year in range(1985, 2016):
        # Open MAR NetCDF file for each year
        infile = os.path.join(raw_dir, f"annual_RU_MARv3.9.2_NCEP1-20km_{year}.nc")
        fileobj = Dataset(infile)

        # Read coordinates and variables
        Y21 = fileobj.variables["Y21_155"][:]
        X12 = fileobj.variables["X12_84"][:]
        latitude = fileobj.variables["LAT"][:, :]
        longitude = fileobj.variables["LON"][:, :]

        # Extract metadata
        Y21_units = fileobj.variables["Y21_155"].units
        X12_units = fileobj.variables["X12_84"].units
        lat_units = fileobj.variables["LAT"].units
        lon_units = fileobj.variables["LON"].units
        z_units = fileobj.variables[q].units
        lon_name = fileobj.variables[q].long_name

        # Extract RU variable (all timesteps, first vertical level, full grid)
        data = fileobj.variables[q][:, :, :]

        # Sum along time dimension → annual sum
        data_sum = np.sum(data, axis=0)

        # Add to cumulative field
        z = z + data_sum

# Open mask file (basins)
fileobj_2 = Dataset(mask_file)
mask = fileobj_2.variables["BASIN"][:, :]
fileobj_2.close()

# Apply mask: hide invalid pixels (NaN in mask)
ma_data = ma.masked_where(np.isnan(mask), z)
setattr(ma_data, "fill_value", float("NaN"))
z2 = ma.filled(ma_data)

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_out = Dataset(output_file, "w", format="NETCDF4_CLASSIC")

# Define dimensions
file_out.createDimension("X12_84", len(X12))
file_out.createDimension("Y21_155", len(Y21))

# Define variables
lons = file_out.createVariable("X12_84", np.int32, ("X12_84",))
lats = file_out.createVariable("Y21_155", np.int32, ("Y21_155",))
data1 = file_out.createVariable(q, np.float32, ("Y21_155", "X12_84"))
lons2 = file_out.createVariable("LON", np.float32, ("Y21_155", "X12_84"))
lats2 = file_out.createVariable("LAT", np.float32, ("Y21_155", "X12_84"))

# Assign metadata
lons.units = X12_units
lats.units = Y21_units
data1.units = z_units
lons2.units = lon_units
lats2.units = lat_units
data1.long_name = lon_name

# Write data
lons[:] = X12[:]
lats[:] = Y21[:]
data1[:] = z2[:, :]
lons2[:] = longitude[:, :]
lats2[:] = latitude[:, :]

# Close file
file_out.close()