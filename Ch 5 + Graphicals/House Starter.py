##Program: House Functions
##Name: Andrew Musielak
## Date: 07/5/2021
# Creates a customizable house in a display window
#-------------------------------------------------------------#

##Imports
from graphics import *

##Global Variables
win = GraphWin("My House", 1000, 650)

##User Defined Functions - Place your drawing functions below
def drawBackground():
    """draws the background"""
    sky = Rectangle(Point(0,0), Point(1000, 400))
    sky.setFill(color_rgb(145, 232, 250))
    ground = Rectangle(Point(0, 400), Point(1000, 650))
    path1 = Rectangle(Point(400, 550), Point(450, 650))
    path2 = Rectangle(Point(687.5, 400), Point(887.5, 650))
    ground.setFill((color_rgb(5, 158, 10)))
    sun = Circle(Point(850, 100), 75)
    sun.setFill(color_rgb(251, 255, 0))
    path1.setFill(color_rgb(140, 140, 140))
    path2.setFill(color_rgb(140, 140, 140))
    sky.draw(win)
    ground.draw(win)
    sun.draw(win)
    path1.draw(win)
    path2.draw(win)

def drawOutline(x1, y1, x2, y2):
    """draws the outline of the house & garage"""
    yPos = y1 + 20
    house = Rectangle(Point(x1, y1), Point(x2, y2))
    house.setFill(color_rgb(193, 201, 230))
    house.draw(win)
    while y2 > yPos:
        line = Line(Point(x1, yPos), Point(x2, yPos))
        line.setOutline(color_rgb(175, 178, 186))
        line.draw(win)
        yPos = yPos + 20

def drawRoof(x1, y1, x2, y2, x3, y3):
    """draws the roof for main house & garage"""
    roof = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    roof.setFill(color_rgb(189, 153, 115))
    roof.draw(win)

def drawDoor(doorColor):
    """draws fornt door with handle"""
    color = doorColor
    if color == "brown":
        color = "DarkGoldenrod4"
    elif color == "black":
        color = "black"
    elif color == "blue":
        color = "dark blue"
    elif color == "red":
        color = "brown"
    elif color == "tan":
        color = "tan"
    door = RoundedRectangle(Point(400, 450), Point(450, 550))
    knob = Circle(Point(440, 500), 3)
    door.setFill(color)
    knob.setFill("yellow")
    knob.setWidth(2)
    door.draw(win)
    knob.draw(win)

def drawWindows(x1, y1, x2, y2):
    """draws windows with crossed lines"""
    window = Rectangle(Point(x1, y1), Point(x2, y2))
    window.setFill(color_rgb(102, 176, 255))
    window.setWidth(3)
    window.draw(win)
    line1 = Line(Point(x1, (y1+y2)/2), Point(x2, (y1+y2)/2))
    line2 = Line(Point((x1+x2)/2, y1), Point((x1+x2)/2, y2))
    line1.setWidth(3)
    line2.setWidth(3)
    line1.setFill(color_rgb(20, 28, 36))
    line2.setFill(color_rgb(20, 28, 36))
    line1.draw(win)
    line2.draw(win)

def drawChimney():
    """draws chimney and stack"""
    chimney = Rectangle(Point(562.5, 100), Point(600, 150))
    shaft = Rectangle(Point(572, 92), Point(590, 100))
    top = Rectangle(Point(570, 87), Point(592.5, 92))
    chimney.setFill(color_rgb(179, 87, 87))
    shaft.setFill(color_rgb(0, 0, 0))
    top.setFill(color_rgb(0, 0, 0))
    chimney.draw(win)
    shaft.draw(win)
    top.draw(win)

def drawGarage(garageColor):
    """draws garage with a window & lines on window & garage"""
    color = garageColor
    if color == "brown":
        color = "DarkGoldenrod4"
    elif color == "black":
        color = "black"
    elif color == "blue":
        color = "dark blue"
    elif color == "red":
        color = "brown"
    elif color == "tan":
        color = "tan"
    garage = Rectangle(Point(687.5, 400), Point(887.5, 550))
    garage.setFill(color)
    garage.draw(win)
    window = Rectangle(Point(695, 415), Point(880, 435))
    window.setFill(color_rgb(102, 176, 255))
    window.setWidth(3)
    window.draw(win)
    count = 0
    point = 695 + 46.25
    while count < 3:
        line = Line(Point(point, 415), Point(point, 435))
        line.setWidth(3)
        line.setFill(color_rgb(20, 28, 36))
        line.draw(win)
        point += 46.25
        count += 1
    count = 0
    point = 450
    while count < 4:
        line = Line(Point(687.5, point), Point(887.5, point))
        line.setWidth(3)
        line.setFill(color_rgb(92, 89, 87))
        line.draw(win)
        point += 25
        count += 1



#Main Function
def main(): 
    win.setBackground("white")
    ##put your function calls here for your drawing
    colors = ("blue", "brown", "red", "black", "tan")
    print("Colors: blue, brown, red, black, or tan.")
    doorColor = input("Please enter the color you would like for the door: ")
    while doorColor not in colors:
        doorColor = input("Please enter the color you would like for the door: ")
    garageColor = input("Please enter the color you would like for the garage: ")
    while garageColor not in colors:
        garageColor = input("Please enter the color you would like for the garage: ")

    drawBackground()
    drawOutline(275, 350, 600, 550)
    drawOutline(400, 150, 600, 350)
    drawOutline(675, 375, 900, 550)
    drawChimney()
    drawRoof(400, 275, 260, 350, 400, 350)
    drawRoof(385, 150, 500, 75, 615, 150)
    drawRoof(660, 375, 777.5, 300, 915, 375)
    drawDoor(doorColor)
    drawWindows(300, 425, 375, 500)
    drawWindows(475, 425, 575, 500)
    drawWindows(412.5, 200, 487.5, 275)
    drawWindows(512.5, 200, 587.5, 275)
    drawGarage(garageColor)


    win.getMouse()#wait for mouse click before closing
    win.close()


##Call To The Main
main()





