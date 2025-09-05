# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:50:11 2021

@author: lucam
"""
import os
import sys
import numpy as n
from netCDF4 import Dataset
import matplotlib.patheffects as pe
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors

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

#------------------CLOUD COVER DATA ETRACTION------------------------
#EXTRACT NETCDF FILE 1
fileobj=Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "CM_during_event_28aug_6sep.nc"))
variable=fileobj.variables["TTZ"][:,:]
variable_100 = variable*100
lat=fileobj.variables["LAT"][:,:]
lon=fileobj.variables["LON"][:,:]
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#EXTRACT NETCDF FILE 4
fileobj4=Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "CM_during_event_5sep_11sep.nc"))
variable4=fileobj4.variables["TTZ"][:,:]
variable4_100 = variable4*100
lat4=fileobj4.variables["LAT"][:,:]
lon4=fileobj4.variables["LON"][:,:]
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#---------------------------RAINFALL DATA EXTRACTION---------------------------------------
#EXTRACT NETCDF FILE 1
fileobj6=Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_B", "Total_rainfall_during_event_28aug_6sep.nc"))
xvariable=fileobj6.variables["RF"][:,:]
xvariable_1=xvariable/10
xlat=fileobj6.variables["LAT"][:,:]
xlon=fileobj6.variables["LON"][:,:]
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#EXTRACT NETCDF FILE 4
fileobj7=Dataset(os.path.join(ROOT, "..", "Data", "PROCESSED", "METEOROLOGICAL_ANALYSIS", "SITE_A", "Total_rainfall_during_event.nc"))
xvariable4=fileobj7.variables["RF"][:,:]
xvariable_4=xvariable4/7
xlat4=fileobj7.variables["LAT"][:,:]
xlon4=fileobj7.variables["LON"][:,:]
fileobj5=Dataset(os.path.join(ROOT, "..", "Data", "RAW", "MAR_1985_2015", "MARv3.9.2_NCEP1-20km_2015.nc"))
lat5=fileobj5.variables["LAT"][:,:]
lon5=fileobj5.variables["LON"][:,:]

#---------------------------------------------------------------------------------

#SPECIFY THE GRID PLOTS

fig =  plt.figure(figsize=(22,22))
spec2 = gridspec.GridSpec(ncols=2, nrows=2, width_ratios=[100,100], height_ratios=[150,150])
spec2.update(wspace=-0.50, hspace=0.10)
#figure=fig,

#Normalize the bar values - I'm ignoring masked values and all kinds of edge cases to make a simple example...
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)
    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return n.ma.masked_array(n.interp(value, x, y), n.isnan(value))

#PLOT BASEMAP 1

ax = fig.add_subplot(spec2[0, 0])
ax.text(0.99, 0.05, '(a)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=18)
m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = n.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = n.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

ny2 = variable4.shape[0]; nx2 = variable4.shape[1]
lons2, lats2 = m.makegrid(nx2, ny2)
x2, y2 = m(lons2, lats2)

cs = m.contourf(lons2,lats2,variable4_100,levels=[0,10,20,30,40,50,60,70,80,90,100],cmap="Greys",latlon=True, zorder=1,alpha=1)

#SITE E (W68.60)
x6,y6 = m(-50.32,68.60)
m.plot(x6,y6,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black",label = "Sites studied")
ax.text(x6 * (1.16), y6 * (0.92), "A", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])
cbar = m.colorbar(cs,location='bottom',pad="9%")

cbar.set_label("% of mean daily cloud cover", rotation=0,labelpad=-60,fontsize=14,color="black")

ax.set_title("5-11 September 2013",fontsize=15)
plt.subplots_adjust(wspace=0, hspace=0)

#PLOT BASEMAP 2

ax = fig.add_subplot(spec2[0, 1])
ax.text(0.99, 0.05, '(b)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=18)
m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = n.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = n.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

m.shadedrelief()
m.drawcoastlines()

ny = variable.shape[0]; nx = variable.shape[1]
lons, lats = m.makegrid(nx, ny)
x, y = m(lons, lats)

cs = m.contourf(lons,lats,variable_100,levels=[0,10,20,30,40,50,60,70,80,90,100],cmap="Greys",latlon=True, zorder=1,alpha=1)

#SITE B (W64.25N)
x2,y2 = m(-50.17,64.46)
m.plot(x2,y2,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black")
ax.text(x2 * (1.18), y2 * (1.05) , "B", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("% of mean daily cloud cover", rotation=0,labelpad=-60,fontsize=14,color="black")

ax.set_title("28 August-6 September 2015",fontsize=15)

#PLOT BASEMAP 3

ax = fig.add_subplot(spec2[1, 0])
ax.text(0.99, 0.05, '(c)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=18)
m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = n.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = n.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

#m.shadedrelief()
m.drawcoastlines()

ny2 = variable4.shape[0]; nx2 = variable4.shape[1]
lons2, lats2 = m.makegrid(nx2, ny2)
x2, y2 = m(lons2, lats2)

cs = m.contourf(lons2,lats2,xvariable_4,norm=MidpointNormalize(midpoint=4,vmin=2,vmax=32),levels=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32],cmap="Blues",latlon=True, zorder=1,alpha=1)

#SITE A (W68.60)
x6,y6 = m(-50.32,68.60)
m.plot(x6,y6,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black",label = "Sites studied")
ax.text(x6 * (1.16), y6 * (0.92), "A", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("Rainfall (mm/24 h)", rotation=0,labelpad=-60,fontsize=14,color="black")

ax.set_title("5-11 September 2013",fontsize=15)
plt.subplots_adjust(wspace=0, hspace=0)

#PLOT BASEMAP 4

ax = fig.add_subplot(spec2[1, 1])
ax.text(0.99, 0.05, '(d)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=18)
m = Basemap(projection='stere',llcrnrlat=lat5[0,0],urcrnrlat=lat5[134,72],llcrnrlon=lon5[0,0],urcrnrlon=lon5[134,72],lon_0=-40,lat_0=70,resolution='l')

parallels = n.arange(0.,90,5.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

meridians = n.arange(-70.,0.,5.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

#m.shadedrelief()
m.drawcoastlines()

ny = xvariable.shape[0]; nx = xvariable.shape[1]
lons, lats = m.makegrid(nx, ny)
x, y = m(lons, lats)

cs = m.contourf(lons,lats,xvariable_1,norm=MidpointNormalize(midpoint=4,vmin=2,vmax=32),levels=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32],cmap="Blues",latlon=True, zorder=1,alpha=1)

#SITE B (W64.25N)
x2,y2 = m(-50.17,64.46)
m.plot(x2,y2,markersize=28, linestyle='none', marker="*",c="yellow",markeredgecolor="black")
ax.text(x2 * (1.18), y2 * (1.05) , "B", fontsize=20, fontweight= "bold", color = "yellow", path_effects=[pe.withStroke(linewidth=4, foreground="black")])

cbar = m.colorbar(cs,location='bottom',pad="9%")
cbar.set_label("Rainfall (mm/24 h)", rotation=0,labelpad=-60,fontsize=14,color="black")

ax.set_title("28 August-6 September 2015",fontsize=15)

#save the plot into a figure
plt.savefig(os.path.join(ROOT, "..", "Data", "OUTPUT", "FIGURES", "Cloud_rainfall_Figure_S2.png"), dpi=300, bbox_inches="tight")

# Show the figure on screen
plt.show()
