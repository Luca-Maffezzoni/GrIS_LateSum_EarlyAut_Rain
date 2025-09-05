# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:01:25 2021

@author: lucam
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#==============================================SPECIFY THE ROOT OF THIS SCRIPT AND OF THE OUTPUT FILE PLOT .png==============================

ROOT = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(ROOT, "..", "data", "OUTPUT", "FIGURES")

#===========================================================READ DATA ADND SPECIFY PLOT SIZE===============================================

#READ DATA SITE A 2013 ENERGY FLUXES
september_LHF = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_A", "aug_sept_2013_daily_LHF.txt"), delimiter=";")
september_LW_net = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_A", "aug_sept_2013_daily_LW_net.txt"), delimiter=";")
september_SHF = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_A", "aug_sept_2013_daily_SHF.txt"), delimiter=";")
september_SW_net = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_A", "aug_sept_2013_daily_SW_net.txt"), delimiter=";")

#READ DATA SITE B 2015 ENERGY FLUXES
september_LHF_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_B", "aug_sept_2015_daily_LHF.txt"), delimiter=";")
september_LW_net_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_B", "aug_sept_2015_daily_LW_net.txt"), delimiter=";")
september_SHF_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_B", "aug_sept_2015_daily_SHF.txt"), delimiter=";")
september_SW_net_2 = pd.read_csv(os.path.join(ROOT, "..", "Data", "INPUT", "SEB_PARM", "SITE_B", "aug_sept_2015_daily_SW_net.txt"), delimiter=";")

#SPECIFY THE GRID PLOTS
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(28,10))

#==========================EXTRACT DAILY VALUES LHF,SHF,LW_net and SW_net and Plot SEB SITE A====================================

LHF = september_LHF["Values"]
LHF_days = september_LHF["Days"]
#EXTRACT DAILY VALUES SHF_net
SHF = september_SHF["Values"]
#EXTRACT DAILY VALUES LW_net
LW_net = september_LW_net["Values"]
#EXTRACT DAILY VALUES SW_net
SW_net = september_SW_net["Values"]

ax1.text(0.04, 0.05, '(a)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax1.transAxes,
        color='black', fontsize=20)

ind = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155])
width = 4.3

#axes and labels
ax1.set_xlim(4.5,160.1)
ax1.set_ylim(-120,180)
ax1.set_yticks([-100,-50,0,50,100,150])
ax1.set_yticklabels([-100,-50,0,50,100,150], fontsize=22)

#CREATE PLOT
ax1.set_ylabel('Energy flux ($W/m^{2}$)',fontsize=28)
ax1.set_axisbelow(True)

#plot values SW_net
rects1 = ax1.bar(ind+2.4, SW_net, width, color="#fcb001",edgecolor="black",linewidth=2)

#plot values LHF            
array_base = np.array([])
a=0
for i in LHF:
    if i > 0:
        array_base=np.append(array_base,SW_net[a])
    else:
        array_base=np.append(array_base,0)
    a = a + 1

rects2 = ax1.bar(ind+2.4, LHF, width, bottom=array_base, color="blue",edgecolor="black",linewidth=2)

#plot values LW_net
array_base_2 = np.array([])
b=0

for j in LHF:
    if j < 0:
        array_base_2 =np.append(array_base_2,LHF[b])
    else:
        array_base_2 =np.append(array_base_2,0)
    b = b + 1
        
rects3 = ax1.bar(ind+2.4, LW_net, width, bottom = array_base_2, color="green",edgecolor="black",linewidth=2)

#plot values SHF
array_base_3 = np.array([])
c=0
for k in SHF:
    if k >0:
        if LHF[c]>0:
            array_base_3 = np.append(array_base_3,SW_net[c]+LHF[c])
        else:
            array_base_3 = np.append(array_base_3,SW_net[c])
    else:
        if LHF[c]<0:
            array_base_3 = np.append(array_base_3,LW_net[c] + LHF[c])
        else:
            array_base_3 = np.append(array_base_3, LW_net[c])
    c = c +1
    
rects4 = ax1.bar(ind+2.4, SHF, width, bottom = array_base_3, color="red",edgecolor="black",linewidth=2)    
    

#plot values 
#add 0 line
ax1.axhline(y=0, color='black', linestyle='-')
#add legend
ax1.legend((rects1[0], rects2[0], rects3[0],rects4[0]), ('SW_net', 'LHF',"LW_net","SHF"),loc= "upper right",fontsize=19)


#set xticks
major=[LHF_days[0],LHF_days[5],LHF_days[10],LHF_days[15],LHF_days[20],LHF_days[25],LHF_days[30]]

ax1.tick_params(axis = 'x', which = 'major', direction = 'in', labelsize = 10, length=10)
ax1.tick_params(axis = 'x', which = 'minor',direction = 'in', labelsize = 0, length = 5)

#Set label for major and minor ticks
ax1.set_xticks([ind[0],ind[5],ind[10],ind[15],ind[20],ind[25],ind[30]])
ax1.set_xticks([ind[1],ind[2],ind[3],ind[4],ind[6],ind[7],ind[8],ind[9],ind[11],ind[12],ind[13],ind[14],ind[16],ind[17],ind[18],ind[19],ind[21],ind[22],ind[23],ind[24],ind[26],ind[27],ind[28],ind[29]],minor=True)

xtickNames = ax1.set_xticklabels([LHF_days[0],LHF_days[5],LHF_days[10],LHF_days[15],LHF_days[20],LHF_days[25],LHF_days[30]])
plt.setp(xtickNames,fontweight="bold", rotation=45, fontsize=24)

ax1.text(ind[14], 164, "Site A",fontweight='bold', fontsize=24)
ax1.text(ind[0], 164, "2013", fontsize=24)

#Set grey columns through the entire plot representing the events studied in 2012 
#GREY COLUMN
ax1.axvspan(ind[12], ind[19], facecolor='grey', alpha=0.3,zorder=0)

#==========================EXTRACT DAILY VALUES LHF,SHF,LW_net and SW_net and Plot SEB SITE B====================================
LHF = september_LHF_2["Values"]
LHF_days = september_LHF_2["Days"]
#EXTRACT DAILY VALUES SHF_net
SHF = september_SHF_2["Values"]
#EXTRACT DAILY VALUES LW_net
LW_net = september_LW_net_2["Values"]
#EXTRACT DAILY VALUES SW_net
SW_net = september_SW_net_2["Values"]


ax2.text(0.04, 0.05, '(b)',
        verticalalignment='top', horizontalalignment='right',
        transform=ax2.transAxes,
        color='black', fontsize=20)

ind = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160])
width = 4.3

#axes and labels
ax2.set_xlim(4.5,165.1)
ax2.set_ylim(-120,180)
ax2.set_yticks([-100,-50,0,50,100,150])
ax2.set_yticklabels([-100,-50,0,50,100,150], fontsize=22)

#CREATE PLOT
ax2.set_ylabel('Energy flux ($W/m^{2}$)',fontsize=28)
ax2.set_axisbelow(True)

#plot values SW_net
rects1 = ax2.bar(ind+2.4, SW_net, width, color="#fcb001",edgecolor="black",linewidth=2)

#plot values LHF            
array_base = np.array([])
a=0
for i in LHF:
    if i > 0:
        array_base=np.append(array_base,SW_net[a])
    else:
        array_base=np.append(array_base,0)
    a = a + 1

rects2 = ax2.bar(ind+2.4, LHF, width, bottom=array_base, color="blue",edgecolor="black",linewidth=2)

#plot values LW_net
array_base_2 = np.array([])
b=0

for j in LHF:
    if j < 0:
        array_base_2 =np.append(array_base_2,LHF[b])
    else:
        array_base_2 =np.append(array_base_2,0)
    b = b + 1
        
rects3 = ax2.bar(ind+2.4, LW_net, width, bottom = array_base_2, color="green",edgecolor="black",linewidth=2)

#plot values SHF
array_base_3 = np.array([])
c=0
for k in SHF:
    if k >0:
        if LHF[c]>0:
            array_base_3 = np.append(array_base_3,SW_net[c]+LHF[c])
        else:
            array_base_3 = np.append(array_base_3,SW_net[c])
    else:
        if LHF[c]<0:
            array_base_3 = np.append(array_base_3,LW_net[c] + LHF[c])
        else:
            array_base_3 = np.append(array_base_3, LW_net[c])
    c = c +1
    
rects4 = ax2.bar(ind+2.4, SHF, width, bottom = array_base_3, color="red",edgecolor="black",linewidth=2)    
    

#plot values 
#add 0 line
ax2.axhline(y=0, color='black', linestyle='-')
#add legend
ax2.legend((rects1[0], rects2[0], rects3[0],rects4[0]), ('SW_net', 'LHF',"LW_net","SHF"),loc= "upper right",fontsize=19)


#set xticks
major=[LHF_days[0],LHF_days[5],LHF_days[10],LHF_days[16],LHF_days[21],LHF_days[26],LHF_days[31]]

ax2.tick_params(axis = 'x', which = 'major', direction = 'in', labelsize = 10, length=10)
ax2.tick_params(axis = 'x', which = 'minor',direction = 'in', labelsize = 0, length = 5)

#Set label for major and minor ticks
ax2.set_xticks([ind[0],ind[5],ind[10],ind[16],ind[21],ind[26],ind[31]])
ax2.set_xticks([ind[1],ind[2],ind[3],ind[4],ind[6],ind[7],ind[8],ind[9],ind[11],ind[12],ind[13],ind[14],ind[15],ind[17],ind[18],ind[19],ind[20],ind[22],ind[23],ind[24],ind[25],ind[27],ind[28],ind[29],ind[30]],minor=True)

xtickNames = ax2.set_xticklabels([LHF_days[0],LHF_days[5],LHF_days[10],LHF_days[16],LHF_days[21],LHF_days[26],LHF_days[31]])
plt.setp(xtickNames,fontweight="bold", rotation=45, fontsize=24)

ax2.text(ind[15], 164, "Site B",fontweight='bold', fontsize=24)
ax2.text(ind[0], 164, "2015", fontsize=24)

#Set grey columns through the entire plot representing the events studied
#GREY COLUMN
ax2.axvspan(ind[13], ind[23], facecolor='grey', alpha=0.3,zorder=0)

fig.tight_layout()

plt.show()

#===========================================SAVE THE FIGURE(OPTIONAL)======================================
# SAVE FIGURE AS PNG
# output_path = os.path.join(output_folder, "SEB_Figure_S3")
# plt.savefig(output_path, dpi=300, bbox_inches="tight")
# plt.close()
