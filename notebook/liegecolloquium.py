class Participant(object):
   
 
    def __init__(self, name=None, firstname=None, affiliation=None, city=None, 
                 country=None, location=None):
        self.name = name
        self.firstname = firstname
        self.affiliation = affiliation
        self.city = city
        self.country = country
    
    def __repr__(self):
        return str(self.__dict__)
        
    def replace_country(self):
        dictcountry = {"U.S.A.": "United States of America", 
                       "The Netherlands": "Nederland"}
        for k, v in dictcountry.items():
            self.country = self.country.replace(k, v)
            
    def get_location(self):
        # Try with different combinations of affil., city, country
        locationstring = ", ".join((self.affiliation, self.city, self.country))
        location = geolocator.geocode(locationstring)
        if not(location):
            locationstring = ", ".join((self.city, self.country))
            location = geolocator.geocode(locationstring)
            
        self.location = location
        return locationstring
    
    def write_to(self, filename, sep='\t'):
        """
        Write the participants information into a file
        """
        with open(filename, 'a') as f:
            f.write(sep.join((self.name, self.firstname, 
                             self.affiliation, self.country,
                             str(self.location.latitude),
                             str(self.location.longitude), "\n"))
                   )
    
    def write_coords_to(self, filename, sep="\t"):
        """
        Write the coordinates in a file
        """
        with open(filename, 'a') as f:
            f.write("[{0}, {1}],\n".format(self.location.latitude,
                                               self.location.longitude)) 
