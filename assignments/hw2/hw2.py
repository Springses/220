"""
Name: Elijah Springs
hw2.py

Problem: This program solves the equations for sum of threes, makes a multiplication table, finds the area of a triangle,
finds the sum of squares, and powers numbers without using the restricted code.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("enter the upper bound?: "))
    accumulator = 0
    for i in range(3, upper_bound+1, 3):
        accumulator = i + accumulator
    print("sum of threes is:", accumulator)


def multiplication_table():
    for i in range(1,11):
        print(i, end= "\t")
    print()
    for i in range(1,11):
        print(i * 2, end= "\t")
    print()
    for i in range(1,11):
        print(i * 3, end= "\t")
    print()
    for i in range(1,11):
        print(i * 4, end= "\t")
    print()
    for i in range(1,11):
        print(i * 5, end= "\t")
    print()
    for i in range(1,11):
        print(i * 6, end= "\t")
    print()
    for i in range(1,11):
        print(i * 7, end= "\t")
    print()
    for i in range(1,11):
        print(i * 8, end= "\t")
    print()
    for i in range(1,11):
        print(i * 9, end= "\t")
    print()
    for i in range(1,11):
        print(i * 10, end= "\t")
    print()


def triangle_area():
    side_a = eval(input("enter side a length: "))
    side_b = eval(input("enter side b length: "))
    side_c = eval(input("enter side c length: "))

    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * ((s - side_a) * (s - side_b) * (s - side_c)))
    print("the area is: ", area)


def sum_squares():
    lower_range = eval(input("enter the lower range: "))
    upper_range = eval(input("enter the upper range: "))
    accumulator = 0
    for i in range(lower_range,upper_range+1):
        accumulator_2 = i * i
        accumulator = accumulator + accumulator_2
    print("the sum of squares is: ", accumulator)



def power():
    base = eval(input("Enter the base number: "))
    expo = eval(input("Enter the exponent number: "))
    accumulator = base
    accumulator_2 = 0
    for i in range(expo-1):
        accumulator = accumulator * base
    print(base, '^', expo, '=', accumulator)



if __name__ == '__main__':
    pass
