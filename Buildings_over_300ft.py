#################
# Zachary Conner
# GTECH 731
# Homework 7
#
# The following script uses Arcpy to select all buildings in Manhattan
# that are taller than 300 feet and creates a feature layer.
#
# Input:
#   Manhattan building footprint shapefile
#   Manhattan elevation shapefile
#
# Output:
#   A feature layer that conatins all of the buildings in Manhattan 300 ft or taller
#################

import arcpy as ap
ap.env.workspace = "C:\Users\zconner\Desktop\ZacharyConner_07"
buildings = 'manh_bldgs.shp'
elevation = 'manh_elevation.shp'
 
output = 'bldgs_elevation'
ap.SpatialJoin_analysis(buildings,elevation, output, "JOIN_ONE_TO_ONE", "#", "#", "COMPLETELY_CONTAINS")
 
in_layer = 'bldgs_elevation'
ap.MakeFeatureLayer_management(in_layer, "bldgs_over_300_feet", "ELEVATION > 300")
