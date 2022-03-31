'''
Elijah Springs

lab10.py

This program creates a door button that changes color and text when clicked, and exits the window when the
exit button is clicked.

This is my work
'''

# imports
from graphics import *
from button import Button
from door import Door

# window
win = GraphWin("Door & Button", 500, 500)

# rectangle for the button
button_rect = Rectangle(Point(175, 10), Point(425, 120))

# drawing the exit button
exit_button = Button(button_rect, "Exit")
exit_button.draw(win)

# creating the door
door_rect = Rectangle(Point(175, 140), Point(425, 500))
door = Door(door_rect, "Door")
door.open("white", "Open")
door.draw(win)

# loop to check if click lands on exit button, or on the door
mouse_click = win.getMouse()

while not exit_button.is_clicked(mouse_click):
    if door.is_clicked(mouse_click):
        door.close("red", "Closed")

    mouse_click = win.getMouse()
    if door.is_clicked(mouse_click):
        door.open("white", "Open")
    mouse_click = win.getMouse()

    # exits window
win.close()

"""
I didn't know where to submit the classes, so I'll put them here
The Button Class
"""
from graphics import *

class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.label_text = Text(shape.getCenter(), self.label)

    def get_label(self):
        return self.label

    def set_label(self, new_label):
        self.label = new_label

    def draw(self, win):
        self.shape.draw(win)
        self.label_text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label_text.undraw()

    def is_clicked(self, point):
        point_x = point.getX()
        point_y = point.getY()

        shape_p1_x = self.shape.getP1().getX()
        shape_p1_y = self.shape.getP1().getY()
        shape_p2_x = self.shape.getP2().getX()
        shape_p2_y = self.shape.getP2().getY()

        x_true = shape_p1_x < point_x < shape_p2_x
        y_true = shape_p1_y < point_y < shape_p2_y

        if x_true and y_true:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

"""
The Door Class
"""
from graphics import *

class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.label_text = Text(shape.getCenter(), self.label)
        self.secret = False

    def get_label(self):
        return self.label

    def set_label(self, new_label):
        self.label = new_label

    def draw(self, win):
        self.shape.draw(win)
        self.label_text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label_text.undraw()

    def is_clicked(self, point):
        point_x = point.getX()
        point_y = point.getY()

        shape_p1_x = self.shape.getP1().getX()
        shape_p1_y = self.shape.getP1().getY()
        shape_p2_x = self.shape.getP2().getX()
        shape_p2_y = self.shape.getP2().getY()

        x_true = shape_p1_x < point_x < shape_p2_x
        y_true = shape_p1_y < point_y < shape_p2_y

        if x_true and y_true:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.label = label
        self.label_text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.label = label
        self.label_text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        return False

    def set_secret(self, secret):
        self.secret = secret

