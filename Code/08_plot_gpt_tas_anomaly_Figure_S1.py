# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:58:59 2021

@author: Luca
"""
import os
import sys
import numpy as np
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
from mpl_toolkits import basemap
import matplotlib.patches as patches

# =========================
# ROOT DIRECTORY
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))

# =========================
# Dynamically set PROJ_LIB for Basemap
# =========================
try:
    conda_prefix = os.environ.get('CONDA_PREFIX', sys.prefix)
    if os.name == 'nt':
        os.environ['PROJ_LIB'] = os.path.join(conda_prefix, 'Library', 'share')
    else:
        os.environ['PROJ_LIB'] = os.path.join(conda_prefix, 'share')
except Exception as e:
    print("Warning: Could not automatically set PROJ_LIB:", e)


#-----------------------GOPOTENTIAL EXTRACTION--------------------------
#EXTRACT NETCDF FILE 1
#------------------------------------------------------------------------
#EXTRACT GPT AT 500 hPa
fileobj = Dataset(os.path.join(ROOT, "..", "Data", "RAW", "SLP_HGT", "hgt.2015.nc"))
z=fileobj.variables["hgt"][239,5,:,:]
for m in range(240,249):
    shf=fileobj.variables["hgt"][m,5,:,:]
    z=np.concatenate((z,shf))
data=np.reshape(z,(10,73,144))
data_mean=np.mean(data, axis=0)
#EXTRACT LAT LON
lat=fileobj.variables["lat"][:]
lon=fileobj.variables["lon"][:]

#CHANGE 180 TO 360 TO -180 TO 0
lon1 = lon.copy()
for n, l in enumerate(lon1):
    if l >= 180:
       lon1[n]=lon1[n]-360. 
lon = lon1

#INVERT LONGITUDE CHANGED -180 A +180
variable1 = data_mean[:,0:72]
variable2 = data_mean[:,72:]
lon1 = lon[0:72]
lon2 = lon[72:]
#------------------------------------------------------------------------
#EXTRACT SLP (1000 hPa)
fileobj42 = Dataset(os.path.join(ROOT, "..", "Data", "RAW", "SLP_HGT", "slp.2015.nc"))
z42=fileobj42.variables["slp"][952,:,:]
for m in range(953,992):
    shf42=fileobj42.variables["slp"][m,:,:]
    z42=np.concatenate((z42,shf42))
data42=np.reshape(z42,(40,73,144))
data_mean42=np.mean(data42, axis=0)
fileobj42.close()
#------------------------------------------------------------------------

#MERGE LONGITUDES AND INVERT LATITUDES
variable_new = np.hstack((variable2, variable1))
lon_new = np.hstack((lon2, lon1))
lat_new = np.flipud(lat)
variable_new_flipped = np.flipud(variable_new)

#GENERATES NEW LAT,LON AND CREATE A GRID WITH NEW RESOLUTION TO INTERPOLATE
array_latitude=np.arange(-89.75,90,0.5)
array_longitude=np.arange(-179.75,180,0.5)
x2,y2 = np.meshgrid(array_longitude,array_latitude)

data_final = basemap.interp(variable_new_flipped, lon_new, lat_new, x2, y2, order=1)
fileobj.close()
#-----------------------------------------------------------------------------------------
#INVERT LONGITUDE CHANGED -180 A +180 and latitude for GPT at 1000 hPa
variable52 = data_mean42[:,0:72]
variable53 = data_mean42[:,72:]

variable_new54 = np.hstack((variable53, variable52))
variable_new_flipped55 = np.flipud(variable_new54)

data_final56 = basemap.interp(variable_new_flipped55, lon_new, lat_new, x2, y2, order=1)
#-----------------------------------------------------------------------------------------


#EXTRACT NETCDF FILE 4
#-----------------------------------------------------------------------------------------
#EXTRACT GPT AT 500 hPa
fileobj4 = Dataset(os.path.join(ROOT, "..", "Data", "RAW", "SLP_HGT", "hgt.2013.nc"))
z4=fileobj4.variables["hgt"][247,5,:,:]
for m in range(248,254):
    shf4=fileobj4.variables["hgt"][m,5,:,:]
    z4=np.concatenate((z4,shf4))
data4=np.reshape(z4,(7,73,144))
data_mean4=np.mean(data4, axis=0)
fileobj4.close()
#-----------------------------------------------------------------------------------------
#EXTRACT SLP (1000 hPa)
fileobj10 = Dataset(os.path.join(ROOT, "..", "Data", "RAW", "SLP_HGT", "slp.2013.nc"))
z10=fileobj10.variables["slp"][988,:,:]
for m in range(989,1016):
    shf10=fileobj10.variables["slp"][m,:,:]
    z10=np.concatenate((z10,shf10))
data10=np.reshape(z10,(28,73,144))
data_mean10=np.mean(data10, axis=0)
fileobj10.close()
#-----------------------------------------------------------------------------------------
#INVERT LONGITUDE CHANGED -180 A +180 and latitude for GPT at 1000 hPa
variable20 = data_mean10[:,0:72]
variable21 = data_mean10[:,72:]
variable_new22 = np.hstack((variable21, variable20))
variable_new_flipped22 = np.flipud(variable_new22)
data_final22 = basemap.interp(variable_new_flipped22, lon_new, lat_new, x2, y2, order=1)
#-----------------------------------------------------------------------------------------

#INVERT LONGITUDE CHANGED -180 A +180 and latitude for GPT at 500 hPa
variable7 = data_mean4[:,0:72]
variable8 = data_mean4[:,72:]
variable_new4 = np.hstack((variable8, variable7))
variable_new_flipped4 = np.flipud(variable_new4)

data_final4 = basemap.interp(variable_new_flipped4, lon_new, lat_new, x2, y2, order=1)


#-----------------------------TAS EXTRACTION--------------------------------------
#EXTRACT NETCDF FILE 4
fileobj4 = Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "TTZ_during_event_minus_climatology.nc"))
variable4=fileobj4.variables["TTZ"][:,:]
lat4=fileobj4.variables["LAT"][:,:]
lon4=fileobj4.variables["LON"][:,:]
#TAKE LON LAT FOR PLOT
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_ANNUAL", "RF", "annual_RF_MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#EXTRACT NETCDF FILE 1
fileobj = Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "TTZ_during_event_minus_climatology.nc"))
variable=fileobj.variables["TTZ"][:,:]
lat=fileobj.variables["LAT"][:,:]
lon=fileobj.variables["LON"][:,:]
#TAKE LON LAT FOR PLOT
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_ANNUAL", "RF", "annual_RF_MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#------------------------------------------------------------------------------------------------------------#

#SPECIFY THE GRID PLOTS

fig =  plt.figure(figsize=(22,22))
spec2 = gridspec.GridSpec(ncols=2, nrows=2, width_ratios=[100,100], height_ratios=[150,150])
spec2.update(wspace=-0.50, hspace=0.10)
#figure=fig,

#Normalize the bar values
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)
    def __call__(self, value, clip=None):
		# I'm ignoring masked values and all kinds of edge cases to make a
		# simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))

#PLOT BASEMAP 1

ax = fig.add_subplot(spec2[0, 0])
ax.text(0.99, 0.05, '(a)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=18)

m = Basemap(projection='stere',lon_0=-45,lat_0=90.,lat_ts=60,llcrnrlat=55,urcrnrlat=78,llcrnrlon=-65,urcrnrlon=44, ax=ax)

X, Y = m(x2,y2)

parallels = np.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

#AVERAGE POSITION OF THE CYCLONE
x,y = m(-57.8,64.3)
m.plot(x,y,markersize=16,linestyle='none', marker="*",c="white",markeredgecolor="black", label="Cyclone centre")
m.plot(0,0,markersize=False, linestyle="solid", linewidth="2", marker="*",c="white", label="MSLP")
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),loc="lower left",ncol=2,facecolor='#ceb301',fontsize=14)
           
#Plot MSLP----------------------------------------------------------------------

cs = m.contour(X,Y,data_final22/100, range(990, 1050, 2),colors = "white")
labels30= plt.clabel(cs, inline=True, fmt='%1.0f', fontsize=14, colors='white')
for label in labels30:
  label.set_fontweight('bold')


#PLOT GEOPOTENTIAL CONTOURF AT 500 hPa------------------------------------------
cs = m.contourf(X,Y,data_final4, levels = np.arange(5210,5750,15), cmap='gist_rainbow_r' ,extend='both')

#SITE A (W68.60)
x6,y6 = m(-50.32,68.60)
m.plot(x6,y6,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black",label = "Sites studied")
ax.text(x6 * (1.08), y6 * (0.92), "A", fontsize=20, fontweight= "bold",color = "yellow",path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("500 mb Geopotential Height (m) Composite Mean", rotation=0,labelpad=-60,fontsize=14,color="black")

#INSERT ARROW LINE--------------------------------------------------------------
# Starting and ending points for the curved arrow (longitude, latitude)
start_lon, start_lat = 60, -55
end_lon, end_lat = 68, -50

# Curvature control parameters (adjust as needed)
curve_factor = 150  # Higher values create sharper curves
num_steps = 50  # Number of steps for smoother curves

lons = np.linspace(start_lon, end_lon, num_steps + 2)
lats = np.linspace(start_lat, end_lat, num_steps + 2)

# Apply curvature by adding a sinusoidal offset to the latitudes
curved_lats = lats + curve_factor * np.sin(np.linspace(0, 2*np.pi, num_steps + 2))

## Convert longitude and latitude coordinates to map projection coordinates
x12, y12 = m(curved_lats,lons)

arrow = patches.FancyArrowPatch((x12[0], y12[0]), (x12[-1], y12[-1]),mutation_scale=25,connectionstyle="arc3,rad=.3", color='white',arrowstyle='simple', linewidth=0.5,label='Flow')

ax.add_patch(arrow)
ax.set_title("5-11 September 2013",fontsize=15)
plt.subplots_adjust(wspace=0, hspace=0)


#PLOT BASEMAP 2

ax2 = fig.add_subplot(spec2[0, 1])
ax2.text(0.99, 0.05, '(b)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax2.transAxes,
        color='black', fontsize=18)

m = Basemap(projection='stere',lon_0=-45,lat_0=90.,lat_ts=60,llcrnrlat=55,urcrnrlat=78,llcrnrlon=-65,urcrnrlon=44, ax=ax2)


parallels = np.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

#AVERAGE POSITION OF THE CYCLONE
x,y = m(-54,59.2)
m.plot(x,y,markersize=16,linestyle='none', marker="*",c="white",markeredgecolor="black", label="Cyclone centre")
m.plot(0,0,markersize=False, linestyle="solid", linewidth="2", marker="*",c="white", label="MSLP")
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),loc="lower left",ncol=2,facecolor='#ceb301',fontsize=14)


#Plot MSLP----------------------------------------------------------------------

cs = m.contour(X,Y,data_final56/100, range(990, 1050, 2),colors = "white")
labels55= plt.clabel(cs, inline=True, fmt='%1.0f', fontsize=14, colors='white')
for label in labels55:
  label.set_fontweight('bold')


#PLOT GEOPOTENTIAL CONTOURF AT 500 hPa------------------------------------------
cs = m.contourf(X,Y,data_final, levels = np.arange(5210,5750,15), cmap='gist_rainbow_r' ,extend='both')

#SITE B (W64.25N)
x2,y2 = m(-50.17,64.46)
m.plot(x2,y2,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black")
ax2.text(x2 * (1.08), y2 * (1.05) , "B", fontsize=20, fontweight= "bold", color = "yellow",path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("500 mb Geopotential Height (m) Composite Mean", rotation=0,labelpad=-60,fontsize=14,color="black")

#INSERT ARROW LINE--------------------------------------------------------------
# Starting and ending points for the curved arrow (longitude, latitude)
start_lon2, start_lat2 = 59, -47.5
end_lon2, end_lat2 = 64, -50

# Curvature control parameters (adjust as needed)
curve_factor = 150  # Higher values create sharper curves
num_steps = 50  # Number of steps for smoother curves

lons22 = np.linspace(start_lon2, end_lon2, num_steps + 2)
lats22 = np.linspace(start_lat2, end_lat2, num_steps + 2)

# Apply curvature by adding a sinusoidal offset to the latitudes
curved_lats2 = lats22 + curve_factor * np.sin(np.linspace(0, 2*np.pi, num_steps + 2))

## Convert longitude and latitude coordinates to map projection coordinates
x66, y66 = m(curved_lats2,lons22)

arrow2 = patches.FancyArrowPatch((x66[0], y66[0]), (x66[-1], y66[-1]),mutation_scale=25,connectionstyle="arc3,rad=.1", color='white',arrowstyle='simple', linewidth=0.5,label='Flow')

ax2.add_patch(arrow2)

ax2.set_title("28 August-6 September 2015",fontsize=15)

#PLOT BASEMAP 3

ax3 = fig.add_subplot(spec2[1, 0])
ax3.text(0.99, 0.05, '(c)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax3.transAxes,
        color='black', fontsize=18)

m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = np.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

ny2 = variable4.shape[0]; nx2 = variable4.shape[1]
lons2, lats2 = m.makegrid(nx2, ny2)
x2, y2 = m(lons2, lats2)

cs = m.contourf(lons2,lats2,variable4,norm=MidpointNormalize(midpoint=0,vmin=-8,vmax=10),levels=[-8,-7.5,-7,-6.5,-6,-5.5, -5. , -4.5, -4. , -3.5, -3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,  5.5,6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5, 10.],cmap="bwr",latlon=True, zorder=1,alpha=1)

#SITE A (W68.60)
x6,y6 = m(-50.32,68.60)
m.plot(x6,y6,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black",label = "Sites studied")
ax3.text(x6 * (1.16), y6 * (0.92), "A", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("TTZ anomaly (C°)", rotation=0,labelpad=-60,fontsize=14,color="black")

ax3.set_title("5-11 September 2013",fontsize=15)
plt.subplots_adjust(wspace=0, hspace=0)

#PLOT BASEMAP 4

ax4 = fig.add_subplot(spec2[1, 1])
ax4.text(0.99, 0.05, '(d)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax4.transAxes,
        color='black', fontsize=18)
m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = np.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = np.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

ny = variable.shape[0]; nx = variable.shape[1]
lons, lats = m.makegrid(nx, ny)
x, y = m(lons, lats)

cs = m.contourf(lons,lats,variable,norm=MidpointNormalize(midpoint=0,vmin=-8,vmax=10),levels=[-8,-7.5,-7,-6.5,-6,-5.5, -5. , -4.5, -4. , -3.5, -3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,  5.5,6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5, 10.],cmap="bwr",latlon=True, zorder=1,alpha=1)


#SITE B (W64.25N)
x2,y2 = m(-50.17,64.46)
m.plot(x2,y2,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black")
ax4.text(x2 * (1.18), y2 * (1.05) , "B", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("TTZ anomaly (C°)", rotation=0,labelpad=-60,fontsize=14,color="black")

ax4.set_title("28 August-6 September 2015",fontsize=15)

#save the plot into a figure
plt.savefig(os.path.join(ROOT, "..", "Data", "OUTPUT", "FIGURES", "Gpt_tas_anomaly_Figure_S1.png"), dpi=300, bbox_inches="tight")

# Show the figure on screen
plt.show()