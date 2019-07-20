## Notebook

The notebooks using [folium](https://github.com/python-visualization/folium/) package were developed with the version 0.1.6.    
Some part of the code will probably not work with the most recent versions, since some functions were deprecated (e.g., folium.map.geojson).     

<img src="../figures/foliummap.png " width="600">

| Tool              | Description              |
|  ----------------:|--------------------------|
|abstract_time_bokeh|Bokeh plot of the time series of abstract received. |
|abstract_time_highchart|Create highcharts plots  of the abstract time series using [pandas-highcharts](https://pypi.python.org/pypi/pandas-highcharts/).|
|abstract_time|Read the list of abstracts and generate a time series plot. |
|compute_participant_distance| Compute the total distance traveled by each participant. |
|parse-Colloquium-publications|Extract author information and article title using journal web page. |
|plot_abstracts_map| Create participation map using the IP from the lists of abstract.|
|plot_folium_abstract_map|Create a map with the countries color according to the number of received abstracts.|
|plot_folium_hotels|Create interactive [leaflet](http://leafletjs.com/) map with the hotels and the interesting locations.||
|read_csv_participants|Read participant information from CSV file.|

### Participation maps

Specifically for the preparation of this [map](https://gher-ulg.github.io/Liege-Colloquium/participationMap.html), one needs to
1. Convert the list of participants (with affiliation) to a list of coordinates, using the tool [get_coordinates_from_participant_list](https://github.com/gher-ulg/Liege-Colloquium-on-Ocean-Dynamics/blob/master/notebook/get_coordinates_from_participant_list.ipynb).
2. Use the list of coordinates to create a `geoJSON` file with the countries and the corresponding number of attendees.
[count_countries](https://github.com/gher-ulg/Liege-Colloquium-on-Ocean-Dynamics/blob/master/notebook/count_countries.ipynb)

Note that there is a lot of missing data from 1990 to 1996 ad from 1998 to 1999.

### Wordle

The [`Wordle`](https://gher-ulg.github.io/Liege-Colloquium/topicwordle.html) is based on the list of topics (file [topic.md](https://github.com/gher-ulg/gher-ulg.github.io/blob/master/Liege-Colloquium/topics.md)) with the tool
[word_count.ipynb](https://github.com/gher-ulg/Liege-Colloquium-on-Ocean-Dynamics/blob/master/notebook/word_count.ipynb).
