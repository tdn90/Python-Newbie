from Map import *
from Plot import *
from Filter import *
from ReportGenerator import *

def PixelsToLatLong(x, y, width=707, height=744, latMin=38.24, latMax=39.03, longMin=-121.56, longMax=-120.6):
    # latitude would be y
    # longitude would be x
    x_ratio = width / (longMax - longMin)
    y_ratio = height / (latMax - latMin)
    longitude= x / x_ratio + longMin
    latitude = y / y_ratio + latMin
    return latitude, longitude

def main():
    win = initializeMap()
    centerPoint = win.getMouse()
    x_coord = centerPoint.getX()
    y_coord = centerPoint.getY()
    centerLat, centerLong = PixelsToLatLong(x_coord, y_coord)
    
    rearPoint = win.getMouse()
    rear_x = rearPoint.getX()
    rear_y = rearPoint.getY()
    rearLat, rearLong = PixelsToLatLong(rear_x, rear_y)
    fileName = 'SacramentoMap.gif'

    distance = distanceMiles(centerLat, centerLong, rearLat, rearLong)
    plotDataOnMap('SacramentoRealEstateTransactions.csv', centerLong, centerLat, distance, win)
    report('SacramentoRealEstateTransactions.csv', centerLong, centerLat, distance)
    
    
    
    
    
