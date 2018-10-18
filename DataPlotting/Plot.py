from graphics import *
from Map import *
from Filter import *

def createBox(win, width=707, height=744):
    topLeft = Point(width-200, 280)
    bottomRight = Point(width, 0)
    box = Rectangle(topLeft, bottomRight)
    box.setFill('white')
    box.draw(win)

def annotation(win, width=707, height=744):
    createBox(win)
    options = {'violet': "< $100,000",
               'indigo': "$100,000–200,000",
               'blue': "$200,000–300,000",
               'green': "$300,000-400,000",
               'yellow': "$400,000–500,000",
               'orange': "$500,000-600,000",
               'red': ">$600,000"}
    Text(Point(width-200 + 100, 280 - 30), "Real Estate Price").draw(win)
    x_colorCircle = width-200 + 30
    x_text = width - 200 + 30 + 90
    y = 280 - 70
    for color, text in options.items():
        c = Circle(Point(x_colorCircle, y), 5)
        c.setFill(color)
        annot = Text(Point(x_text, y), text)
        c.draw(win)
        annot.draw(win)
        y -= 30

def plotDataOnMap(fileName, centerLong, centerLat, distance, win):
    filteredEntries = filter(fileName, centerLong, centerLat, distance)
    for row in filteredEntries:
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        price = int(row['price'])
        color = getRealEstateColor(price)
        plotCircle(win, latitude, longitude, color)
    annotation(win)
        
    
        
