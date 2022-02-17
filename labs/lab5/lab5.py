'''
Elijah Springs

lab5.py



This is my work.
'''

from graphics import *
from math import *

from graphics import Point


def triangle():
    #window and instruction text
    win = GraphWin("Triangle", 500, 500)
    text = Text(Point(250, 400), "Click 3 times anywhere")
    text.draw(win)

    # storing the clicks in variables
    click_one = win.getMouse()
    click_two = win.getMouse()
    click_three = win.getMouse()

    # the triangle
    tri = Polygon(click_one, click_two, click_three)
    tri.setFill("green")
    tri.draw(win)

    # calculating the lengths
    length_one = sqrt((abs(click_two.getX() - click_one.getX()) ** 2) + (abs(click_two.getY() - click_one.getY()) ** 2))
    length_two = sqrt((abs(click_three.getX() - click_two.getX()) ** 2) + (abs(click_three.getY() - click_two.getY()) ** 2))
    length_three = sqrt((abs(click_one.getX() - click_three.getX()) ** 2) + (abs(click_one.getY() - click_three.getY()) ** 2))

    # calculating the perimeters
    perimiter = length_one + length_two + length_three

    # calculating the area
    area_variable = perimiter / 2
    area = sqrt(area_variable * (area_variable - length_one) * (area_variable - length_two) * (area_variable - length_three))

    # printing the results
    text.setText("Click again to close")
    area_text = Text(Point(250, 425), "Area: " + str(area))
    area_text.draw(win)
    perim_text = Text(Point(250, 450), "Perimiter: " + str(perimiter))
    perim_text.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_entry = Entry(Point(win_width / 2 + 20, win_height / 2 + 40), 5)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_entry = Entry(Point(win_width / 2 + 20, win_height / 2 + 70), 5)
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_entry = Entry(Point(win_width / 2 + 20, win_height / 2 + 100), 5)
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)

    # the loop
    for i in range(5):
        win.getMouse()
        red = eval(red_entry.getText())
        blue = eval(blue_entry.getText())
        green = eval(green_entry.getText())
        shape.setFill(color_rgb(red, green, blue))

    inst.setText("All done!, Click again to close window")


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    #input
    user_string = input("Enter any word: ")

    #first letter
    first_letter = user_string[0]
    print(first_letter)

    #last letter
    length = len(user_string)
    last_letter = user_string[length - 1]
    print(last_letter)

    #characters in the 2 -  5 positions
    two_to_five = user_string[1:5]
    print(two_to_five)

    # first and last letter
    first_last = first_letter + last_letter
    print(first_last)

    # first three letters ten times
    first_three = user_string[0:3]
    print(first_three * 10)

    #prints every letter individually
    for letter in user_string:
        print(letter)

    #total number of letters
    num_of_letters = len(user_string)
    print(num_of_letters)

def process_list():
    # variables
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    # hithere
    x = values[1]
    x = x + values[3]
    print(x)

    # 5 + 2.5
    x = values[0]
    x = x + values[2]
    print(x)

    # hihihihihi
    x = values[1]
    print(x * 5)

    # 2.5, there, pt
    x = values[2:5]
    print(x)

    # 2.5, there, 5
    x = values[2:4]
    five = values[0]
    x = x + [five]
    print(x)

    # 2.5, there, 7.2
    x = values[2:4]
    sevenpointtwo = float(values[5])
    x = x + [sevenpointtwo]
    print(x)

    # add all numbers
    x = values[0]
    x = x + values[2]
    x = x + float(values[5])
    print(x)

    # number of all objects in list
    x = len(values)
    print(x)


def another_series():
    #couldn't quite figure this one out :(
    pass






def target():
    win = GraphWin("Target", 500, 500)
    center = Point(250,250)

    white_circ = Circle(center, 250)
    white_circ.setFill("white")
    white_circ.draw(win)

    black_circ = Circle(center, 200)
    black_circ.setFill("black")
    black_circ.draw(win)

    blue_circ = Circle(center, 150)
    blue_circ.setFill("blue")
    blue_circ.draw(win)

    red_circ = Circle(center, 100)
    red_circ.setFill("red")
    red_circ.draw(win)

    yellow_circ = Circle(center, 50)
    yellow_circ.setFill("yellow")
    yellow_circ.draw(win)

    win.getMouse()
    win.close()