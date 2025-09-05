# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:46:09 2020

@author: lucam
"""

import numpy as N
from netCDF4 import Dataset
import netCDF4
from datetime import datetime, timedelta 
from netCDF4 import num2date, date2num
import glob
import os
import numpy.ma as MA
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
raw_folder1 = os.path.join(ROOT, "..", "data", "raw")
raw_folder2 = os.path.join(ROOT, "..", "data", "raw","AUTUMN_MAR")

output_folder = os.path.join(ROOT, "..", "data", "output")
os.makedirs(output_folder, exist_ok=True)

#EXTRACT THE MASK FROM RIGNOT IN ORDER TO MASK THE VALUE OUTSIDE THE GRIS BASINS OF THE MAR MODEL OUTPUTS

main_file = os.path.join(raw_folder1, "Rignot_Mask_without_zero.nc")

if os.path.exists(main_file):
    fileobj1=Dataset(main_file)
    mask = fileobj1.variables["BASIN"][:,:]
    fileobj1.close()

# Extraction of the 20 days with maximum rainfall for each year from 2008 to 2016 in autumn since the daily values of rainfall in the .nc files cover only autumn
# Created array [9][20]: 9 years and 20 major events per year in autumn,
# where the 20th element (-1) represents the maximum.


data_finali=N.array([])


for x in range (2008,2017):
    filename = r"autumn_RF_MARv3.9.2_NCEP1-20km_"+str(x)+".nc"
    file_path = os.path.join(raw_folder2, filename)
    
    fileobj=Dataset(file_path)
    data1=N.array([],dtype="f")
    data = fileobj.variables["RF"][:,:,:]
    time = fileobj.variables["TIME"][:]
    for i in range (len(time)):
        variable=data[i]
        ma_data = MA.masked_where(mask!=53,variable) #mask everything apart from the south-west basin. Put 52 if you want only the west region.
        setattr(ma_data, "fill_value",float ("NaN"))
        ma_data_masked=MA.filled(ma_data)
        c=N.nansum(ma_data_masked)
        data1=N.append(data1,c)
    
    data_sorted=N.argsort(data1)
    
    data_extracted=data_sorted[-20:]
    
    data_finali=N.append(data_finali,data_extracted)

data_finali_reshape=N.reshape(data_finali,(9,20))
fileobj.close()

#Save the Array in .txt format
output_file = os.path.join(output_folder, "Extreme_rainfall_events_south_west_autumn.txt")# if you put above 52 in the mask you will obtain the same result but for the west region

N.savetxt(output_file,data_finali_reshape,delimiter=";",newline="\r\n",fmt="%.2d")

# In the first array, I extracted the 20 rainiest days of the season for each of the 9 years
# using NumPy's argsort function. This produces a 9x20 array (9 rows, 20 columns) where each
# row corresponds to a year and contains the indices of the 20 rainiest days, ordered from
# the least to the most rainy day of that year. See the previous .txt file generated.
#
# In the second array, I calculated the total rainfall for those specific days following
# the structure of the first array. This way, the second array contains the rainfall
# amounts, and by using the position in this array, I can reference the corresponding
# index (i.e., the day) in the first array. 
#
# At the end of this process, the second array has the same size and structure as the
# first array, and it is saved to a .txt file. This allows us to both see the rainfall
# amounts and, using the previous file "Extreme_rainfall_events_south_west_autumn.txt",
# associate each value with the exact day and year of the event.

s=2008
dati_finali_2=N.array([])

for p in range(0,9):
    filename = r"autumn_RF_MARv3.9.2_NCEP1-20km_"+str(s)+".nc"
    file_path = os.path.join(raw_folder2, filename)
    
    fileobj=Dataset(file_path)
    
    for z in range(0,20):
        data3 = fileobj.variables["RF"][int(data_finali_reshape[p,z]),:,:]
        ma_data2 = MA.masked_where(mask!=53,data3) #mask everything apart from the south-west region. Put 52 if you want only the west region.
        setattr(ma_data2, "fill_value",float ("NaN"))
        ma_data_masked2=MA.filled(ma_data2)
        data4 =N.nansum(ma_data_masked2)
        dati_finali_2=N.append(dati_finali_2,data4)
    fileobj.close()
    s=s+1
    

reshape_finale=N.reshape(dati_finali_2,(9,20))


#Save the Array in .txt format
output_file_2 = os.path.join(output_folder, "Extreme_rainfall_events_south_west_autumn_2.txt")# if you put above 52 in the mask you will obtain the same result but for the west region

N.savetxt(output_file_2,reshape_finale,delimiter=";",newline="\r\n",fmt="%.2d")

#===================================================================#
# Technical Note:
# Using the extraction of the largest daily cyclonic rainfall events identified above,
# we manually selected the events that occurred during late summer and early autumn 
# (August-September) for which ice velocity data were available both during and prior 
# to the events. Starting from the days of maximum rainfall, the entire cyclonic event 
# was then analyzed in detail.