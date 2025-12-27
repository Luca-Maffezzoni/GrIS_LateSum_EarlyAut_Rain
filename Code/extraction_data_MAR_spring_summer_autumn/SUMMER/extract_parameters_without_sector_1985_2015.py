# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:49:08 2019

@author: lucam
"""

import numpy as np
from netCDF4 import Dataset
import os
import numpy.ma as ma


# ---------------------------------------------------------------------------
# SCRIPT DESCRIPTION
# ---------------------------------------------------------------------------
# This script processes annual MAR model NetCDF (.nc) outputs for the selected
# variable as Rainfall (RF) over Greenland. 
# The original MAR model provides yearly outputs from **1958 to 2016**.
#
# The complete dataset is not stored in any
# directory within this project due to its large size.
#
# In this version, the file paths are therefore **imaginary**
# and only represent the structure of the real workflow.
#
# The script extracts and processes data specifically for the time period 1985-2015,applies a Rignot basin 
# mask (to include only the real GrIS basins), and saves the
# results into new NetCDF files for glaciological summer analysis. 
# They are the only data in summer useful for the analysis in this project and so extracted and shown
# ---------------------------------------------------------------------------


# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

ROOT = os.path.dirname(__file__)

# Variables to extract (from your original script)
VARIABLES = ["RF"]

# Years 1985–2015
YEARS = list(range(1985, 2015 + 1))

# Leap years according to YOUR ORIGINAL LOGIC
LEAP_YEARS = [1988, 1992, 1996, 2000, 2004, 2008, 2012]

# Imaginary MAR dataset paths
# (One file per year, no real file is required)
# -----------------------------------------------------------------------
# IMAGINARY INPUT FILES (YEARS 1958–2016)
# -----------------------------------------------------------------------
# The real MAR dataset includes annual output files from 1958 to 2016.
# Here we only consider years from 1985 to 2015, represented
# by files that are not physically present in any directory.
# -----------------------------------------------------------------------
FILES = [
    fr"ImaginaryPath\MARv3.9.2_NCEP1-20km_{year}.nc"
    for year in YEARS
]

# Rignot mask path
RIGNOT_MASK_PATH = os.path.join(
    ROOT, "..", "..", "..", "Data", "RAW", "Rignot_Mask_without_zero.nc"
)

# ------------------------------------------------------------
# MAIN SCRIPT
# ------------------------------------------------------------

for q in VARIABLES:

    for x in FILES:
        fname = os.path.basename(x)

        # Extract year from filename
        year = None
        for Y in YEARS:
            if str(Y) in fname:
                year = Y
                break

        if year is None:
            continue

        print(f"Processing {year} → variable {q}")

        # Open imaginary MAR file
        fileobj = Dataset(x)

        # ---------------- GRID VARIABLES ----------------
        Y21 = fileobj.variables["Y21_155"][:]
        X12 = fileobj.variables["X12_84"][:]
        latitude = fileobj.variables["LAT"][:, :]
        longitude = fileobj.variables["LON"][:, :]

        # ------------------------------------------------------------
        # SUMMER EXTRACTION — EXACTLY YOUR ORIGINAL LEAP/NON-LEAP LOGIC
        # ------------------------------------------------------------
        if year in LEAP_YEARS:
            # Leap year logic
            start = 152
            end = 244
            # TIME
            time = np.array([fileobj.variables["TIME"][w] for w in range(start, end)], dtype="f")
            # VARIABLE
            z = fileobj.variables[q][start, :, :]
            for m in range(start + 1, end):
                shf = fileobj.variables[q][m, :, :]
                z = np.concatenate((z, shf))
            data = np.reshape(z, (92, 135, 73))

        else:
            # Normal year logic
            start = 151
            end = 243
            time = np.array([fileobj.variables["TIME"][w] for w in range(start, end)], dtype="f")
            z = fileobj.variables[q][start, :, :]
            for m in range(start + 1, end):
                shf = fileobj.variables[q][m, :, :]
                z = np.concatenate((z, shf))
            data = np.reshape(z, (92, 135, 73))

        # ---------------- METADATA ----------------
        Y21_units = fileobj.variables["Y21_155"].units
        X12_units = fileobj.variables["X12_84"].units
        lat_units = fileobj.variables["LAT"].units
        lon_units = fileobj.variables["LON"].units
        t_units = fileobj.variables["TIME"].units
        z_units = fileobj.variables[q].units
        long_name_q = fileobj.variables[q].long_name

        fileobj.close()

        # ------------------------------------------------------------
        # APPLY RIGNOT MASK
        # ------------------------------------------------------------
        mask_file = Dataset(RIGNOT_MASK_PATH)
        mask = mask_file.variables["BASIN"][:, :]
        mask_file.close()

        # 3D mask aligned with time dimension
        mask_grid, _ = np.meshgrid(mask, time)
        mask_3D = np.reshape(mask_grid, (len(time), len(Y21), len(X12)))

        masked_data = ma.masked_where(np.isnan(mask_3D), data)
        setattr(masked_data, "fill_value", float("NaN"))
        data_filled = ma.filled(masked_data)

        # Mask LAT and LON
        lat_masked = ma.masked_where(np.isnan(mask), latitude)
        setattr(lat_masked, "fill_value", float("NaN"))
        latitude_filled = ma.filled(lat_masked)

        lon_masked = ma.masked_where(np.isnan(mask), longitude)
        setattr(lon_masked, "fill_value", float("NaN"))
        longitude_filled = ma.filled(lon_masked)

        # ------------------------------------------------------------
        # OUTPUT FOLDER
        # ------------------------------------------------------------
        output_folder = os.path.join(
            ROOT, "..", "..", "..", "Data", "RAW",
            "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION",
            f"SUMMER_MAR_3_{year}"
        )
        os.makedirs(output_folder, exist_ok=True)
        
        # -------------------------------------------------------------------
        # OUTPUT FILE NAME (YEAR-BASED)
        # -------------------------------------------------------------------
        
        output_filename = f"sum_{q}_MARv3.9.2_NCEP1-20km_{year}.nc"
        output_path = os.path.join(output_folder, output_filename)

        # ------------------------------------------------------------
        # WRITE NETCDF OUTPUT
        # ------------------------------------------------------------
        nc = Dataset(output_path, "w", format="NETCDF4_CLASSIC")

        nc.createDimension("X12_84", len(X12))
        nc.createDimension("Y21_155", len(Y21))
        nc.createDimension("TIME", len(time))

        var_lon = nc.createVariable("X12_84", np.int32, ("X12_84",))
        var_lat = nc.createVariable("Y21_155", np.int32, ("Y21_155",))
        var_time = nc.createVariable("TIME", "f", ("TIME",))
        var_data = nc.createVariable(q, np.float32, ("TIME", "Y21_155", "X12_84"))
        var_lon2 = nc.createVariable("LON", np.float32, ("Y21_155", "X12_84"))
        var_lat2 = nc.createVariable("LAT", np.float32, ("Y21_155", "X12_84"))

        # Units
        var_lon.units = X12_units
        var_lat.units = Y21_units
        var_time.units = t_units
        var_data.units = z_units
        var_lon2.units = lon_units
        var_lat2.units = lat_units
        var_data.long_name = long_name_q

        # Write
        var_lon[:] = X12
        var_lat[:] = Y21
        var_time[:] = time
        var_data[:] = data_filled
        var_lon2[:] = longitude_filled
        var_lat2[:] = latitude_filled

        nc.title = f"parameter_{q}_summer_{year}"
        nc.close()