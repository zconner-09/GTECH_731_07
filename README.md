# GTECH_731_07
Homework assignment 7 for GTECH 731. The goal of this assignment is to get some working familiarity with ArcPy. Write a Python script that uses ArcPy to create an output dataset from an input dataset, using at least one toolbox call. Some data to work with is included in the attached file <br />
manh_data.zip <br /> 

I'd recommend this option if you want to explore a little more and use local data.

manh_bldgs.shp - building footprint polygons for buildings in Manhattan. <br />
manh_dem.tif – a digital elevation model of Manhattan, downloaded from the USGS and part of the National Elevation Dataset (NED). Elevation is in meters above sea level. <br />
manh_elevation.shp – elevation point data for Manhattan, including rooftop elevations. <br />
manhattan.shp – a polygon outlining the Manhattan borough boundary. <br />
manh_streets - manhattan's street network. <br />
Here are some suggestions that use the posted data, ordered (approximately) by increasing difficulty: <br />

Suppose you want to view the largest buildings on a map. Write a script that selects and outputs the top X percentile buildings by size in Manhattan.

Suppose a storm is coming and you want to see the the points at risk of flooding for a given storm surge, i.e., the elevation points below the threshold. Write a script that selects and outputs the points below that threshold.

Do the same but create a polygon so you can display the at-risk areas on a map.Suppose you want to plan a walking trip the length of Broadway. Write a script the adds up the length of all the line segments that make up Broadway in Manhattan.

Suppose you need to identify the buildings at risk for flooding for any given storm surge.  One method would be to find the centroid of each building, and get the ground elevation from the DEM for each of these points.
Suppose you are estimating energy consumption across the buildings in Manhattan and need to know the volume(height x area) of every building. Write a script that finds the height of all the buildings, and multiplies that by the area of each building polygon, and writes the result to a new field in the buildingshape file containing the volume.

Some toolbox functions that might be useful: <br />

ExtractValuesToPoints - extracts raster values to point shapes <br />
AddField_management - adds an attribute field <br />
UpdateCursor - updates records <br />
SpatialJoin_analysis - joins based on spatial relationship  <br />
CalculateAreas_stats - calculates polygon areas <br />
MakeFeatureLayer_management - creates a new layer with optional filter <br />
CalculateField_management - populates a calculated field <br />
CopyFeatures_management - creates a new feature class from an existing one <br />
SelectLayerByAttribute_management - select rows by attribute <br />
AggregatePoints_cartography - creates polygons from clusters of points <br />
Intersect_analysis - finds intersecting geometries <br />
Delete_management - delete selected rows <br />
Idw - create an interpolated surface using inverse distance weighting <br />
Clip_management - clips a raster to a rectangle or geometry <br />
Select_analysis - selects records by attribute value  <br />
