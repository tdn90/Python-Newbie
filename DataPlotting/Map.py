from graphics import *

def initializeMap(mapFile='SacramentoMap.gif', latMin=38.24, latMax=39.03, longMin=-121.56, longMax=-120.6):
    # Turn the mapFile into an image to get its width and height in pixels
    image = Image(Point(0,0), mapFile)
    width = image.getWidth()
    height = image.getHeight()

    # Create a window just large enough to hold the image
    win = GraphWin('Sacramento Area', width, height)
    win.setCoords(0, 0, width, height)
    center = Point(width/2, height/2)
    image = Image(center, mapFile)
    image.draw(win)
    return win

def LatLongToPixels(latitude, longitude, width=707, height=744, latMin=38.24, latMax=39.03, longMin=-121.56, longMax=-120.6):
    # latitude would be y
    # longitude would be x
    x_ratio = width / (longMax - longMin)
    y_ratio = height / (latMax - latMin)
    x = (longitude - longMin) * x_ratio
    y = (latitude - latMin) * y_ratio
    return x,y

def getRealEstateColor(price):
    options = {0: 'violet',
               1: 'indigo',
               2: 'blue',
               3: 'green',
               4: 'yellow',
               5: 'orange',
               6: 'red'}
    minPrice = 100000
    for i in range(6):
        if (price < minPrice):
            return options[i]
        else:
            minPrice += 100000
    return options[6]
    
def plotCircle(win, lat, long, color):
    x,y = LatLongToPixels(lat, long)
    c = Circle(Point(x,y), 5)
    c.setFill(color)
    c.draw(win)


