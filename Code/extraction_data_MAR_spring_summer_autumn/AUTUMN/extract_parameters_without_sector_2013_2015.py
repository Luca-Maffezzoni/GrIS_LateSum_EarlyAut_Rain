# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:45:59 2019

@author: lucam
"""

import numpy as np
from netCDF4 import Dataset
import os
import numpy.ma as ma

# ---------------------------------------------------------------------------
# SCRIPT DESCRIPTION
# ---------------------------------------------------------------------------
# This script processes annual MAR model NetCDF (.nc) outputs for selected
# variables that are (Short Wave Downward (SWD), Long Wave Downard (LWD), Long Wave Upward (LWU), Sensible Heat Flux (SHF) and Latent Heat Flux (LHF) over Greenland. 
# The original MAR model provides yearly outputs from **1958 to 2016**.
#
# The complete dataset is not stored in any
# directory within this project due to its large size.
#
# In this version, the file paths are therefore **imaginary**
# and only represent the structure of the real workflow.
#
# The script extracts and processes data specifically for the years
# **2013** and **2015**, applies a Rignot basin mask (to include only the real GrIS basins), and saves the
# results into new NetCDF files for glaciological autmumn analysis. 
# They are the only data in autumn useful for the analysis in this project and so extracted and shown
# ---------------------------------------------------------------------------

# Define ROOT path (used for relative paths)
ROOT = os.path.dirname(__file__)

# Loop over the variables of interest
for q in ["SWD","LWD","LWU","SHF","LHF"]:

    # -----------------------------------------------------------------------
    # IMAGINARY INPUT FILES (YEARS 1958–2016)
    # -----------------------------------------------------------------------
    # The real MAR dataset includes annual output files from 1958 to 2016.
    # Here we only consider two  years (2013 and 2015), represented
    # by two files that are not physically present in any directory.
    # -----------------------------------------------------------------------
    files = [
        r"ImaginaryPath\MARv3.9.2_NCEP1-20km_2013.nc",
        r"ImaginaryPath\MARv3.9.2_NCEP1-20km_2015.nc"
    ]

    # -----------------------------------------------------------------------
    # RIGNOT MASK FILE
    # -----------------------------------------------------------------------
    rignot_mask_path = os.path.join(
        ROOT, "..", "..", "..", "Data", "RAW", "Rignot_Mask_without_zero.nc"
    )

    # -----------------------------------------------------------------------
    # MAIN PROCESSING LOOP
    # -----------------------------------------------------------------------
    for x in files:
        a = os.path.basename(x)

        # -------------------------------------------------------------------
        # DETECT THE YEAR FROM FILE NAME
        # -------------------------------------------------------------------
        # Instead of using a numeric counter, the year is automatically
        # extracted from the file name (e.g., "2013" or "2015").
        # This keeps the workflow simpler and directly tied to each file.
        # -------------------------------------------------------------------
        if "2013" in a:
            year = 2013
        elif "2015" in a:
            year = 2015
        else:
            year = "unknown"

        # Open the (imaginary) MAR NetCDF file
        fileobj = Dataset(x)
        
        # --- EXTRACT GRID VARIABLES ---
        Y21 = fileobj.variables["Y21_155"][:]
        X12 = fileobj.variables["X12_84"][:]
        latitude = fileobj.variables["LAT"][:,:]
        longitude = fileobj.variables["LON"][:,:]
        
        # --- SELECT TIME AND VARIABLE DATA ---
        # Extract time slices corresponding to the autumn period
        time=np.array([],dtype="f")
        for w in range(243,334):
            p=fileobj.variables["TIME"][w]
            time=np.append(time,p)
        # Extract variable data
        z=fileobj.variables[q][243,:,:]
        for m in range(244,334):
            shf=fileobj.variables[q][m,:,:]
            z=np.concatenate((z,shf))
        data=np.reshape(z,(91,135,73))
                    
        # --- EXTRACT UNITS AND METADATA ---
        Y21_units = fileobj.variables["Y21_155"].units
        X12_units = fileobj.variables["X12_84"].units
        lat_units = fileobj.variables["LAT"].units
        lon_units = fileobj.variables["LON"].units
        t_units = fileobj.variables["TIME"].units
        z_units = fileobj.variables[q].units
        lon_name = fileobj.variables[q].long_name
        fileobj.close()
        
        # -------------------------------------------------------------------
        # APPLY RIGNOT MASK
        # -------------------------------------------------------------------
        fileobj_2 = Dataset(rignot_mask_path)
        mask = fileobj_2.variables["BASIN"][:, :]
        fileobj_2.close()

        [mask_grid, _] = np.meshgrid(mask, time)
        mask_grid_3D = np.reshape(mask_grid, (len(time), len(Y21), len(X12)))

        masked_data = ma.masked_where(np.isnan(mask_grid_3D), data)
        setattr(masked_data, "fill_value", float("NaN"))
        z = ma.filled(masked_data)

        # Mask LAT and LON
        lat_masked = ma.masked_where(np.isnan(mask), latitude)
        setattr(lat_masked, "fill_value", float("NaN"))
        latitude_filled = ma.filled(lat_masked)

        lon_masked = ma.masked_where(np.isnan(mask), longitude)
        setattr(lon_masked, "fill_value", float("NaN"))
        longitude_filled = ma.filled(lon_masked)
        
        # -------------------------------------------------------------------
        # OUTPUT DIRECTORY BASED ON YEAR
        # -------------------------------------------------------------------
        if year == 2013:
            output_folder = os.path.join(
                ROOT, "..", "..", "..", "Data", "RAW",
                "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION",
                "AUTUMN_MAR_4_2013"
            )
        elif year == 2015:
            output_folder = os.path.join(
                ROOT, "..", "..", "..", "Data", "RAW",
                "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION",
                "AUTUMN_MAR_4_2015"
            )
        else:
            output_folder = os.path.join(
                ROOT, "..", "..", "..", "Data", "RAW",
                "MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION"
            )

        os.makedirs(output_folder, exist_ok=True)

        # -------------------------------------------------------------------
        # OUTPUT FILE NAME (YEAR-BASED)
        # -------------------------------------------------------------------
        output_filename = f"autumn_{q}_MARv3.9.2_NCEP1-20km_{year}.nc"
        output_path = os.path.join(output_folder, output_filename)
        
        # -------------------------------------------------------------------
        # CREATE AND WRITE NEW NETCDF OUTPUT FILE
        # -------------------------------------------------------------------
        file_out = Dataset(output_path, "w", format="NETCDF4_CLASSIC")
        
        # Create dimensions
        file_out.createDimension("X12_84", len(X12))
        file_out.createDimension("Y21_155", len(Y21))
        file_out.createDimension("TIME", len(time))

        # Create variables
        lons = file_out.createVariable("X12_84", np.int32, ("X12_84",))
        lats = file_out.createVariable("Y21_155", np.int32, ("Y21_155",))
        times = file_out.createVariable("TIME", "f", ("TIME",))
        data1 = file_out.createVariable(q, np.float32, ("TIME", "Y21_155", "X12_84"))
        lons2 = file_out.createVariable("LON", np.float32, ("Y21_155", "X12_84"))
        lats2 = file_out.createVariable("LAT", np.float32, ("Y21_155", "X12_84"))

        # Assign units and metadata
        lons.units = X12_units
        lats.units = Y21_units
        times.units = t_units
        data1.units = z_units
        lons2.units = lon_units
        lats2.units = lat_units
        data1.long_name = lon_name

        # Write arrays
        lons[:] = X12[:]
        lats[:] = Y21[:]
        times[:] = time[:]
        data1[:] = z[:, :, :]
        lons2[:] = longitude_filled[:, :]
        lats2[:] = latitude_filled[:, :]

        # Add a descriptive title
        file_out.title = f"parameter_{q}_autumn_{year}"
        file_out.close()