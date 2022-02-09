'''
Elijah Springs

lab4.py

This program displays an animation in a window to celebrate Valentine's Day.

This is my work.
'''
import time
from graphics import Point, GraphWin, Polygon, Line, Rectangle, Text

def greeting_card():

    # window
    window = GraphWin("Greeting Card", 700, 700)
    window.setCoords(0, 0, 10, 10)

    # this is the pink background
    background = Rectangle(Point(0, 10), Point(10, 0))
    background.setFill("pink")
    background.draw(window)

    # this is the left side of the heart
    heart_left = Polygon(Point(3, 8), Point(2, 7.125), Point(1.25, 6), Point(5, 2), Point(5, 6.75))
    heart_left.setOutline("red")
    heart_left.setFill('red')
    heart_left.setWidth(3)
    heart_left.draw(window)

    # this is the arrow
    arrow = Line(Point(-1.75, 5), Point(0, 5))
    arrow.setArrow("last")
    arrow.setWidth(15)
    arrow.draw(window)

    # this is the right side of the heart, drawn after the arrow so it appears the arrow is going through the heart
    heart_right = Polygon(Point(5, 2), Point(8.75, 6), Point(8, 7.125), Point(7, 8), Point(5, 6.75))
    heart_right.setOutline("red")
    heart_right.setFill("red")
    heart_right.setWidth(3)
    heart_right.draw(window)

    # the loop the make the arrow move
    for i in range(50):
        arrow.move(.25,0)
        time.sleep(.1)

    # the displayed message
    click_message = Text(Point(5, 1), "Click to close")
    click_message.draw(window)

    # the function to close the window
    window.getMouse()
    window.close()
greeting_card()