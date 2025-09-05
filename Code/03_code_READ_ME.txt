This script was made with QGIS software version 3.10.1 not directly writing but with the MODEL BUILDER tool.
This script must be run within QGIS (Processing Toolbox → run script)

---------------------------------------------------------INPUT FILES-------------------------------------------------

The requested input files for each run are the 1)single flowline (shapefile) and 2)an ice velocity (or error associated) image pairs raster:
1) They can be find in "Data/INPUT/GIS_SITE_A/SITE_A_flow_lines_shape" and "Data/INPUT/GIS_SITE_B/SITE_B_flow_lines_shape"
2) They can be find in "Data/INPUT/GIS_SITE_A/RASTER_ICE_VELOCITY_SELECTED_SITE_A" and "Data/INPUT/GIS_SITE_B/RASTER_ICE_VELOCITY_SELECTED_SITE_B"

---------------------------------------------------------OUTPUT FILES------------------------------------------------

The single output for each run is and HTML file in your local folder with some statistics including the average value of velocity along the flowline.
#########################################################################################################################################
For convenience, data generated above were grouped: for each flowline, two separate text files were generated. The first file ("flow_line_mean_*.txt") contains the mean ice velocity values calculated for 
all selected image pair periods (the first column in the file indicates the central day of the period covered by each image pair, whereas the second column provides 
the extracted mean velocity value), while the second file ("flow_line_error_*.txt") reports the corresponding mean errors associated. 

The .txt files are located in "Data/PROCESSED/AVERAGE_VELOCITY_FLOWLINES_SITE_A" and "Data/PROCESSED/AVERAGE_VELOCITY_FLOWLINES_SITE_B".


-------------------------------------------------------------NOTE----------------------------------------------------

NOTE: the ice velocity image pairs above (and error associated) coming from MEaSUREs Selected Glacier Site Velocity Maps for Greenland from lnSAR, 
Version 3 (Joughin et al., 2020) are resampled in our study through bilinear interpolation (QGIS_Function) to the same coarser spatial resolution 
of 250 m as MEaSUREs Multi-year Greenland Ice Sheet Velocity dataset(Joughin et al., 2016) to enable comparisons.
