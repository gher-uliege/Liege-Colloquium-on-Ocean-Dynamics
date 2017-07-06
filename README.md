# Liège Colloquium on Ocean Dynamics

Started in 2016, this project is meant to store the LaTeX files used to create the colloquium poster for the [2016 edition](http://modb.oce.ulg.ac.be/?page=colloquium&year=2016). It has evolved into a more consistent repository with a few [Jupyter notebooks](http://jupyter.org/) designed to prepare figures and illustrations for the Colloquium and that could be re-used for future editions, hopefully.

For the 50th Edition (2018), the plan is to have an overview of the previous editions in terms of countries, topics and participants.

## Directories

* **figures**: time evolution of the number of received abstracts, spatial distribution of the abstracts and other figures necessary for the poster.
* [**latex**](./latex/README.md): sources to create the poster in pdf.
* **logos**: partners and sponsors, necessary for the poster.
* [**notebooks**](./notebook/README.md): tools to create the abstract maps and time series.

<img src="./figures/abstractslist2016_map.png " width="500">

## Requirements

* The 1st notebooks were run using Python 2.7, while the most recent code is in Python 3.6. Basic packages were installed for the plotting.
* LaTeX: you need to have the fonts Cube-Regular and DINM2 installed in a directory where LaTeX can find them.

<img src="./figures/CLQ2016_poster.jpg " width="500">
