"""
Name: Elijah Springs
hw4.py

Problem: This code creates 5 seperate squares depending on where the user clicks, finds the perimeter and area of a
rectangle which size depends on the users clicked coordinates, and finds the radius of a circle which size depends
on the users clicked coordinates. I sadly could not figure out the pie2 function.

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can draw squares
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw more squares")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to draw more squares
    for i in range(num_clicks):
        shape_clone = shape.clone()
        shape_clone.draw(win)
        click = win.getMouse()
        center = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

# Closing text
    close_text = Text(Point(width / 2, height - 20), "Click again to close")
    close_text.draw(win)

    win.getMouse()
    win.close()


def rectangle():
# creation of the window and instruction text
    rectangle_win = GraphWin("Rectangle", 500, 500)
    text = Text(Point(250,450), "Click for the top left corner")
    text.draw(rectangle_win)
# storing the clicks
    click_one = rectangle_win.getMouse()
    text.setText("Click for the bottom right corner")
    click_two = rectangle_win.getMouse()
# creating the rectangle
    rect = Rectangle(Point(click_one.getX(), click_one.getY()), Point(click_two.getX(), click_two.getY()))
    rect.setFill("green")
    rect.draw(rectangle_win)
# calculating the perimiter and area
    perimiter = (((click_two.getX() - click_one.getX()) + (click_two.getY() - click_one.getY())) * 2)
    area = ((click_two.getX() - click_one.getX()) * (click_two.getY() - click_one.getY()))

# creating new text
    text.undraw()
    perimiter_text = Text(Point(250, 400), "Perimiter: " + str(perimiter))
    area_text = Text(Point(250, 425), "Area: " + str(area))
    perimiter_text.draw(rectangle_win)
    area_text.draw(rectangle_win)

# creating the close text
    close_text = Text( Point(250, 450), "Click again to close")
    close_text.draw(rectangle_win)
    rectangle_win.getMouse()
    rectangle_win.close()



def circle():
# creation of graphics window
    circle_win = GraphWin("Radius", 500, 500)

# the instruction text
    circle_text = Text(Point(250, 450), "Click for the center of the circle")
    circle_text.draw(circle_win)

# storing mouse click data
    center_click = circle_win.getMouse()
    center_x = center_click.getX()
    center_y = center_click.getY()

    circle_text.setText("Click for the width of the circle")
    circumf_click = circle_win.getMouse()
    circumf_x = circumf_click.getX()
    circumf_y = circumf_click.getY()

# calculating the radius
    radius = math.sqrt(((circumf_x - center_x) ** 2) + ((circumf_y - center_y) ** 2))

# drawing the circle
    the_circle = Circle(Point(center_x, center_y), radius)
    the_circle.setFill("blue")
    the_circle.draw(circle_win)

# printing the radius and closing text
    radius_text = Text(Point(250, 425), "Radius: " + str(radius))
    radius_text.draw(circle_win)

    circle_text.setText("Click again to close")
    circle_win.getMouse()
    circle_win.close()

def pi2():
    pass


if __name__ == '__main__':
    pass
