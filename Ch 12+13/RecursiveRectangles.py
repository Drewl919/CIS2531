from graphics import *

class RecursiveGraphic(object):
    
    def __init__(self, win: GraphWin):
        self.startWidth = 250
        self.startHeight = 200
        self.tlX = win.getWidth() // 2 - self.startWidth // 2
        self.tlY = win.getHeight() // 2 - self.startHeight // 2

    def drawRectangles(self, win):
        self.drawCenterRectangle(win)
        self.drawUpperLeft(win, self.startWidth, self.startHeight, self.tlX, self.tlY)
        self.drawUpperRight(win, self.startWidth, self.startHeight, self.tlX, self.tlY)
        self.drawLowerLeft(win, self.startWidth, self.startHeight, self.tlX, self.tlY)
        self.drawLowerRight(win, self.startWidth, self.startHeight, self.tlX, self.tlY)
        # Make the initial call to your method(s) here

    def drawCenterRectangle(self, win):
        rect = Rectangle(Point(self.tlX, self.tlY), Point(self.tlX + self.startWidth, self.tlY + self.startHeight))
        rect.setFill("Black")
        rect.draw(win)

    # Create your recursive method(s) here

    def drawUpperLeft(self, win, width, height, xPT, yPT):
        """draws a rect. that is 1/2 the size in the upper left corner"""
        if width >= 2:
            # print(f"UL: {width/2}")
            xPT = xPT
            yPT = yPT
            oppositeXPT = xPT - width/2
            oppositeYPT = yPT - height/2
            rect = Rectangle(Point(xPT, yPT), Point(oppositeXPT, oppositeYPT))
            rect.setFill("Black")
            rect.draw(win)
            self.drawUpperLeft(win, width/2, height/2, oppositeXPT, oppositeYPT)
            self.drawLowerLeft(win, width/2, height/2, oppositeXPT, oppositeYPT)
            self.drawUpperRight(win, width/2, height/2, oppositeXPT, oppositeYPT)

    def drawUpperRight(self, win, width, height, xPT, yPT):
        """draws a rect. that is 1/2 the size in the upper right corner"""
        if width >= 2:
            # print(f"UR: {width / 2}")
            xPT = xPT + width
            yPT = yPT
            oppositeXPT = xPT + width/2
            oppositeYPT = yPT - height/2
            rect = Rectangle(Point(xPT, yPT), Point(oppositeXPT, oppositeYPT))
            rect.setFill("Black")
            rect.draw(win)
            self.drawUpperRight(win, width/2, height/2, xPT, oppositeYPT)
            self.drawLowerRight(win, width/2, height/2, xPT, oppositeYPT)
            self.drawUpperLeft(win, width/2, height/2, xPT, oppositeYPT)

    def drawLowerLeft(self, win, width, height, xPT, yPT):
        """draws a rect. that is 1/2 the size in the lower left corner"""
        if width >= 2:
            # print(f"LL: {width / 2}")
            xPT = xPT
            yPT = yPT + height
            oppositeXPT = xPT - width/2
            oppositeYPT = yPT + height/2
            rect = Rectangle(Point(xPT, yPT), Point(oppositeXPT, oppositeYPT))
            rect.setFill("Black")
            rect.draw(win)
            self.drawLowerLeft(win, width/2, height/2, oppositeXPT, yPT)
            self.drawUpperLeft(win, width/2, height/2, oppositeXPT, yPT)
            self.drawLowerRight(win, width/2, height/2, oppositeXPT, yPT)

    def drawLowerRight(self, win, width, height, xPT, yPT):
        """draws a rect. that is 1/2 the size in the lower right corner"""
        if width >= 2:
            # print(f"LR: {width / 2}")
            xPT = xPT + width
            yPT = yPT + height
            oppositeXPT = xPT + width/2
            oppositeYPT = yPT + height/2
            rect = Rectangle(Point(xPT, yPT), Point(oppositeXPT, oppositeYPT))
            rect.setFill("Black")
            rect.draw(win)
            self.drawLowerRight(win, width/2, height/2, xPT, yPT)
            self.drawUpperRight(win, width/2, height/2, xPT, yPT)
            self.drawLowerLeft(win, width/2, height/2, xPT, yPT)

def main():
    win = GraphWin("Recursive Rectangles", 1000, 650)
    rg = RecursiveGraphic(win)
    rg.drawRectangles(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()