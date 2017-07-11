## Notebook

The notebooks using [folium](https://github.com/python-visualization/folium/) package were developed with the version 0.1.6.    
Some part of the code will probably not work with the most recent versions, since some functions were deprecated (e.g., folium.map.geojson).     

<img src="../figures/foliummap.png " width="600">

| Tool              | Description              |
|  ----------------:|--------------------------|
|abstract_time_bokeh|Bokeh plot of the time series of abstract received. |
|abstract_time_highchart|Create highcharts plots  of the abstract time series using [pandas-highcharts](https://pypi.python.org/pypi/pandas-highcharts/).|
|abstract_time|Read the list of abstracts and generate a time series plot. |
|get_coordinates_from_participant_list|Reads a tab separated file containing the author name affiliation, and generate the coordinates corresponding to their institude.|
|parse-Colloquium-publications|Extract author information and article title using journal web page. |
|plot_abstracts_map| Create participation map using the IP from the lists of abstract.|
|plot_folium_abstract_map|Create a map with the countries color according to the number of received abstracts.|
|plot_folium_hotels|Create interactive [leaflet](http://leafletjs.com/) map with the hotels and the interesting locations.||
|read_csv_participants|Read participant information from CSV file.|
