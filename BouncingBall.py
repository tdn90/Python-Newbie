from graphics import *

def bounce(resolution):
    win = GraphWin("Bouncing Ball", 300, 300)
    win.setCoords(-150,-150,150,150)
    startPos = win.getMouse()
    ball = Circle(Point(startPos.getX(), startPos.getY()), 5)
    ball.setFill("red");
    ball.draw(win)    

    speedPos = win.getMouse()
    dx = (speedPos.getX() - startPos.getX())
    dy = (speedPos.getY() - startPos.getY())

    for i in range(900):
        for j in range(resolution):
            currentCenter = ball.getCenter()
            newX = currentCenter.getX() + (dx / resolution)
            newY = currentCenter.getY() + (dy / resolution)
            time.sleep(1/15)
            ball.undraw()
            ball = Circle(Point(newX, newY), 5)
            ball.setFill("red")
            ball.draw(win)
            if (newX + 5 > 150 or newX - 5 < -150):
                dx = -dx
            if (newY + 5 > 150 or newY - 5 < -150):
                dy = -dy
