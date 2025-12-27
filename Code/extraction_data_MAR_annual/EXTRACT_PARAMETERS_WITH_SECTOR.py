



import os
import numpy as N
from netCDF4 import Dataset


# ---------------------------------------------------------------------------
# ROOT DIRECTORY
# ---------------------------------------------------------------------------
ROOT = os.path.dirname(__file__)

# ---------------------------------------------------------------------------
# SCRIPT DESCRIPTION
# ---------------------------------------------------------------------------
# This script processes annual MAR model NetCDF (.nc) outputs for selected
# variables as surface mass balance (SMB) runoff (RU) and TTZ (TAS) over Greenland. 
# The original MAR model provides yearly outputs of many variables from **1958 to 2016**.
#
# The complete dataset is not stored in any
# directory within this project due to its large size.
#
# In this version, the file paths are therefore **imaginary**
# and only represent the structure of the real workflow.
#
# The script extracts and processes data specifically for the time period 1985-2015 and saves the
# results into new NetCDF files located in RAW data. 
# They are the only annual data useful for the analysis in this project and so extracted and shown
# ---------------------------------------------------------------------------


# Imaginary MAR dataset paths
# (One file per year, no real file is required)
# -----------------------------------------------------------------------
# IMAGINARY INPUT FILES (YEARS 1985–2015)
# -----------------------------------------------------------------------
# The real MAR dataset includes annual output files from 1958 to 2016.
# Here we only consider years from 1985 to 2015 for this work, represented
# by files that are not physically present in any directory.
# -----------------------------------------------------------------------


# Years 1985–2015
FILES = [
    r"ImaginaryPath\MARv3.9.2_NCEP1-20km_" + str(year) + ".nc"
    for year in range(1985, 2015 + 1)
]

for q in ["SMB", "RU", "TTZ"]:
    for x in FILES:
        # extract year from filename
        fname = os.path.basename(x)
        year = int(fname[-8:-3])

        # -------------------------------------------------------------------
        # OUTPUT FOLDER
        # -------------------------------------------------------------------
        output_folder = os.path.join(
            ROOT, "..", "..", "..", "Data", "RAW",
            "MAR_ANNUAL",
            q
        )
        os.makedirs(output_folder, exist_ok=True)

        # -------------------------------------------------------------------
        # OUTPUT FILE NAME (YEAR-BASED)
        # -------------------------------------------------------------------
        output_filename = f"annual_{q}_MARv3.9.2_NCEP1-20km_{year}.nc"
        output_path = os.path.join(output_folder, output_filename)

        # -------------------------------------------------------------------
        # READ INPUT FILE (imaginary path)
        # -------------------------------------------------------------------
        fileobj = Dataset(x)  # read a single file .nc (imaginary)

        # EXTRACT VARIABLES
        Y21 = fileobj.variables["Y21_155"][:]
        X12 = fileobj.variables["X12_84"][:]
        latitude = fileobj.variables["LAT"][:, :]
        longitude = fileobj.variables["LON"][:, :]
        data = fileobj.variables[q][:, 0, :, :]
        time = fileobj.variables["TIME"][:]

        # EXTRACT UNITS
        Y21_units = fileobj.variables["Y21_155"].units
        X12_units = fileobj.variables["X12_84"].units
        lat_units = fileobj.variables["LAT"].units
        lon_units = fileobj.variables["LON"].units
        t_units = fileobj.variables["TIME"].units
        z_units = fileobj.variables[q].units
        lon_name = fileobj.variables[q].long_name
        fileobj.close()

        # -------------------------------------------------------------------
        # WRITE OUTPUT FILE
        # -------------------------------------------------------------------
        file_prova = Dataset(output_path, "w", format="NETCDF4_CLASSIC")

        # make dimensions
        lon = file_prova.createDimension("X12_84", len(X12))
        lat = file_prova.createDimension("Y21_155", len(Y21))
        timess = file_prova.createDimension("TIME", len(time))

        # make variables
        lons = file_prova.createVariable("X12_84", N.int32, ("X12_84",))
        lats = file_prova.createVariable("Y21_155", N.int32, ("Y21_155",))
        times = file_prova.createVariable("TIME", "f", ("TIME",))
        data1 = file_prova.createVariable(q, N.float32, ("TIME", "Y21_155", "X12_84"))
        lons2 = file_prova.createVariable("LON", N.float32, ("Y21_155", "X12_84"))
        lats2 = file_prova.createVariable("LAT", N.float32, ("Y21_155", "X12_84"))

        # assign units
        lons.units = X12_units
        lats.units = Y21_units
        times.units = t_units
        data1.units = z_units
        lons2.units = lon_units
        lats2.units = lat_units
        data1.long_name = lon_name

        # write data
        lons[:] = X12[:]
        lats[:] = Y21[:]
        times[:] = time[:]
        data1[:] = data[:, :, :]
        lons2[:] = longitude[:, :]
        lats2[:] = latitude[:, :]

        # title
        file_prova.title = "parameter_" + q
        file_prova.close()