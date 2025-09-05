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
q = "CM"

# =========================
# OPEN INPUT NETCDF FILE
# =========================
fileobj = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2013.nc")
)

Y21 = fileobj.variables["Y21_155"][:]
X12 = fileobj.variables["X12_84"][:]
latitudine=fileobj.variables["LAT"][:,:]
longitudine=fileobj.variables["LON"][:,:]
#EXTARCT UNITS
Y21_units=fileobj.variables["Y21_155"].units
X12_units=fileobj.variables["X12_84"].units
lat_units=fileobj.variables["LAT"].units
lon_units=fileobj.variables["LON"].units
z_units=fileobj.variables[q].units
#long-name of variable q
lon_name=fileobj.variables[q].long_name
#extract values
z=fileobj.variables[q][247:254,:,:]
data=N.reshape(z,(7,135,73))
data_mean=N.mean(data, axis=0)
fileobj.close()

# =========================
# CREATE OUTPUT NETCDF FILE
# =========================
file_prova = Dataset(
    os.path.join(ROOT, "..", "..", "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "CM_during_event_5sep_11sep.nc"),
    "w",
    format="NETCDF4_CLASSIC"
)

#make dimensions
lon = file_prova.createDimension("X12_84",len(X12))
lat = file_prova.createDimension("Y21_155",len(Y21))
#make variables
lons = file_prova.createVariable("X12_84",N.int32,("X12_84",))
lats = file_prova.createVariable("Y21_155",N.int32,("Y21_155",))
data1=file_prova.createVariable("TTZ",N.float32,("Y21_155","X12_84"))
lons2=file_prova.createVariable("LON",N.float32,("Y21_155","X12_84"))
lats2= file_prova.createVariable("LAT",N.float32,("Y21_155","X12_84"))
#make units
lons.units=X12_units
lats.units=Y21_units
data1.units=z_units
lons2.units=lon_units
lats2.units=lat_units
data1.long_name=lon_name

#write data
lons[:] = X12[:]
lats[:] = Y21[:]
data1[:] = data_mean[:,:]
lons2[:] = longitudine[:,:]
lats2[:] = latitudine[:,:]
#title 
file_prova.title="Mean_CM_during_event"
file_prova.close()



