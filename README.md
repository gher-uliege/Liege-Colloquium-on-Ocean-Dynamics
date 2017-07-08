# Liège Colloquium on Ocean Dynamics

Started in 2016, this project was meant to store the [LaTeX](./latex) files used to create the colloquium poster for the [2016 edition](http://modb.oce.ulg.ac.be/?page=colloquium&year=2016). It has evolved into a more consistent repository with a few [Jupyter notebooks](./notebooks) designed to prepare figures and illustrations for the Colloquium and that could be re-used for future editions, hopefully.

For the 50th Edition (2018), the plan is to have an overview of the previous editions in terms of countries, topics and participants.

## Directories

* **figures**: time evolution of the number of received abstracts, spatial distribution of the abstracts and other figures necessary for the poster.
* [**latex**](./latex/README.md): sources to create the poster in pdf.
* **logos**: partners and sponsors, necessary for the poster.
* [**notebooks**](./notebook/README.md): tools to create the abstract maps and time series.

<img src="./figures/abstractslist2016_map.png " width="500">

## Requirements

### LaTeX

For the posters/flyers, we use the [`beamer`](https://www.ctan.org/tex-archive/macros/latex/contrib/beamer?lang=en) class along with other packages to include logos, draw line and enlarge part of an image:
* [tikz](https://www.ctan.org/pkg/pgf?lang=en)
* [marvosym](https://www.ctan.org/pkg/marvosym?lang=en)
* [fontawesome](https://www.ctan.org/tex-archive/fonts/fontawesome?lang=en)        
In addition, you need to have the fonts Cube-Regular and DINM2 installed in a directory where LaTeX can find them.
 
### Python 
The first notebooks were run using Python 2.7, while the most recent code is in Python 3.6.     
Basic packages were installed for the plotting:
* [matplotlib](https://matplotlib.org/)
* [bokeh](http://bokeh.pydata.org)
* [pandas](http://pandas.pydata.org/)   


<img src="./figures/CLQ2016_poster.jpg " width="500">
