"""
Elijah Springs

lab8.py

This program creates a bumper car esque simulation.

This is my work.
"""

# imports
from random import randint
from graphics import *
from math import *

# the main function
def bumper():

    # window
    win = GraphWin("Bumper Cars", 500, 500)

    # random point for the circles
    random_point = Point(randint(15, 485), randint(15, 485))

    # the circles
    circle_ball = Circle(random_point, 15)
    circle_ball_2 = Circle(random_point, 15)

    # creating the color of the circles
    ball_one_color = get_random_color()
    ball_two_color = get_random_color()

    # setting the color of the circles
    circle_ball.setFill(ball_one_color)
    circle_ball_2.setFill(ball_two_color)

    # creating the speed of each circle
    ball_one_speed = get_random(20)
    ball_two_speed = get_random(20)

    # drawing each of the circles
    circle_ball.draw(win)
    circle_ball_2.draw(win)

    # storing the speed in separate x and y values for each circle
    ball_x_speed = ball_one_speed
    ball_y_speed = ball_one_speed
    ball_2_x_speed = ball_two_speed
    ball_2_y_speed = ball_two_speed


    # the while loop
    while 1 > 0:

        # moving the circles
        circle_ball.move(ball_x_speed, ball_y_speed)
        circle_ball_2.move(ball_2_x_speed, ball_2_y_speed)

        # if the ball hits the top or bottom
        if hit_vertical(circle_ball, win):
            ball_y_speed = ball_y_speed * -1

        # if the ball hits the sides
        if hit_horizontal(circle_ball, win):
            ball_x_speed = ball_x_speed * -1

        # if the other ball hits the top or bottom
        if hit_vertical(circle_ball_2, win):
            ball_2_y_speed = ball_2_y_speed * -1

        # if the other ball hits the sides
        if hit_horizontal(circle_ball_2, win):
            ball_2_x_speed = ball_2_x_speed * -1

        # if the balls collide
        if did_collide(circle_ball, circle_ball_2):
            ball_x_speed = ball_x_speed * -1
            ball_y_speed = ball_y_speed * -1
            ball_2_y_speed = ball_y_speed * -1
            ball_2_x_speed = ball_x_speed * -1

        # checking for a mouse click
        if win.checkMouse():
            win.close()

        # the move rate
        time.sleep(.1)

# random number function
def get_random(move_amount):
    random_num = randint(-1 * move_amount, move_amount)
    return random_num

# a function for when the balls collide
def did_collide(ball, ball_2):
    ball_x = ball.getCenter().getX()
    ball_y = ball.getCenter().getY()
    ball_2_x = ball_2.getCenter().getX()
    ball_2_y = ball_2.getCenter().getY()
    distance = sqrt(((ball_2_x - ball_x) ** 2) + ((ball_2_y - ball_y) ** 2))
    while distance > 15:
        return False
    return True

# if the balls hit the top or bottom, it bounces
def hit_vertical(ball, win):
    if ((ball.getCenter().getY() - 15) < 0) or ((ball.getCenter().getY() + 15) > win.getHeight()):
        return True
    return False

# if the balls hit the sides, it bounces
def hit_horizontal(ball, win):
    if ((ball.getCenter().getX() - 15) < 0) or ((ball.getCenter().getX() + 15) > win.getWidth()):
        return True
    return False

# generates a random color for the circles
def get_random_color():
    random_color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return random_color

