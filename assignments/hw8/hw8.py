"""
Name: Elijah Springs
hw8.py

Problem: This program creates a list of sum of sqares originally formatted in a string, and outputs if user inputted circles overlap.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def add_ten(nums):
    newnums = []
    for i in range(len(nums)):
        newnums.append(nums[i] + 10)
    return None


def square_each(nums):
    newnumssquared = []
    for i in range(len(nums)):
        newnumssquared.append(nums[i] ** 2)
    return newnumssquared


def sum_list(nums):
    number = 0
    for i in range(len(nums)):
        number = number + int(nums[i])
    return number



def to_numbers(nums):
    newnums = []
    for i in range(len(nums)):
        newnums.append(int(nums[i]))
    return newnums


def sum_of_squares(nums):
    sos_list_accumulator = []
    for i in range(len(nums)):
        accumulator = []

        indexer = nums[i]

        for j in indexer.split(", "):
            accumulator.append(j)

        accumulator = to_numbers(accumulator)
        accumulator = square_each(accumulator)
        accumulator = sum_list(accumulator)

        sos_list_accumulator.append(accumulator)

    return sos_list_accumulator


def starter(weight, wins):
    if weight > 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 and wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year / 400 == int:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_two.getX()) ** 2 + (center_two.getY() - circumference_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)


    if did_overlap(circle_one, circle_two):
        text = Text(Point(5, 1), "Circles did overlap")
        text.draw(win)
    else:
        text = Text(Point(5, 1), "Circles did not overlap")
        text.draw(win)

    close_text = Text(Point(5, 0.5), "Click again to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

def did_overlap(circle_one, circle_two):
    c1_x = circle_one.getCenter().getX()
    c1_y = circle_one.getCenter().getY()
    c2_x = circle_two.getCenter().getX()
    c2_y = circle_two.getCenter().getY()

    distance = math.sqrt(((c2_x - c1_x) ** 2) + ((c2_y - c1_y) ** 2))

    c1_radius = circle_one.getRadius()
    c2_radius = circle_two.getRadius()

    if (c1_radius + c2_radius) > distance:
        return True
    return False



if __name__ == '__main__':
    pass
