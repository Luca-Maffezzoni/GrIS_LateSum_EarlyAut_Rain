Here you find the flowlines output coming from r.flow algorithm in GRASS-GIS applied on the multy_year_velocity dataset (multy_year_vv_SITE_B) at the site B studied.
Subsequently, by the use of the DEM that you can find the RAW DATA (GrIS_Digital_elevation_model_90m_v01.1) along with the GRASS output we draw the four
flow lines of this site B.

NOTE: The velocity pixel values in the raster were inverted from positive to negative.This allows the r.flow algorithm, which follows the gradient, 
to track a negative gradient from upstream to downstream, thereby generating flow lines in the correct direction (mountain to valley). If the pixel 
values had remained positive, the flow lines would have been generated in the opposite direction (valley to mountain).