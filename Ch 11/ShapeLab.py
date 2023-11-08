from graphics import *

class Shape:
    def __init__(self, numSides, shapeName, nameAnchor, messageAnchor):
        """Constructor for a shape with with the provided parameters"""
        self.__numSides = numSides
        self.__shapeName = shapeName
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor

    def displayName (self, window):
        """Displays the name of the given shape and shows it at the provided anchor point"""
        name = Text(self.__nameAnchor, self.__shapeName)
        name.draw(window)

    def displayNumSides (self, window):
        """Displays the number of sides for the given shape and shows it at the provided anchor point"""
        sides = Text(self.__messageAnchor, f"A {self.__shapeName} has {self.__numSides} sides")
        sides.draw(window)


class Square(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        """Constructor for a square with the provided parameters and sends them to Shape class"""
        super().__init__("4", "Square", nameAnchor, messageAnchor)

    def drawShape(self, window):
        """Draws a square to win at the indicated points"""
        square = Rectangle(Point(50, 50), Point(250, 250))
        square.setFill("black")
        square.draw(window)


class Ball(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        """Constructor for a ball with the provided parameters and sends them to Shape class"""
        super().__init__("0", "Circle", nameAnchor, messageAnchor)

    def drawShape(self, window):
        """Draws a circle to win at the indicated points with a radius of 100"""
        circle = Circle(Point(450, 150), 100)
        circle.setFill("black")
        circle.draw(window)


class Triangle(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        """Constructor for a triangle with the provided parameters and sends them to Shape class"""
        super().__init__("3", "Triangle", nameAnchor, messageAnchor)

    def drawShape(self, window):
        """Draws a triangle to win at the indicated points"""
        triangle = Polygon(Point(50, 550), Point(250, 550), Point(150, 350))
        triangle.setFill("black")
        triangle.draw(window)


class Octagon(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        """Constructor for a octagon with the provided parameters and sends them to Shape class"""
        super().__init__("8", "Octagon", nameAnchor, messageAnchor)

    def drawShape(self, window):
        """Draws a octagon to win at the indicated points"""
        octagon = Polygon(Point(412.5, 362.5), Point(487.5, 362.5), Point(537.5, 412.5), Point(537.5, 487.5), Point(487.5, 537.5), Point(412.5, 537.5), Point(362.5, 487.5), Point(362.5, 412.5))
        octagon.setFill("black")
        octagon.draw(window)



def main():
    win = GraphWin("Shape Test", 600, 600)
    l1 = Line(Point(300, 0), Point(300, 600))
    l2 = Line(Point(0, 300), Point(600, 300))
    l1.draw(win)
    l2.draw(win)

    shapes = []
    shapes.append(Square(Point(50, 20), Point(100, 280)))
    shapes.append(Ball(Point(350, 20), Point(400, 280)))  # remove comment to test Ball
    shapes.append(Triangle(Point(50, 320), Point(100, 580)))  # remove comment to test Triangle
    shapes.append(Octagon(Point(350, 320), Point(400, 580)))  # remove comment to test Octagon

    for shape in shapes:
        shape.displayName(win)
        shape.displayNumSides(win)
        shape.drawShape(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()




