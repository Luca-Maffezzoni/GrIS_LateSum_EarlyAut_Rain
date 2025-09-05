# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:03:10 2020

@author: lucam
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
import os

# =========================
# DEFINE ROOT AND PROJECT FOLDERS
# =========================
ROOT = os.path.dirname(os.path.abspath(__file__))  # Root folder where this script is saved

file_txt_data_folder_site_A = os.path.join(ROOT, "..", "data", "PROCESSED", "VELOCITY_ALONG_FLOWLINES_SITE_A")
file_txt_data_folder_site_B = os.path.join(ROOT, "..", "data", "PROCESSED", "VELOCITY_ALONG_FLOWLINES_SITE_B")
output_folder = os.path.join(ROOT, "..", "data", "OUTPUT", "FIGURES")


#---------------------------------------------------READ DATA FROM SITE A---------------------------------------------------

#READ DATAFRAMES ice velocity FLOW LINE 1
ice_velocity_before_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_1_22Aug13_02Sep13.txt"), delimiter=";")
ice_velocity_during_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_1_02Sep13_13Sep13.txt"), delimiter=";")
ice_velocity_after_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_1_13Sep13_24Sep13.txt"), delimiter=";")

#READ DATAFRAMES ice velocity FLOW LINE 2
ice_velocity_before_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_2_22Aug13_02Sep13.txt"), delimiter=";")
ice_velocity_during_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_2_02Sep13_13Sep13.txt"), delimiter=";")
ice_velocity_after_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_2_13Sep13_24Sep13.txt"), delimiter=";")

#READ DATAFRAMES ice velocity FLOW LINE 3
ice_velocity_before_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_3_22Aug13_02Sep13.txt"), delimiter=";")
ice_velocity_during_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_3_02Sep13_13Sep13.txt"), delimiter=";")
ice_velocity_after_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_3_13Sep13_24Sep13.txt"), delimiter=";")

#READ DATAFRAMES ice velocity FLOW LINE 4
ice_velocity_before_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_4_22Aug13_02Sep13.txt"), delimiter=";")
ice_velocity_during_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_4_02Sep13_13Sep13.txt"), delimiter=";")
ice_velocity_after_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_4_13Sep13_24Sep13.txt"), delimiter=";")

#READ DATAFRAMES ice velocity FLOW LINE 5
ice_velocity_before_7 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_5_22Aug13_02Sep13.txt"), delimiter=";")
ice_velocity_during_7 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_5_02Sep13_13Sep13.txt"), delimiter=";")
ice_velocity_after_7 = pd.read_csv(os.path.join(file_txt_data_folder_site_A, "flow_5_13Sep13_24Sep13.txt"), delimiter=";")


#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 1

values_distance_31 = ice_velocity_before_3["Distance"][:]
years_velocity_31 = ice_velocity_before_3["Velocity"][:]
values_distance_32 = ice_velocity_during_3["Distance"][:]
years_velocity_32 = ice_velocity_during_3["Velocity"][:]
values_distance_33 = ice_velocity_after_3["Distance"][:]
years_velocity_33 = ice_velocity_after_3["Velocity"][:]

#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 2

values_distance_43 = ice_velocity_before_4["Distance"][:]
years_velocity_43 = ice_velocity_before_4["Velocity"][:]
values_distance_44 = ice_velocity_during_4["Distance"][:]
years_velocity_44 = ice_velocity_during_4["Velocity"][:]
values_distance_45 = ice_velocity_after_4["Distance"][:]
years_velocity_45 = ice_velocity_after_4["Velocity"][:]

#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 3
 
values_distance_52 = ice_velocity_before_5["Distance"][:]
years_velocity_52 =  ice_velocity_before_5["Velocity"][:] 
values_distance_53 = ice_velocity_during_5["Distance"][:]
years_velocity_53 =  ice_velocity_during_5["Velocity"][:] 
values_distance_54 = ice_velocity_after_5["Distance"][:]
years_velocity_54 =  ice_velocity_after_5["Velocity"][:] 

#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 4

values_distance_61 = ice_velocity_before_6["Distance"][:]
years_velocity_61 =  ice_velocity_before_6["Velocity"][:] 
values_distance_62 = ice_velocity_during_6["Distance"][:]
years_velocity_62 =  ice_velocity_during_6["Velocity"][:] 
values_distance_63 = ice_velocity_after_6["Distance"][:]
years_velocity_63 =  ice_velocity_after_6["Velocity"][:] 

#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 5

values_distance_70 = ice_velocity_before_7["Distance"][:]
years_velocity_70 =  ice_velocity_before_7["Velocity"][:] 
values_distance_71 = ice_velocity_during_7["Distance"][:]
years_velocity_71 =  ice_velocity_during_7["Velocity"][:] 
values_distance_72 = ice_velocity_after_7["Distance"][:]
years_velocity_72 =  ice_velocity_after_7["Velocity"][:] 


#-------------------------------------------READ DATA OF SITE B----------------------------------------------------------

# READ DATAFRAMES ice velocity FLOW LINE 1
ice_velocity_8august_19august_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_1_08Aug15_19Aug15.txt"), delimiter=";")
ice_velocity_before_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_1_19Aug15_30Aug15.txt"), delimiter=";")
ice_velocity_during_3 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_1_30Aug15_09Sep15.txt"), delimiter=";")

# READ DATAFRAMES ice velocity FLOW LINE 2
ice_velocity_8august_19august_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_2_08Aug15_19Aug15.txt"), delimiter=";")
ice_velocity_before_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_2_19Aug15_30Aug15.txt"), delimiter=";")
ice_velocity_during_4 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_2_30Aug15_09Sep15.txt"), delimiter=";")

# READ DATAFRAMES ice velocity FLOW LINE 3
ice_velocity_8august_19august_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_3_08Aug15_19Aug15.txt"), delimiter=";")
ice_velocity_before_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_3_19Aug15_30Aug15.txt"), delimiter=";")
ice_velocity_during_5 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_3_30Aug15_09Sep15.txt"), delimiter=";")

# READ DATAFRAMES ice velocity FLOW LINE 4
ice_velocity_8august_19august_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_4_08Aug15_19Aug15.txt"), delimiter=";")
ice_velocity_before_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_4_19Aug15_30Aug15.txt"), delimiter=";")
ice_velocity_during_6 = pd.read_csv(os.path.join(file_txt_data_folder_site_B, "flow_4_30Aug15_09Sep15.txt"), delimiter=";")


#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 1

xvalues_distance_30 = ice_velocity_8august_19august_3["Distance"][:]
xyears_velocity_30 = ice_velocity_8august_19august_3["Velocity"][:]
xvalues_distance_31 = ice_velocity_before_3["Distance"][:]
xyears_velocity_31 = ice_velocity_before_3["Velocity"][:]
xvalues_distance_32 = ice_velocity_during_3["Distance"][:]
xyears_velocity_32 = ice_velocity_during_3["Velocity"][:]


#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 2

xvalues_distance_42 = ice_velocity_8august_19august_4["Distance"][:]
xyears_velocity_42 = ice_velocity_8august_19august_4["Velocity"][:]
xvalues_distance_43 = ice_velocity_before_4["Distance"][:]
xyears_velocity_43 = ice_velocity_before_4["Velocity"][:]
xvalues_distance_44 = ice_velocity_during_4["Distance"][:]
xyears_velocity_44 = ice_velocity_during_4["Velocity"][:]

#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 3

xvalues_distance_50 = ice_velocity_8august_19august_5["Distance"][:]
xyears_velocity_50 = ice_velocity_8august_19august_5["Velocity"][:]
xvalues_distance_51 = ice_velocity_before_5["Distance"][:]
xyears_velocity_51 = ice_velocity_before_5["Velocity"][:]
xvalues_distance_52 = ice_velocity_during_5["Distance"][:]
xyears_velocity_52 = ice_velocity_during_5["Velocity"][:]


#EXTRACT VALUES FROM DATAFRAMES FLOW LINE 4

xvalues_distance_58 = ice_velocity_8august_19august_6["Distance"][:]
xyears_velocity_58 = ice_velocity_8august_19august_6["Velocity"][:]
xvalues_distance_59 = ice_velocity_before_6["Distance"][:]
xyears_velocity_59= ice_velocity_before_6["Velocity"][:]
xvalues_distance_60 = ice_velocity_during_6["Distance"][:]
xyears_velocity_60 = ice_velocity_during_6["Velocity"][:]




#------------------------------------------CREATE SUBPLOTS---------------------------------------------------------

#CREATE THE PLOT WITH SUBGRID
fig =  plt.figure(figsize=(13,13))

spec2 = gridspec.GridSpec(ncols=3, nrows=5,hspace=0, width_ratios=[0.3,5,5], height_ratios=[3.5,3.5,3.5,3.5,3.5])
spec2.update(wspace=0.2, hspace=0.2)


#DEFINE NESTED GRIDSPEC IN GRIDSPEC IN ORDER TO HAVE 3 SUBPLOTS NESTED IN EACH OF SIX SUBLOPTS DEFINED BEFORE
gs00 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[0,1])
gs01 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[1,1])
gs02 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[2,1])
gs03 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[3,1])
gs04 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[4,1])
gs05 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[0,2])
gs06 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[1,2])
gs07 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[2,2])
gs08 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[3,2])
gs_vertical_left = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[:,0])
#gs_vertical_right = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=spec2[:,2])

#GET COLOOR_RAMP
cmap = mpl.cm.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=2002, vmax=2011)


#----------------------------------------------PLOT SITE A------------------------------------------------------


#PLOT 1 TRANSECT
ax1 = plt.subplot(gs00[0])

ax1.plot(values_distance_31,years_velocity_31,linestyle="None",marker="o",markersize=2.5, color="blue",label="22 August - 2 Septmeber")
ax1.plot(values_distance_32,years_velocity_32,linestyle="None",marker="o",markersize=2.5, color="red",label="2 september-13 September")
ax1.plot(values_distance_33,years_velocity_33,linestyle="None",marker="o",markersize=2.5, color="orange",label="13 September - 24september")
    
ax1.set_title(label="   ", fontsize=24)
ax1.text(0.99, 0.99, 'A1',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax1.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_ylim(0,230)
ax1.set_yticks([0,50,100,150,200])
ax1.set_yticklabels([0,50,100,150,200], fontsize=12)
ax1.set_xlim(-1530,32500)
ax1.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax1.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)

#PLOT 2 TRANSECT

ax2 = plt.subplot(gs01[0])

ax2.plot(values_distance_43,years_velocity_43,linestyle="None",marker="o",markersize=2.5, color="blue",label="22 August - 2 Septmeber")
ax2.plot(values_distance_44,years_velocity_44,linestyle="None",marker="o",markersize=2.5, color="red",label="2 september-13 September")
ax2.plot(values_distance_45,years_velocity_45,linestyle="None",marker="o",markersize=2.5, color="orange",label="13 September - 24september")
 
ax2.text(0.99, 0.99, 'A2',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax2.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim(0,460)
ax2.set_yticks([0,100,200,300,400])
ax2.set_yticklabels([0,100,200,300,400], fontsize=12)
ax2.set_xlim(-1750,37500)
ax2.set_xticks([0,5000,10000,15000,20000,25000,30000,35000])
ax2.set_xticklabels([0,5000,10000,15000,20000,25000,30000,35000], fontsize=12)

#PLOT 3 TRANSECT

ax3 = plt.subplot(gs02[0])

ax3.plot(values_distance_52,years_velocity_52,linestyle="None",marker="o",markersize=2.5, color="blue",label="22 August - 2 Septmeber")
ax3.plot(values_distance_53,years_velocity_53,linestyle="None",marker="o",markersize=2.5, color="red",label="2 september-13 September")
ax3.plot(values_distance_54,years_velocity_54,linestyle="None",marker="o",markersize=2.5, color="orange",label="13 September - 24september")

ax3.text(0.99, 0.99, 'A3',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax3.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.set_ylim(0,230)
ax3.set_yticks([0,50,100,150,200])
ax3.set_yticklabels([0,50,100,150,200], fontsize=12)
ax3.set_xlim(-1350,27000)
ax3.set_xticks([0,5000,10000,15000,20000,25000])
ax3.set_xticklabels([0,5000,10000,15000,20000,25000], fontsize=12)


#PLOT 4 TRANSECT

ax4 = plt.subplot(gs03[0])

ax4.plot(values_distance_61,years_velocity_61,linestyle="None",marker="o",markersize=2.5, color="blue",label="22 August - 2 Septmeber")
ax4.plot(values_distance_62,years_velocity_62,linestyle="None",marker="o",markersize=2.5, color="red",label="2 september-13 September")
ax4.plot(values_distance_63,years_velocity_63,linestyle="None",marker="o",markersize=2.5, color="orange",label="13 September - 24september")

ax4.text(0.99, 0.99, 'A4',
      verticalalignment='bottom', horizontalalignment='center',
#        transform=ax4.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.set_ylim(0,175)
ax4.set_yticks([0,50,100,150])
ax4.set_yticklabels([0,50,100,150],fontsize=12)
ax4.set_xlim(-1530,32500)
ax4.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax4.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)

#PLOT 5 TRANSECT

ax5 = plt.subplot(gs04[0])

ax5.plot(values_distance_70,years_velocity_70,linestyle="None",marker="o",markersize=2.5, color="blue",label="22 August - 2 Septmeber")
ax5.plot(values_distance_71,years_velocity_71,linestyle="None",marker="o",markersize=2.5, color="red",label="2 september-13 September")
ax5.plot(values_distance_72,years_velocity_72,linestyle="None",marker="o",markersize=2.5, color="orange",label="13 September - 24september")

ax5.text(0.99, 0.99, 'A5',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax5.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.set_ylim(0,175)
ax5.set_yticks([0,50,100,150])
ax5.set_yticklabels([0,50,100,150],fontsize=12)
ax5.set_xlim(-1530,32500)
ax5.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax5.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)

ax5.set_xlabel("Distance from ice-sheet margins (m)",labelpad=14,size=14)


#-------------------------------------------------------PLOT SITE B----------------------------------------------------------
#PLOT 1 TRANSECT
ax7 = plt.subplot(gs05[0])
ax7.margins(y=0)

ax7.plot(xvalues_distance_30,xyears_velocity_30,linestyle="None",marker="o",markersize=2.5, color="blue",label="8august_19august")
ax7.plot(xvalues_distance_31,xyears_velocity_31,linestyle="None",marker="o",markersize=2.5, color="orange",label="19august_30august")
ax7.plot(xvalues_distance_32,xyears_velocity_32,linestyle="None",marker="o",markersize=2.5, color="red",label="30august_9september")

ax7.set_title(label="   ", fontsize=24)
ax7.text(0.99, 0.99, 'B1',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax7.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
ax7.margins(x=1500)
ax7.set_ylim(0,1130)
ax7.set_yticks([0,200,400,600,800,1000])
ax7.set_yticklabels([0,200,400,600,800,1000], fontsize=12)
ax7.set_xlim(-1650,32500)
ax7.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax7.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)


#PLOT 2 TRANSECT

ax8 = plt.subplot(gs06[0])


ax8.plot(xvalues_distance_42,xyears_velocity_42,linestyle="None",marker="o",markersize=2.5, color="blue",label="8august_19august")
ax8.plot(xvalues_distance_43,xyears_velocity_43,linestyle="None",marker="o",markersize=2.5, color="orange",label="19august_30august")
ax8.plot(xvalues_distance_44,xyears_velocity_44,linestyle="None",marker="o",markersize=2.5, color="red",label="30august_9september")

 
ax8.text(0.99, 0.99, 'B2',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax8.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)
ax8.set_ylim(0,6900)
ax8.set_yticks([0,1000,2000,3000,4000,5000,6000])
ax8.set_yticklabels([0,1000,2000,3000,4000,5000,6000], fontsize=12)
ax8.set_xlim(-1650,32500)
ax8.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax8.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)



#PLOT 3 TRANSECT
ax9 = plt.subplot(gs07[0])


ax9.plot(xvalues_distance_50,xyears_velocity_50,linestyle="None",marker="o",markersize=2.5, color="blue",label="8august_19august")
ax9.plot(xvalues_distance_51,xyears_velocity_51,linestyle="None",marker="o",markersize=2.5, color="orange",label="19august_30august")
ax9.plot(xvalues_distance_52,xyears_velocity_52,linestyle="None",marker="o",markersize=2.5, color="red",label="30august_9september")

ax9.text(0.99, 0.99, 'B3',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax9.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax9.spines['top'].set_visible(False)
ax9.spines['right'].set_visible(False)
ax9.set_ylim(0,6900)
ax9.set_yticks([0,1000,2000,3000,4000,5000,6000])
ax9.set_yticklabels([0,1000,2000,3000,4000,5000,6000], fontsize=12)
ax9.set_xlim(-1650,32500)
ax9.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax9.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)


#PLOT 4 TRANSECT
ax10 = plt.subplot(gs08[0])

ax10.plot(xvalues_distance_58,xyears_velocity_58,linestyle="None",marker="o",markersize=2.5,color="blue",label="8august_19august")
ax10.plot(xvalues_distance_59,xyears_velocity_59,linestyle="None",marker="o",markersize=2.5, color="orange",label="19august_30august")
ax10.plot(xvalues_distance_60,xyears_velocity_60,linestyle="None",marker="o",markersize=2.5, color="red",label="30august_9september")

ax10.text(0.99, 0.99, 'B4',
        verticalalignment='bottom', horizontalalignment='center',
#        transform=ax10.transAxes,
        color='black', fontsize=13,fontweight="bold")
ax10.spines['top'].set_visible(False)
ax10.spines['right'].set_visible(False)
ax10.set_ylim(0,280)
ax10.set_yticks([0,50,100,150,200,250])
ax10.set_yticklabels([0,50,100,150,200,250], fontsize=12)
ax10.set_xlim(-1650,32500)
ax10.set_xticks([0,5000,10000,15000,20000,25000,30000])
ax10.set_xticklabels([0,5000,10000,15000,20000,25000,30000], fontsize=12)


ax10.set_xlabel("Distance from ice-sheet margins (m)",labelpad=14,size=14)



#----------------------------------------------------PLOT VERTICAL AXES-------------------------------------------------------

#PLOT VERTICAL ICE VELOCITY
ax6 = plt.subplot(gs_vertical_left[0])
ax6.axis('off')
ax6.text(-1.5,0.60,"Velocity(m $yr^{-1})$",rotation = 90, fontsize=28)


#------------------------------------- PLOT LEGEND OF A ------------------------------------------------------------------

#PLOT VERTICAL YEARS

#ax3 = plt.subplot(gs_vertical_right[0])
#ax3.axis('off')
colors= ["blue","red","orange"]
labels= ["22 August - 1 September","2 September - 12 September","13 September - 23 September"]
lines = [Line2D([0], [0],color=c,marker='o', markersize=7, linewidth=False) for c in colors]
leg = ax3.legend(lines, labels, loc="upper right",fontsize=11,ncol=1)
leg.texts[1].set_backgroundcolor("#dddddd")
ax1.text(12888.5, 200.539, r'2013', fontsize=17, fontweight="bold")


#--------------------------------------PLOT LEGEND OF B--------------------------------------------------------------------


colors= ["blue","orange","red"]
labels= ["8 August - 18 August","19 August - 29 August","30 August - 9 September"]
blue = Line2D([0], [0], marker='o', markersize=7,markerfacecolor='blue',linewidth=False,label="8 August - 18 August")
orange = Line2D([0], [0], marker='o', markersize=7,markerfacecolor='orange',linewidth=False,label="19 August - 29 August")
red = Line2D([0], [0], marker='o', markersize=7,markerfacecolor='r',linewidth=False,label="30 August - 9 September")
leg= ax9.legend(handles=[blue,orange,red], loc="upper right",fontsize=11,ncol=1)
leg.texts[1].set_backgroundcolor("#dddddd")
leg.texts[2].set_backgroundcolor("#dddddd")
ax7.text(12888.5, 970.539, r'2015', fontsize=17, fontweight="bold")

#===========================================SAVE THE FIGURE(OPTIONAL)======================================
# SAVE FIGURE AS PNG
# output_path = os.path.join(output_folder, "velocity_along_entire_flowlines_site_A_and_B.png")
# plt.savefig(output_path, dpi=300, bbox_inches="tight")
# plt.close()