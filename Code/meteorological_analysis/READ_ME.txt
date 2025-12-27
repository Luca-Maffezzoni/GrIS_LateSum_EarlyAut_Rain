# The scripts in the SITE_A and SITE_B folders extract meteorological data 
# for the two rainfall events under study, using the annual .nc files in 
# Data/RAW/MAR_ANNUAL as input (selecting the relevant year/years).

# Rainfall(RF), cloud cover (CM) were calculated only during the two cyclonic periods at site A and B in 2013 and 2015.

# To compute TAS anomalies, two datasets were prepared:
#   1) the mean TAS during the two cyclonic events (Mean_TTZ_during_event.py), and 
#   2) the mean TAS over the climatological period 1985–2015 (Mean_TTZ_during_event_climatology_1985-2015.py) during the same day of the year of the cyclonic events.
# The anomaly is then obtained by subtracting (1) from (2).

# All output files have already been saved in 
# Data/PROCESSED/METEOROLOGICAL_ANALYSIS/ under the respective SITE_A and SITE_B folders.

# These processed outputs data serve as the input data for the scripts 
# "08_plot_gpt_tas_anomaly_Figure_S1.py" and "09_cloud_rainfall_Figure_S3.py".