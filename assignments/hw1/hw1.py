"""
Name: Elijah Springs
hw1.py

Problem: This program solves problems such as evaluating area and volume, evaluating a basketball players
shooting percentage, the total cost of coffee, and converting kilometers to miles.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    v_length = eval(input("Enter the length: "))
    v_width = eval(input("Enter the width: "))
    v_height = eval(input("Enter the height: "))
    volume = v_length * v_width * v_height
    print("The volume is: ", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the total amount of shots the player took: "))
    total_shots_made = eval(input("Enter the total amount of shots the player made: "))
    make_percentage = (total_shots_made / total_shots) * 100
    print("The players shooting percentage is: ", round(make_percentage, 1), "%")


def coffee():
    pounds = eval(input("How many pounds of coffee would you like?: "))
    total_cost = (pounds * 10.50) + (pounds * 0.86) + 1.50
    print("Your total is: $", total_cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter how many kilometers you traveled: "))
    miles = kilometers / 1.609
    print("You traveled", round(miles, 2), "miles.")


if __name__ == '__main__':
    pass
