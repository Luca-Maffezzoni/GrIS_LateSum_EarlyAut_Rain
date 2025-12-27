# The scripts "extract_sum_ruonff_1985_2015.py" and "SMB_1985_2015.py"
# calculate, respectively, the 31-year cumulative runoff and SMB,
# and save the results in the folder Data/PROCESSED/MET_GLACIO_PARAMETERS.

# In the SITE_A folder, the scripts "extract_2_basins_RU_above_200mm.py"
# and "SMB_1985_2015_basins_site_A.py" mask the previous runoff and SMB files,
# extracting only the data for the two catchments of site A,
# and save the outputs in Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_A.

# Similarly, in the SITE_B folder, the scripts "extract_3_basins_RU_above_200mm.py"
# and "SMB_1985_2015_basins_site_B.py" mask the original runoff and SMB files,
# extracting only the data for the three catchments of site B,
# and save the outputs in Data/PROCESSED/MET_GLACIO_PARAMETERS/SITE_B.

# All other scripts in the SITE_A and SITE_B folders extract data separately
# for May and for Summer+September, using as RAW data the files already extracted
# from the annual .nc files, selecting the specific season
# (see Data/RAW/MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION).
# These scripts compute daily mean values of meltwater, rainfall, runoff, and temperature
# for the respective catchments using the runoff and SMB masks.

# Note: The outputs of these other scripts in SITE_A and SITE_B
# (those that extract data from May 1 to September 30) are not shown
# in the PROCESSED data folder, because the author provides in
# Data/INPUT/MET_GLAC_PARAM for SITE_A and SITE_B the merged
# data for each of the four variables from May 1 to September 30
# in single .txt files useful as input for the script "06_plot_average_velocity_and_met_glacio_variable_Figure_2.py"
