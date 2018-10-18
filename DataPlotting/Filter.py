import math
import csv

# http://www.movable-type.co.uk/scripts/latlong.html
def toRad(x):
    """Convert given numeric degrees into radians"""
    return x*math.pi/180.0;

def distanceMiles(lat1, long1, lat2, long2):
    """ Uses Haversine formula to calculate the greatcircle
    distance between two points on the earth's
    surface expressed in (lat,long) coordinates """
    R = 3958.7558657440545 # Mean radius of Earth in miles
    dLat = toRad(lat2-lat1)
    dLon = toRad(long2-long1)
    lat1 = toRad(lat1)
    lat2 = toRad(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
    math.sin(dLon/2) * math.sin(dLon/2) * \
    math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return (d)

def filter(fileName, centerLong, centerLat, distance):
    file = open(fileName, 'r')
    dRdr = csv.DictReader(file)
    filteredEntries = []
    for row in dRdr:
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        if (distanceMiles(centerLat, centerLong, latitude, longitude) <= distance):
            filteredEntries.append(row)
    file.close()
    return filteredEntries
