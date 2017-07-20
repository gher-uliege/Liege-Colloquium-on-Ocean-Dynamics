import os
import sys
import glob
import logging
from collections import Counter
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3, OpenMapQuest


arcgis = ArcGIS(timeout=100)
nominatim = Nominatim(timeout=100)
googlev3 = GoogleV3(timeout=100)
openmapquest = OpenMapQuest(timeout=100)

logloc= logging.getLogger('locator')
logloc.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logloc.addHandler(ch)

# choose and order your preference for geocoders here
geocoders = [nominatim, googlev3, arcgis, openmapquest]

class Participant(object):
   
 
    def __init__(self, name=None, firstname=None, affiliation=None, city=None, 
                 country=None, countryname=None, location=None):
        self.name = name
        self.firstname = firstname
        self.affiliation = affiliation
        self.city = city
        self.country = country
        self.lon = None
        self.lat = None
        self.countryname = None
    
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
                       "Côte d'Ivoire": "Ivory Coast",
                       "Serbia": "Republic of Serbia",
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
        
        while not(lon) and not (lat):

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
                    countryname = location.raw["display_name"].split(",")[-1].strip()
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

        return locationstring

    
    def write_to(self, filename, sep='\t'):
        """
        Write the participants information into a file
        """
        with open(filename, 'a') as f:
            f.write(sep.join((self.name, self.firstname, 
                             self.affiliation, self.countryname,
                             str(self.lat),
                             str(self.lon), "\n"))
                   )
    
    def write_coords_to(self, filename, sep="\t"):
        """
        Write the coordinates in a file
        """
        with open(filename, 'a') as f:
            f.write("[{0}, {1}],\n".format(self.lat, self.lon))
