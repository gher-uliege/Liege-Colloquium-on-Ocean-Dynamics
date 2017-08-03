import os
import re
import logging
from collections import Counter
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3, OpenMapQuest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib import colorbar
from matplotlib import rcParams
from matplotlib.collections import LineCollection
from mpl_toolkits.axes_grid.inset_locator import zoomed_inset_axes
import shapefile
import pycountry
from geolite2 import geolite2



arcgis = ArcGIS(timeout=100)
nominatim = Nominatim(timeout=100)
googlev3 = GoogleV3(timeout=100)
openmapquest = OpenMapQuest(timeout=100)

logloc = logging.getLogger('locator')
logloc.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logloc.addHandler(ch)

# choose and order your preference for geocoders here
geocoders = [nominatim, googlev3, arcgis, openmapquest]


class Participant(object):

    def __init__(self, name=None, firstname=None, affiliation=None, city=None, 
                 country=None, countryname=None):
        self.name = name
        self.firstname = firstname
        self.affiliation = affiliation
        self.city = city
        self.country = country
        self.lon = None
        self.lat = None
        self.countryname = countryname
    
    def __repr__(self):
        return "Participant {0} {1} ({2})".format(self.firstname,
                                                  self.name,
                                                  self.country)
        
    def replace_country(self):
        dictcountry = {"U.S.A.": "United States of America", 
                       "The Netherlands": "Netherlands",
                       "U.K.": "United Kingdom",
                       "Republic of Burundi": "Burundi",
                       "Belgique": "Belgium",
                       #"Russia": "Russian Federation",
                       "Maroc": "Morocco",
                       "México": "Mexico",
                       "Cameroun": "Cameroon",
                       "Côte d'Ivoire": "Ivory Coast",
                       "Serbia": "Republic of Serbia",
                       "Bulgary": "Bulgaria",
                       "Sénégal": "Senegal"}
        for k, v in dictcountry.items():
            self.country = self.country.replace(k, v)

    def get_location(self):
        # Try with different combinations of affiliation, city, country

        locationstring = ", ".join((self.affiliation, self.city, self.country))
        logloc.info(locationstring)

        i = 0
        lon = None
        lat = None
        countryname = None

        while not lon and not lat:

            # logloc.debug("i = {0}".format(i))
            try:
                # try to geocode using a service
                location = geocoders[i].geocode(locationstring)

                # if it returns a location
                if location is not None:
                    logloc.debug("Ok with Geocoder: {0}".format(geocoders[i]))
                    # return those values
                    lat = location.latitude
                    lon = location.longitude
                    # Not all the locators work the same way!
                    # countryname = location.raw["display_name"].split(",")[-1].strip()
                else:
                    logloc.debug("Geocoder {0} did not provide coordinates".format(geocoders[i]))

            except:
                # catch whatever errors, likely timeout, and return null values
                logloc.debug("Problem with geocoder {0}".format(geocoders[i]))

            # Try another geocoder
            i += 1

        self.lon = lon
        self.lat = lat
        self.countryname = countryname

        return locationstring, location

    def write_to(self, filename, sep="\t"):
        """
        Write the participants information into a file
        """
        with open(filename, 'a') as f:
            f.write(sep.join((self.name, self.firstname, 
                             self.affiliation, self.country,
                             str(self.lat),
                             str(self.lon), "\n")))
    
    def write_coords_to(self, filename, sep="\t"):
        """
        Write the coordinates in a file
        """
        with open(filename, 'a') as f:
            f.write("[{0}, {1}],\n".format(self.lat, self.lon))


def make_country_map(countrylist, shapefile, m, figname, year=None,
                     bounds=(1, 2, 4, 6, 8, 10, 15, 20),
                     cmap=cm.YlGnBu,
                     logofile="../logos/logo_colloquium.png"):
    """
    :param countrylist: list of country iso-codes
    :param shapefile: path of the shape file
    :param m: projection created with Basemap
    :param figname: path of the figure to be created
    :param year: considered year
    :param bounds: bounds of the colorbar
    :param cmap: colormap
    :param logofile: file storing the CLQ logo
    :return:
    """

    # Count the occurrence of each country in the list
    countrycount = Counter(countrylist)
    nmax = max(countrycount.values())

    shapes, records = read_shape(shapefile)

    fig = plt.figure(figsize=(11.7, 8.3))
    ax = plt.subplot(111)
    rcParams.update({'font.size': 16})

    if year is not None:
        titletext = "{0}: {1} participants".format(year, len(countrylist))
        plt.title(titletext, fontsize=20)

    m.drawcountries(linewidth=0.1)
    m.drawcoastlines(linewidth=0.1)

    """
    axins = zoomed_inset_axes(ax, 2.5, loc=3)
    m.drawcountries(linewidth=.2, ax=axins)
    x, y = m(-15., 35.)
    x2, y2 = m(27, 60.)
    axins.set_xlim(x, x2)
    axins.set_ylim(y, y2)
    axins.axis('off')
    """

    for record, shape in zip(records, shapes):
        countryname = record[1]
        if countryname in countrycount:
            lons, lats = zip(*shape.points)
            data = np.array(m(lons, lats)).T

            if len(shape.parts) == 1:
                segs = [data, ]
            else:
                segs = []
                for i in range(1, len(shape.parts)):
                    index = shape.parts[i-1]
                    index2 = shape.parts[i]
                    segs.append(data[index:index2])
                segs.append(data[index2:])

            lines = LineCollection(segs, antialiaseds=(1,))
            lines.set_facecolors(cmap(countrycount[countryname]/nmax))
            lines.set_edgecolors('k')
            lines.set_linewidth(0.1)
            ax.add_collection(lines)

            """
            lines2 = LineCollection(segs, antialiaseds=(1,))
            lines2.set_facecolors(cmap(countrycount[countryname] / nmax))
            lines2.set_edgecolors('k')
            lines2.set_linewidth(0.1)
            axins.add_collection(lines2)
            """

    cax = fig.add_axes([0.475, 0.21, 0.4, 0.02])
    cmap.set_over((0., 0., 0.))
    cb1 = colorbar.ColorbarBase(cax, cmap=cmap,
                                norm=colors.BoundaryNorm(bounds, cmap.N),
                                orientation='horizontal', spacing='uniform',
                                extend='max', label='Number of participants')

    cb1.ax.xaxis.set_label_position('top')

    if os.path.exists(logofile):
        im = plt.imread(logofile)
        newax = fig.add_axes([0.85, 0.85, 0.07, 0.07], anchor='NE')
        newax.imshow(im)
        newax.axis('off')

    # Remove frame
    ax.axis('off')
    # Add year in upper-left corner
    # plt.annotate(year, xy=(0.05, 8.5), xycoords='axes fraction', fontsize=30)

    plt.savefig(figname, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()


def read_shape(filename):
    """
    Read shapes from shapefile
    :param filename: path to the file containing the shape
    :return: shape
    :return: records
    """
    try:
        r = shapefile.Reader(filename)
        shapes = r.shapes()
        records = r.records()
    except IOError as exc:
        raise IOError("%s: %s" % (filename, exc.strerror))

    return shapes, records


def countries_from_abstract_list(filename):
    """
    Create a list of countries using the Colloquium abstract list
    :param filename: path to the abstract file
    :type filename: str
    :return countrylist: list of country iso-codes
    """

    reader = geolite2.reader()
    countrylist = []
    nlines = 0

    try:
        with open(filename, 'r') as f:
            for lines in f.readlines():
                nlines += 1
                match = re.search(r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})_IP_(\d+\.\d+\.\d+\.\d+).json',
                                  lines)
                if match:
                    ip = match.group(7)
                    logging.debug("IP: {}".format(ip))
                    match_ip = reader.get(ip)
                    if match_ip:
                        countrylist.append(match_ip['country']['iso_code'])
    except IOError as exc:
        raise IOError("%s: %s" % (filename, exc.strerror))

    logloc.info("Number of abstracts in the list: {}".format(nlines))
    logloc.info("Number of identified countries: {}".format(len(countrylist)))

    return countrylist


def countries_from_particitant_list(filename):
    """
    Return a list of country iso-codes from a list of participants
    (.tsv files located in ../data/ directory).
    :param filename: path to the file containing the participants
    :type filename: str
    :return: country_iso_list
    """

    # start with empty list
    country_iso_list = []
    with open(filename, 'r') as f:
        line = f.readline().rstrip()
        while line:
            country = line.split('\t')[-1]
            # Create fake participant to substitute the country
            p = Participant(country=country)
            p.replace_country()

            country_iso_list.append(pycountry.countries.lookup(p.country).alpha_2)
            line = f.readline().rstrip()

    return country_iso_list
