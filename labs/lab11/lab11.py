"""
Elijah Springs

lab11.py

This creates a three door game in a graphics window, where if the user clicks the secret door, they win.

This is my work.
"""

# imports
from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint

def main():

    # window
    win = GraphWin("Three Door Game", 800, 500)

    # shapes for doors, buttons, and scores
    door_one_shape = Rectangle(Point(50, 275), Point(250, 500))
    door_two_shape = Rectangle(Point(300, 275), Point(500, 500))
    door_three_shape = Rectangle(Point(550, 275), Point(750, 500))
    quit_button_shape = Rectangle(Point(550, 50, ), Point(750, 150))
    score_shape = Rectangle(Point(50, 50), Point(250, 150))

    # creating door and button classes, as well as instruction text
    door_one = Door(door_one_shape, "Door 1")
    door_two = Door(door_two_shape, "Door 2")
    door_three = Door(door_three_shape, "Door 3")
    quit_button = Button(quit_button_shape, "Quit")
    instructions = Text(Point(400, 260), "Click a door")

    # drawing doors and buttons
    door_one.draw(win)
    door_two.draw(win)
    door_three.draw(win)
    quit_button.draw(win)
    instructions.draw(win)
    score_shape.draw(win)

    # for the score box
    wins = 0
    wins_sign = Text(Point(75, 75), "Wins")
    wins_sign.draw(win)
    wins_text = Text(Point(75, 125), wins)
    wins_text.draw(win)
    losses = 0
    losses_sign = Text(Point(225, 75), "Losses")
    losses_sign.draw(win)
    losses_text = Text(Point(225, 125), losses)
    losses_text.draw(win)

    # setting the user click
    user_click = Point(0, 0)

    # while quit button is not clicked
    while not quit_button.is_clicked(user_click):

        # resets
        instructions.setText("Click a door")
        door_one.set_secret(False)
        door_two.set_secret(False)
        door_three.set_secret(False)
        door_one.color_door("blue")
        door_two.color_door("blue")
        door_three.color_door("blue")

        # creating a random secret door
        list_of_doors = [door_one, door_two, door_three]
        random_door_num = randint(0, 2)
        random_door = list_of_doors[random_door_num]
        random_door.set_secret(True)

        # user click
        user_click = win.getMouse()

        # if statements (if door is clicked and is secret, if door is clicked and is not secret)
        if door_one.is_clicked(user_click) and door_one.is_secret():
            door_one.color_door("green")
            instructions.setText("You win! Click to play again")
            wins = wins + 1
            wins_text.setText(wins)

        elif door_one.is_clicked(user_click) and not door_one.is_secret():
            door_one.color_door("red")
            random_door.color_door("green")
            instructions.setText("You lost, click to play again")
            losses = losses + 1
            losses_text.setText(losses)

        elif door_two.is_clicked(user_click) and door_two.is_secret():
            door_two.color_door("green")
            instructions.setText("You win! Click to play again")
            wins = wins + 1
            wins_text.setText(wins)

        elif door_two.is_clicked(user_click) and not door_two.is_secret():
            door_two.color_door("red")
            random_door.color_door("green")
            instructions.setText("You lost, click to play again")
            losses = losses + 1
            losses_text.setText(losses)

        elif door_three.is_clicked(user_click) and door_three.is_secret():
            door_three.color_door("green")
            instructions.setText("You win! Click to play again")
            wins = wins + 1
            wins_text.setText(wins)

        elif door_three.is_clicked(user_click) and not door_three.is_secret():
            door_three.color_door("red")
            random_door.color_door("green")
            instructions.setText("You lost, click to play again")
            losses = losses + 1
            losses_text.setText(losses)

        user_click = win.getMouse()

    # close window when quit button is clicked
    win.close()
