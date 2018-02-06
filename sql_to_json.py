"""
SQL to JSON Conversion
Written by: Heba El-Shimy
F21BD - Big Data Management Coursework 1
"""

# Import supporting libraries
import simplejson

from sqlobject import *
import yaml

# Import configuration file with database connection variables
with open("databaseconfig.yml", 'r') as configfile:
    cfg = yaml.load(configfile)

connection_string = 'mysql://{}:{}@{}/{}'.format(cfg['mysql']['user'],
                                                cfg['mysql']['passwd'],
                                                cfg['mysql']['host'],
                                                cfg['mysql']['db'])

# Establish a connection with mysql server
try:
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection
# Handle errors in creating the connection  
except ValueError as error:
    print(error)

# Automatically extract database schema and define the columns and their types for missing/unrecognized ones
class Airline(SQLObject):
    class sqlmeta:
        table = 'airlines'
        idName = 'alid'
        fromDatabase = True

class Airport(SQLObject):
    class sqlmeta:
        table = 'airports'
        idName = 'apid'
        fromDatabase = True

class Route(SQLObject):
    class sqlmeta:
        table = 'routes'
        idName = 'rid'
        fromDatabase = True
    
    alid = IntCol(length=11)
    src_ap = StringCol(length=4, varchar=True)
    src_apid = IntCol(length=11)
    dst_ap = StringCol(length=4, varchar=True)
    dst_apid = IntCol(length=11)
    codeshare = StringCol()
    stops = StringCol()
    equipment = StringCol()
    rid = IntCol(length=11)

class Country(SQLObject):
    class sqlmeta:
        table = 'countries'
        idName = 'code'
        idType = str
        fromDatabase = True

    code = StringCol(length=2, varchar=True)
    name = StringCol()
    oa_code = StringCol(length=2, varchar=True)
    dst = StringCol(length=1, varchar=False)

class City(SQLObject):
    class sqlmeta:
        table = 'cities'
        idName = 'cid'
        fromDatabase = True

    tz_id = StringCol()


def export_db_to_json():
    """
    A function that loads all SQL database and feeds them into dictionaries
    in preparation for exporting them to json files.
    """

    # Load all tables
    all_airlines = Airline.select()
    all_airports = Airport.select()
    all_routes = Route.select()
    all_countries = Country.select()
    all_cities = City.select()
    
    # Define empty dictionaries to hold data
    airlines_dict = []
    airports_dict = []
    routes_dict = []
    countries_dict = []
    cities_dict = []

    # Loop through all table data row-by-row and extract data, then feed
    # into dictionary with relevant keys
    for airport in all_airports:
        airport_dict = {
            'apid': airport.id,
            'name': airport.name,
            'city': airport.city,
            'iata': airport.iata,
            'icao': airport.icao,
            'x': airport.x,
            'y': airport.y,
            'elevation': airport.elevation
        }
        airports_dict.append(airport_dict)

    for airline in all_airlines:
        airline_dict = {
            'alid': airline.id,
            'name': airline.name,
            'iata': airline.iata,
            'icao': airline.icao,
            'callsign': airline.callsign,
            'country': airline.country,
            'alias': airline.alias,
            'mode': airline.mode,
            'active': airline.active
        }
        airlines_dict.append(airline_dict)
    
    for route in all_routes:
        route_dict = {
            'rid': route.id,
            'alid': route.alid,
            'src_ap': route.src_ap,
            'src_apid': route.src_apid,
            'dst_ap': route.dst_ap,
            'dst_apid': route.dst_apid,
            'codeshare': route.codeshare,
            'stops': route.stops,
            'equipment': route.equipment
        }
        routes_dict.append(route_dict)

    for country in all_countries:
        country_dict = {
            'code': country.code,
            'name': country.name,
            'oa_code': country.oa_code,
            'dst': country.dst
        }
        countries_dict.append(country_dict)
    
    for city in all_cities:
        city_dict = {
            'cid': city.id,
            'name': city.name,
            'country': city.country,
            'timezone': city.timezone,
            'tz_id': city.tz_id
        }
        cities_dict.append(city_dict)

    # Create empty files to write data from dictionaries
    # resulting files are in json format
    with open('airlines.json', 'a') as col1:
        col1.write(simplejson.dumps(airlines_dict))

    with open('airports.json', 'a') as col2:
        col2.write(simplejson.dumps(airports_dict))

    with open('routes.json', 'a') as col3:
        col3.write(simplejson.dumps(routes_dict))

    with open('countries.json', 'a') as col4:
        col4.write(simplejson.dumps(countries_dict))

    with open('cities.json', 'a') as col5:
        col5.write(simplejson.dumps(cities_dict))

# Start the program
if __name__ == "__main__":
    export_db_to_json()