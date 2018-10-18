import numpy as np
from Filter import *

def gatherData(fileName, long, lat, distance):
    filteredEntries = filter(fileName, long, lat, distance)
    priceList = []
    bedList = []
    bathList = []
    for row in filteredEntries:
        priceList.append(int(row['price']))
        bedList.append(int(row['beds']))
        bathList.append(int(row['baths']))
    return priceList, bedList, bathList

def outputToFile(output, lat, long, distance, minPrice, maxPrice, meanPrice, medianPrice, meanBeds, meanBaths):
    f = open(output, "w")
    f.write("-------------------REPORT---------------------\n");
    f.write("Latitude: {}\nLongitude: {}\nDistance from center point: {}\n".format(lat, long, distance))
    f.write("Minimum selling price: {}\n".format(minPrice))
    f.write("Maximum selling price: {}\n".format(maxPrice))
    f.write("Mean selling price: {}\n".format(meanPrice))
    f.write("Median selling price: {}\n".format(medianPrice))
    f.write("Mean number of bedrooms: {}\n".format(meanBeds))
    f.write("Mean number of bathrooms: {}\n".format(meanBaths))
    f.close()

def report(fileName, long, lat, distance, output='report.txt'):
    priceList, bedList, bathList = gatherData(fileName, long, lat, distance)
    if (len(priceList) == 0):
        outputToFile(output,0,0,0,0,0,0,0,0,0)
    else:   
        minPrice = min(priceList)
        maxPrice = max(priceList)
        meanPrice = np.mean(priceList)
        medianPrice = np.median(priceList)
        meanBeds = np.mean(bedList)
        meanBaths = np.mean(bathList)
        outputToFile(output, lat, long, distance, minPrice, maxPrice, meanPrice, medianPrice, meanBeds, meanBaths)
    
    
    
    
    
    
    
        
    
