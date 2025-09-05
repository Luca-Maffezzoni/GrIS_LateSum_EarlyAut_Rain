# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:36:34 2023

@author: lmaff
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pylab as pl
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(ROOT, "..", "data", "OUTPUT", "FIGURES")

#----------------------------------------------READ DATA FROM SITE A---------------------------------------

#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 1
#READ DATAFRAMES DAYS
days_txt = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "Days.txt"))
days = days_txt["Days"][:]
#MULTY YEAR FLOW LINE 1 VELOCITY
multy_year_velocity_flow_line_1 = 88.39
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
flow_line_1 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_mean_1.txt"), delimiter=";")
flow_line_1_day = flow_line_1["Day"][:]
flow_line_1_values = flow_line_1["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
error_flow_line_1 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_error_1.txt"), delimiter=";")
error_flow_line_1_day = error_flow_line_1["Day"][:]
error_flow_line_1_values = error_flow_line_1["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 2
#MULTY YEAR FLOW LINE 2 VELOCITY
multy_year_velocity_flow_line_2 = 158.76
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
flow_line_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_mean_2.txt"), delimiter=";")
flow_line_2_day = flow_line_2["Day"][:]
flow_line_2_values = flow_line_2["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
error_flow_line_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_error_2.txt"), delimiter=";")
error_flow_line_2_values = error_flow_line_2["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 3
#MULTY YEAR FLOW LINE 3 VELOCITY
multy_year_velocity_flow_line_3 = 82.32
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
flow_line_3 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_mean_3.txt"), delimiter=";")
flow_line_3_day = flow_line_3["Day"][:]
flow_line_3_values = flow_line_3["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
error_flow_line_3 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_error_3.txt"), delimiter=";")
error_flow_line_3_values = error_flow_line_3["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 4
#MULTY YEAR FLOW LINE 4 VELOCITY
multy_year_velocity_flow_line_4 = 74.09
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
flow_line_4 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_mean_4.txt"), delimiter=";")
flow_line_4_day = flow_line_4["Day"][:]
flow_line_4_values = flow_line_4["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
error_flow_line_4 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_error_4.txt"), delimiter=";")
error_flow_line_4_values = error_flow_line_4["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 5
#MULTY YEAR FLOW LINE 5 VELOCITY
multy_year_velocity_flow_line_5 = 95.03
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
flow_line_5 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_mean_5.txt"), delimiter=";")
flow_line_5_day = flow_line_5["Day"][:]
flow_line_5_values = flow_line_5["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
error_flow_line_5 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_A", "flow_line_error_5.txt"), delimiter=";")
error_flow_line_5_values = error_flow_line_5["Values"][:]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#READ DATA OF MELT,RUNOFF,RAIN AND TEMPERATURE
#READ DATAFRAMES MELTWATER
meltwater = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_A", "daily_meltwater_2013.txt"), delimiter=";")
#READ DATAFRAMES RUNOFF
runoff = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_A", "daily_runoff_2013.txt"), delimiter=";")
#READ DATAFRAMES RAINFALL
rainfall = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_A", "daily_rainfall_2013.txt"), delimiter=";")
#READ DATAFRAMES TEMPERATURE
temperature = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_A", "daily_temperature_2013.txt"), delimiter=";")
#EXTRACT VALUES FROM DATAFRAMES MELTWATER
meltwater_days = meltwater["Days"][:]
meltwater_values = meltwater["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES RUNOFF
runoff_days = runoff["Days"][:]
runoff_values = runoff["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES RAINFALL
rainfall_days = rainfall["Days"][:]
rainfall_values = rainfall["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES TEMPERATURE
temperature_days = temperature["Days"][:]
temperature_values = temperature["Values"][:]



#---------------------------------------------READ DATA FROM SITE B--------------------------------------------------



#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 1
#READ DATAFRAMES DAYS
xdays_txt = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "Days.txt"))
xdays = xdays_txt["Days"][:]
#MULTY YEAR FLOW LINE 1 VELOCITY
xmulty_year_velocity_flow_line_1 = 592.76
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
xflow_line_1 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_mean_1.txt"), delimiter=";")
xflow_line_1_day = xflow_line_1["Day"][:]
xflow_line_1_values = xflow_line_1["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
xerror_flow_line_1 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_error_1.txt"), delimiter=";")
xerror_flow_line_1_day = xerror_flow_line_1["Day"][:]
xerror_flow_line_1_values = xerror_flow_line_1["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 2
#MULTY YEAR FLOW LINE 2 VELOCITY
xmulty_year_velocity_flow_line_2 = 1265.28
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
xflow_line_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_mean_2.txt"), delimiter=";")
xflow_line_2_day = xflow_line_2["Day"][:]
xflow_line_2_values = xflow_line_2["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
xerror_flow_line_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_error_2.txt"), delimiter=";")
xerror_flow_line_2_values = xerror_flow_line_2["Values"][:]

#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 3
#MULTY YEAR FLOW LINE 3 VELOCITY
xmulty_year_velocity_flow_line_3 = 1624.60
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
xflow_line_3 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_mean_3.txt"), delimiter=";")
xflow_line_3_day = xflow_line_3["Day"][:]
xflow_line_3_values = xflow_line_3["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
xerror_flow_line_3 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_error_3.txt"), delimiter=";")
#error_flow_line_1_day = error_flow_line_1["Day"][:]
xerror_flow_line_3_values = xerror_flow_line_3["Values"][:]


#READ DATA OF ICE VELOCITY AND ERROR OF FLOW LINE 4
#MULTY YEAR FLOW LINE 4 VELOCITY
xmulty_year_velocity_flow_line_4 = 122.91
#FLOW LINE CENTRAL DAY AND VELOCITY FOR EACH IMAGE PAIR
xflow_line_4 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_mean_4.txt"), delimiter=";")
xflow_line_4_day = xflow_line_4["Day"][:]
xflow_line_4_values = xflow_line_4["Values"][:]
#FLOW LINE ERROR FOR EACH IMAGE PAIR
xerror_flow_line_4 = pd.read_csv(os.path.join(ROOT, "..", "Data", "PROCESSED", "AVERAGE_VELOCITY_FLOWLINES_SITE_B", "flow_line_error_4.txt"), delimiter=";")
xerror_flow_line_4_values = xerror_flow_line_4["Values"][:]

#READ DATA OF MELT,RUNOFF,RAIN AND TEMPERATURE
#READ DATAFRAMES MELTWATER
xmeltwater = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_B", "daily_meltwater_2015.txt"), delimiter=";")
#READ DATAFRAMES RUNOFF
xrunoff = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_B", "daily_runoff_2015.txt"), delimiter=";")
#READ DATAFRAMES RAINFALL
xrainfall = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_B", "daily_rainfall_2015.txt"), delimiter=";")
#READ DATAFRAMES TEMPERATURE
xtemperature = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "MET_GLACIO_PARAM", "SITE_B", "daily_temperature_2015.txt"), delimiter=";")
#EXTRACT VALUES FROM DATAFRAMES MELTWATER
xmeltwater_days = xmeltwater["Days"][:]
xmeltwater_values = xmeltwater["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES RUNOFF
xrunoff_days = xrunoff["Days"][:]
xrunoff_values = xrunoff["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES RAINFALL
xrainfall_days = xrainfall["Days"][:]
xrainfall_values = xrainfall["Values"][:]
#EXTRACT VALUES FROM DATAFRAMES TEMPERATURE
xtemperature_days = xtemperature["Days"][:]
xtemperature_values = xtemperature["Values"][:]


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#DEFINE THE PLOT SIZE, NUMBER OF COLUMNS/ROWS AND DISTANCE BETWEEN PLOTS
fig =  plt.figure(figsize=(13,13))
#fig =  plt.figure(figsize=(21,22))
#CAMBIATO COLUMNS E ROW PER PAPER IN 3 E 5
spec2 = gridspec.GridSpec(ncols=3, nrows=6,hspace=0, width_ratios=[0.3,5,5], height_ratios=[3.5,3.5,3.5,3.5,3.5,8])
spec2.update(wspace=0.04, hspace=0.06)

#DEFINE NESTED GRIDSPEC IN GRIDSPEC IN ORDER TO HAVE 3 SUBPLOTS NESTED IN EACH OF SIX SUBLOPTS DEFINED BEFORE
gs00 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[0,1],hspace=0)
gs01 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[1,1],hspace=0)
gs02 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[2,1],hspace=0)
gs03 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[3,1],hspace=0)
gs04 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[4,1],hspace=0)
gs05 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=spec2[5,1],hspace=0)

gs06 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[0,2],hspace=0)
gs07 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[1,2],hspace=0)
gs08 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[2,2],hspace=0)
gs09 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[3,2],hspace=0)
gs10 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[4,2],hspace=0)
gs11 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=spec2[5,2],hspace=0)

gs_vertical_left = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[:,0])

#----------------------------------------- PLOT ICE VELOCITIES SITE A --------------------------------------------------------------------------------------------------------------------
 
#number of samples
N = 153
ind = np.arange(N)

#PLOT ICE VELOCITY FLOW LINE 1
#Define the higher nested subplot with labels 
ax1 = plt.subplot(gs00[0])
ax1.set_ylim(25,285)
ax1.set_yticks([50,100,150,200,250])
ax1.set_yticklabels([50,100,150,200,250], fontsize=12)
ax1.text(ind[73], 257, "A1",fontweight='bold', fontsize=12)
ax1.text(ind[34], 225,"Alangordliup Glacier (Marine)",fontweight='bold', fontsize=12)
#ax1.set_ylabel('Ice velocity (m/year)',fontsize=25)
ax1.axhline(y=multy_year_velocity_flow_line_1, color='r', linestyle='--',label = "Multi-years-velocity")
ax1.plot([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_1_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_1_values,yerr=error_flow_line_1_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_1_values,xerr=[5,5,5,5,5,5,11,11,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax1.legend(loc= "upper left",fontsize=20)

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]

ax1.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax1.set_xticks(ind,minor="True")
ax1.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax1.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax1.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax1.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 2
ax2 = plt.subplot(gs01[0])
ax2.set_ylim(90,420)
ax2.set_yticks([150,200,250,300,350])
ax2.set_yticklabels([150,200,250,300,350], fontsize=12)
ax2.text(ind[73], 370, "A2",fontweight='bold', fontsize=12)
ax2.text(ind[36], 328,"Sarqardliup Glacier (Marine)",fontweight='bold', fontsize=12)
ax2.axhline(y=multy_year_velocity_flow_line_2, color='r', linestyle='--',label = "Multi-years-velocity")
ax2.plot([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_2_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_2_values,yerr=error_flow_line_2_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_2_values,xerr=[5,5,5,5,5,5,11,11,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax2.legend(loc= "lower left")

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]

ax2.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax2.set_xticks(ind,minor="True")
ax2.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax2.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax2.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax2.get_xticklabels(), visible=False)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PLOT ICE VELOCITY FLOW LINE 3
#Define the higher nested subplot with labels 
ax3 = plt.subplot(gs02[0])
ax3.set_ylim(25,280)
ax3.set_yticks([50,100,150,200,250])
ax3.set_yticklabels([50,100,150,200,250], fontsize=12)
ax3.text(ind[73], 250, "A3",fontweight='bold', fontsize=12)
ax3.text(ind[30], 218,"Quingap Iluliarera Glacier (Land)",fontweight='bold', fontsize=12)
#ax1.set_ylabel('Ice velocity (m/year)',fontweight="bold",fontsize=19)
ax3.axhline(y=multy_year_velocity_flow_line_3, color='r', linestyle='--',label = "Multi-years-velocity")
ax3.plot([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_3_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_3_values,yerr=error_flow_line_3_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_3_values,xerr=[5,5,5,5,5,5,11,11,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax3.legend(loc= "lower left",fontsize=24)

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax3.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax3.set_xticks(ind,minor="True")
ax3.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax3.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax3.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax3.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 4
ax4 = plt.subplot(gs03[0])
ax4.set_ylim(25,280)
ax4.set_yticks([50,100,150,200,250])
ax4.set_yticklabels([50,100,150,200,250], fontsize=12)
ax4.text(ind[73], 250, "A4",fontweight='bold', fontsize=12)
ax4.text(ind[30], 218,"Quingap Iluliarera Glacier (Land)",fontweight='bold', fontsize=12)
#ax2.set_ylabel('Ice velocity (m/year)',fontweight="bold",fontsize=19)
ax4.axhline(y=multy_year_velocity_flow_line_4, color='r', linestyle='--',label = "Multi-years-velocity")
ax4.plot([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_4_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_4_values,yerr=error_flow_line_4_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_4_values,xerr=[5,5,5,5,5,5,11,11,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax2.legend(loc= "lower left")

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax4.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax4.set_xticks(ind,minor="True")
ax4.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax4.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax4.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax4.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 5
ax5 = plt.subplot(gs04[0])
ax5.set_ylim(25,320)
ax5.set_yticks([50,100,150,200,250])
ax5.set_yticklabels([50,100,150,200,250], fontsize=12)
ax5.text(ind[73], 278, "A5",fontweight='bold', fontsize=12)
ax5.text(ind[37], 239,"Lliulialik Glacier (Land)",fontweight='bold', fontsize=12)
#ax3.set_ylabel('Ice velocity (m/year)',fontweight="bold",fontsize=19)
ax5.axhline(y=multy_year_velocity_flow_line_5, color='r', linestyle='--',label = "Multi-years-velocity")
ax5.plot([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_5_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_5_values,yerr=error_flow_line_5_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[8],ind[19],ind[30],ind[41],ind[52],ind[63],ind[79],ind[101],ind[118],ind[129],ind[140]],flow_line_5_values,xerr=[5,5,5,5,5,5,11,11,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax3.legend(loc= "lower left")

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax5.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax5.set_xticks(ind,minor="True")
ax5.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax5.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax5.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax5.get_xticklabels(), visible=False)



#----------------------------------------- PLOT ICE VELOCITIES SITE B --------------------------------------------------------------------------------------------------------------------


#PLOT ICE VELOCITY FLOW LINE 1
#Define the higher nested subplot with labels 
ax9 = plt.subplot(gs07[0])
ax9.yaxis.tick_right()
ax9.set_ylim(390,850)
ax9.set_yticks([400,500,600,700,800])
ax9.set_yticklabels([400,500,600,700,800], fontsize=12)
ax9.text(ind[73], 700,"B1",fontweight='bold', fontsize=12)
ax9.text(ind[35], 775,"Akugdlerssup Glacier (Marine)",fontweight='bold', fontsize=12)
# ax1.set_ylabel('Ice velocity (m/year)',fontsize=25)
ax9.axhline(y=xmulty_year_velocity_flow_line_1, color='r', linestyle='--',label = "Multi-years-velocity")
ax9.plot([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_1_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_1_values,yerr=xerror_flow_line_1_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_1_values,xerr=[5,11,5,11,5,5,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax7 = plt.subplot(gs06[0])
#plt.subplot(gs07[0]).legend(loc= "upper center",fontsize=13)
# Add a legend
pos = ax9.get_position()
ax9.set_position([pos.x0, pos.y0, pos.width, pos.height * 1])
ax9.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, 2.10),
    fontsize = 13,
)

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax9.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax9.set_xticks(ind,minor="True")
ax9.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax9.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax9.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax9.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 2
ax10 = plt.subplot(gs08[0])
ax10.yaxis.tick_right()
ax10.set_ylim(950,1900)
ax10.set_yticks([1000,1200,1400,1600,1800])
ax10.set_yticklabels([1000,1200,1400,1600,1800], fontsize=12)
ax10.text(ind[73], 1620, "B2",fontweight='bold', fontsize=12)
ax10.text(ind[34], 1770, "Kangiata Nunata Glacier (Marine)",fontweight='bold', fontsize=12)
ax10.axhline(y=xmulty_year_velocity_flow_line_2, color='r', linestyle='--',label = "Multi-years-velocity")
ax10.plot([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_2_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_2_values,yerr=xerror_flow_line_2_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_2_values,xerr=[5,11,5,11,5,5,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax2.legend(loc= "lower left")

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax10.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax10.set_xticks(ind,minor="True")
ax10.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax10.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax10.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax10.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 3
#Define the higher nested subplot with labels 
ax11 = plt.subplot(gs09[0])
ax11.yaxis.tick_right()
ax11.set_ylim(1380,2000)
ax11.set_yticks([1450,1600,1750,1900])
ax11.set_yticklabels([1450,1600,1750,1900], fontsize=12)
ax11.text(ind[73], 1810,"B3",fontweight='bold', fontsize=12)
ax11.text(ind[34], 1900,"Kangiata Nunata Glacier (Marine)",fontweight='bold', fontsize=12)
#ax1.set_ylabel('Ice velocity (m/year)',fontsize=25)
ax11.axhline(y=xmulty_year_velocity_flow_line_3, color='r', linestyle='--',label = "Multi-years-velocity")
ax11.plot([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_3_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_3_values,yerr=xerror_flow_line_3_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_3_values,xerr=[5,11,5,11,5,5,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax11.legend(loc= "upper left",fontsize=20)

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax11.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax11.set_xticks(ind,minor="True")
ax11.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax11.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax11.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax11.get_xticklabels(), visible=False)


#PLOT ICE VELOCITY FLOW LINE 4
ax12 = plt.subplot(gs10[0])
ax12.yaxis.tick_right()
ax12.set_ylim(100,270)
ax12.set_yticks([120,160,200,240])
ax12.set_yticklabels([120,160,200,240], fontsize=12)
ax12.text(ind[74], 220, "B4",fontweight='bold', fontsize=12)
ax12.text(ind[34], 248, "Kangaussarssup Glacier (Land)",fontweight='bold', fontsize=12)
ax12.axhline(y=xmulty_year_velocity_flow_line_4, color='r', linestyle='--',label = "Multi-years-velocity")
ax12.plot([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_4_values,linestyle = "None",marker="o",markersize=4.5, color="red", markeredgewidth=1.3, markerfacecolor="black",zorder=2,label = "Average velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_4_values,yerr=xerror_flow_line_4_values,ecolor='orange',capsize=3,capthick=1,linestyle = "None",zorder=1,label = "Error associated with velocity")
pl.errorbar([ind[16],ind[32],ind[49],ind[65],ind[81],ind[92],ind[104],ind[116],ind[126]],xflow_line_4_values,xerr=[5,11,5,11,5,5,5,5,5],ecolor='black',capsize=3,capthick=1,linestyle = "None",zorder=0,label = "Time span of image pairs")
#SET LEGEND
#ax2.legend(loc= "lower left")

major=[days[0],days[14],days[30],days[45],days[60],days[75],days[91],days[106],days[122],days[137],days[152]]
#Set label for major and minor ticks
ax12.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax12.set_xticks(ind,minor="True")
ax12.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10)
ax12.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax12.set_xticklabels(major)
plt.setp(xtickNames)
plt.setp(ax12.get_xticklabels(), visible=False)



#---------------- PLOT MELT,RUNOFF,RAINFALL AND TEMPERATURE SITE A--------------------------------------------------------------------


##PLOT 2013 MELT,RUNOFF,RAIN AND TEMPERATURE
##Define the lower nested subplot with labels
ax_runoff_1 = plt.subplot(gs05[2])
ax_runoff_1.plot(ind[:], runoff_values, drawstyle='steps-mid',color="blue",linestyle='--', label = "Runoff")
ax_runoff_1.set_ylabel("mm w.e",labelpad = 8,fontsize = 14)
##Define the second sublplot nested 
ax_rainfall_1 = plt.subplot(gs05[1])
##fill the step-mid plot written afterwards
ax_rainfall_1.fill_between(days, rainfall_values,step="mid", alpha=0.4,color="black")
ax_rainfall_1.plot(ind[:], rainfall_values,drawstyle='steps-mid',color="black",linestyle='-', label = "Rainfall")
ax_rainfall_1.set_ylabel("mm \nrainfall",labelpad =8,fontsize = 14)
##In the same subplot work on the opposite y axis
ax = ax_rainfall_1.twinx()
ax.plot(ind,meltwater_values, drawstyle='steps-mid',color="red",linestyle='--', label = "Meltwater")
#ax.set_ylabel("mm w.e", labelpad = 10,fontsize = 14)
##define the last subplot
ax8 = plt.subplot(gs05[0], sharex = ax_rainfall_1)
ax8.plot(temperature_days,temperature_values,color="#ff028d",label = "Temperature")
ax8.axhline(y=0, color='#ff028d', linestyle='--')
####Ad label temperature creating ax.twinx of ax8 subplot
ax_y_8 = ax8.twinx()
#ax_y_8.set_ylabel("(C°)\nAir temperaure",labelpad=32,fontsize = 12)
##Set tegend in 3 different subplots defined before
#ax_rainfall_1.legend(loc= "upper left",fontsize=12)
ax.legend(loc ="upper right",fontsize=12)
#ax8.legend(loc="lower left")
#ax_runoff_1.legend(loc="upper left",fontsize=12)
#delete ticks on ax8 twinx
ax_y_8.tick_params(axis = "y", right = False)
#
#Define Xtics labels at the lowest plot
major=[days[0]," ",days[30], " ",days[60]," ",days[91]," ",days[122]," ","30 sep"]
#Decide where put or delete tics parameters 
ax_runoff_1.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
ax_runoff_1.set_xticks(ind,minor="True")
ax_runoff_1.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10,rotation = 20)
ax_runoff_1.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = ax_runoff_1.set_xticklabels(major,ha="right")
plt.setp(xtickNames,fontsize=9, )
ax_rainfall_1.set_xticks(ind,minor="True")
ax8.set_xticks(ind,minor="True")
ax_rainfall_1.tick_params(axis= "x", direction = "in")
ax8.tick_params(axis= "x", direction = "in")

##delete ticks on ax8 twinx
ax_y_8.tick_params(axis = "y", right = False)
##put x and y axis at the top and right of the subplot ax8
ax8.xaxis.tick_top()
ax8.yaxis.tick_right()
#Define where mask the subplots borders
ax_rainfall_1.spines['top'].set_visible(False)
ax_rainfall_1.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax8.spines["bottom"].set_visible(False)
ax_y_8.spines["bottom"].set_visible(False)
# 
#Mask ticks labels apart for the last plot 2009
plt.setp(ax_rainfall_1.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax8.get_yticklabels(), visible=False)
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax8.get_xticklabels(), visible=False)
plt.setp(ax_y_8.get_yticklabels(), visible=False)

#Tight layout of the borders
ax_rainfall_1.margins(x=0)
ax8.margins(x=0)
ax_runoff_1.margins(x=0)

#Insert year of study
ax8.text(ind[65], -12, "2013",fontweight='bold', fontsize=14)

#DEFINISCI I MARGINI PER FARLI COMBACIARE TRA GRAFICI
def set_xmargin(ax, left=0.0, right=0.3):
    ax.set_xmargin(0)
    ax.autoscale_view()
    lim = ax.get_xlim()
    delta = np.diff(lim)
    left = lim[0] - delta*left
    right = lim[1] + delta*right
    ax.set_xlim(left,right)

set_xmargin(ax1, left = 0.021, right=0.049)
set_xmargin(ax2, left = 0.021, right=0.049)
set_xmargin(ax3, left = 0.021, right=0.049)
set_xmargin(ax4, left = 0.021, right=0.049)
set_xmargin(ax5, left = 0.021, right=0.049)
set_xmargin(ax_runoff_1, left = 0.00, right=0.0)
set_xmargin(ax_rainfall_1, left = 0.0, right=0.0)
set_xmargin(ax8, left = 0.00, right=0.0)
set_xmargin(ax, left = 0.00, right=0.0)  

#Set y lim and yticks in order to avoid overlapp of ticks
ax_rainfall_1.set_ylim(ymin = 0, ymax = 25)
ax_rainfall_1.set_yticks([5,10,15,20])
ax_rainfall_1.set_yticklabels([5,10,15,20], fontsize=12)  
ax_runoff_1.set_ylim(ymin = 0, ymax = 45)
ax_runoff_1.set_yticks([10,20,30,40])
ax_runoff_1.set_yticklabels([10,20,30,40], fontsize=12)  
ax.set_ylim(ymin = 0, ymax = 55)
ax.set_yticks([])
#ax.set_yticklabels([10,20,30,40,50], fontsize=12)  
ax8.set_ylim(ymin = -25)
ax8.set_yticks([])
#ax8.set_yticklabels([0,-5,-10,-15,-20], fontsize=12)



##---------------- PLOT MELT,RUNOFF,RAINFALL AND TEMPERATURE SITE B--------------------------------------------------------------------


##PLOT 2015 MELT,RUNOFF,RAIN AND TEMPERATURE
##Define the lower nested subplot with labels
xax_runoff_1 = plt.subplot(gs11[2])
xax_runoff_1.plot(ind[:], xrunoff_values, drawstyle='steps-mid',color="blue",linestyle='--', label = "Runoff")
#xax_runoff_1.set_ylabel("mm w.e",labelpad = 8,fontsize = 14)
##Define the second sublplot nested 
xax_rainfall_1 = plt.subplot(gs11[1])
##fill the step-mid plot written afterwards
xax_rainfall_1.fill_between(xdays, xrainfall_values,step="mid", alpha=0.4,color="black")
xax_rainfall_1.plot(ind[:], xrainfall_values,drawstyle='steps-mid',color="black",linestyle='-', label = "Rainfall")
#xax_rainfall_1.set_ylabel("mm",labelpad =8,fontsize = 14)
##In the same subplot work on the opposite y axis
xax = xax_rainfall_1.twinx()
xax.plot(ind,xmeltwater_values, drawstyle='steps-mid',color="red",linestyle='--', label = "Meltwater")
xax.set_ylabel("mm w.e", labelpad = 10,fontsize = 14)
##define the last subplot
xax8 = plt.subplot(gs11[0], sharex = xax_rainfall_1)
xax8.plot(xtemperature_days,xtemperature_values,color="#ff028d",label = "Temperature")
xax8.axhline(y=0, color='#ff028d', linestyle='--')
####Ad label temperature creating ax.twinx of ax8 subplot
xax_y_8 = xax8.twinx()
xax_y_8.set_ylabel("(C°)\nAir temperaure",labelpad=32,fontsize = 12)
##Set tegend in 3 different subplots defined before
xax_rainfall_1.legend(loc= "upper left",fontsize=12)
#xax.legend(loc ="upper right",fontsize=12)
#ax8.legend(loc="lower left")
xax_runoff_1.legend(loc="upper left",fontsize=12)
#delete ticks on ax8 twinx
xax_y_8.tick_params(axis = "y", right = False)
#
#Define Xtics labels at the lowest plot
major=["  1 may"," ",days[30], " ",days[60]," ",days[91]," ",days[122]," ","30 Sep"]
#Decide where put or delete tics parameters
xax_runoff_1.set_xticks([ind[0],ind[14],ind[30],ind[45],ind[60],ind[75],ind[91],ind[106],ind[122],ind[137],ind[152]])
xax_runoff_1.set_xticks(ind,minor="True")
xax_runoff_1.tick_params(axis = 'x', which = 'major', direction = 'in',length = 8,labelsize = 10, rotation = -20)
xax_runoff_1.tick_params(axis = 'x', which = 'minor',direction = 'in',length = 4, labelsize = 0)
xtickNames = xax_runoff_1.set_xticklabels(major,ha="left")
plt.setp(xtickNames,fontsize=9)
xax_rainfall_1.set_xticks(ind,minor="True")
xax8.set_xticks(ind,minor="True")
xax_rainfall_1.tick_params(axis= "x", direction = "in")
xax8.tick_params(axis= "x", direction = "in")

##delete ticks on ax8 twinx
xax_y_8.tick_params(axis = "y", right = False)
##put x and y axis at the top and right of the subplot ax8
xax8.xaxis.tick_top()
xax8.yaxis.tick_right()
#Define where mask the subplots borders
xax_rainfall_1.spines['top'].set_visible(False)
xax_rainfall_1.spines['bottom'].set_visible(False)
xax_rainfall_1.spines['right'].set_visible(False)
xax.spines['top'].set_visible(False)
xax.spines['bottom'].set_visible(False)
xax8.spines["bottom"].set_visible(False)
xax_y_8.spines["bottom"].set_visible(False)
# 
#Mask ticks labels apart for the last plot 2009
plt.setp(xax_rainfall_1.get_xticklabels(), visible=False)
plt.setp(xax_rainfall_1.get_yticklabels(), visible=False)
plt.setp(xax_runoff_1.get_yticklabels(), visible=False)
plt.setp(xax.get_xticklabels(), visible=False)
plt.setp(xax8.get_xticklabels(), visible=False)
plt.setp(xax_y_8.get_yticklabels(), visible=False)

#Tight layout of the borders
xax_rainfall_1.margins(x=0)
xax8.margins(x=0)
xax_runoff_1.margins(x=0)

#Insert year of study
xax8.text(ind[65], -12, "2015",fontweight='bold', fontsize=14)

#DEFINISCI I MARGINI PER FARLI COMBACIARE TRA GRAFICI
def set_xmargin(ax, left=0.0, right=0.3):
    ax.set_xmargin(0)
    ax.autoscale_view()
    lim = ax.get_xlim()
    delta = np.diff(lim)
    left = lim[0] - delta*left
    right = lim[1] + delta*right
    ax.set_xlim(left,right)

set_xmargin(ax9, left = 0.089, right=0.176)
set_xmargin(ax10, left = 0.089, right=0.176)
set_xmargin(ax11, left = 0.089, right=0.176)
set_xmargin(ax12, left = 0.089, right=0.176)
set_xmargin(xax_runoff_1, left = 0.0025, right=0.00)
set_xmargin(xax_rainfall_1, left = 0.0, right=0.0)
set_xmargin(xax8, left = 0.00, right=0.0)
set_xmargin(xax, left = 0.00, right=0.0)  

#Set y lim and yticks in order to avoid overlapp of ticks
xax_rainfall_1.set_ylim(ymin = 0, ymax = 30)
xax_rainfall_1.set_yticks([])
#xax_rainfall_1.set_yticklabels([5,10,15,20], fontsize=12)  
xax_runoff_1.set_ylim(ymin = 0, ymax = 45)
xax_runoff_1.set_yticks([])
#xax_runoff_1.set_yticklabels([10,20,30,40], fontsize=12)  
xax.set_ylim(ymin = 0, ymax = 55)
xax.set_yticks([10,20,30,40,50])
xax.set_yticklabels([10,20,30,40,50], fontsize=12)  
xax8.set_ylim(ymin = -25)
xax8.set_yticks([0,-5,-10,-15,-20])
xax8.set_yticklabels([0,-5,-10,-15,-20], fontsize=12)



#PLOT VERTICAL ICE VELOCITY
ax6 = plt.subplot(gs_vertical_left[0])
ax6.axis('off')
ax6.text(-2.3,0.78,"Velocity(m $yr^{-1})$",rotation = 90, fontsize=22)
 
#--------------------------------------------PLOT GRAY SITE A-----------------------------------------------------------------

#Set grey columns through the entire plot representing the events studied in 2013 
#GREY COLUMN
for ax_gray_2 in (ax1,ax2,ax3,ax4,ax5):
    ax_gray_2.axvspan(ind[126], ind[132], facecolor='grey', alpha=0.3)

for ax_gray_1 in (ax8,ax_runoff_1):
    ax_gray_1.axvspan(ind[126], ind[132], facecolor='grey', alpha=0.3)

for ax_gray_2 in (ax_rainfall_1,):
    ax_gray_2.axvspan(ind[126], ind[132], facecolor='grey', alpha=0.3)
    

#--------------------------------------------PLOT GRAY SITE B------------------------------------------------------------------
#Set grey columns through the entire plot representing the events studied in 2015 
#GREY COLUMN
for xax_gray_2 in (ax9,ax10,ax11,ax12):
    xax_gray_2.axvspan(ind[118], ind[130], facecolor='grey', alpha=0.3)

for xax_gray_1 in (xax8,xax_runoff_1):
    xax_gray_1.axvspan(ind[118], ind[130], facecolor='grey', alpha=0.3)

for xax_gray_2 in (xax_rainfall_1,):
    xax_gray_2.axvspan(ind[118], ind[130], facecolor='grey', alpha=0.3)

#===========================================SAVE THE FIGURE(OPTIONAL)======================================
# SAVE FIGURE AS PNG
# output_path = os.path.join(output_folder, "Figure_2")
# plt.savefig(output_path, dpi=300, bbox_inches="tight")
# plt.close()