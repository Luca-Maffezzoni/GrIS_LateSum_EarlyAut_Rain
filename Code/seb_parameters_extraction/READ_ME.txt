# All the scripts in the SITE_A and SITE_B folders extract data separately
# for the period selected around the two rainfall events, using as RAW data the files already extracted
# from the annual .nc files, selecting the specific season
# (see Data/RAW/MAR_DATA_MET_GLACIO_VARIABLE_EXTRACTION).
# These scripts compute daily mean values of albedo(AL1), latent heat flux (LHF), Long-wave downward (LWD), Long-wave upward (LWU)
# Sensible heat flux (SHF) and Short-wave downward (SWD) for the respective catchments using the SMB masks.

# Note: The outputs of these scripts for SITE_A and SITE_B 
# are not shown in the PROCESSED data folder, because the author provides 
# the post processed data with headers in Data/INPUT/SEB_PARAM for SITE_A and SITE_B, 
# which serve as inputs for the subsequent script named "07_plot_SEB_Figure_S3.py". In these files, 
# the net longwave radiation (LW_net) of interest for this study has already been 
# calculated as LWD - LWU, and the net shortwave radiation (SW_net) as SWD - SWU / 100 * AL1. 
# Therefore, the final data ready for the next script are: LHF, SHF, LW_net, and SW_net.