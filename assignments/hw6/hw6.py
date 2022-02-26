"""
Name: Elijah Springs
hw6.py

Problem: This program converts a number to cash using the .format function, encodes a message, finds the surface area
and volume of a sphere (or sets it up at least), and does a better version of encoding a message.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def cash_converter():
    # input
    num = eval(input("Enter a number: "))

    # the format
    output = "That is ${}.00".format(num)

    # the output
    print(output)


def encode():
    # the input
    message = input("enter a message: ")

    # the key input
    key = eval(input("enter a number key: "))

    # accumulator for the string
    new_message_accumulator = ""

    # loop
    for i in range(len(message)):
        # indexing
        message_ord = ord(message[i])

        # converting to numbers
        new_message_ord = message_ord + key

        # converting back to characters
        new_letter = chr(new_message_ord)
        new_message_accumulator = new_message_accumulator + new_letter

    # output
    print(new_message_accumulator)



def sphere_area(radius):
    # calculation and return
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area


def sphere_volume(radius):
    # calculation and return
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

# TO TEST THE SPHERE AREA AND VOLUME

# r = eval(input("enter the radius: "))
# r = float(r)
# the_area = sphere_area(r)
# the_volume = sphere_volume(r)
# print(the_area)
# print(the_volume)

def sum_n(number):
    # I don't quite understand what to do on this one :(
    pass


def sum_n_cubes(number):
    # I don't quite understand this one either :(
    pass


def encode_better():
    # inputs
    message = input("enter a message: ")
    key = input("enter a key: ")

    # accumulator
    new_message = ""

    # loop
    for i in range(len(message)):

        # indexing
        message_letter = message[i]
        key_letter = key[i % len(key)]

        # converting to numbers
        message_ord: int = ord(message_letter)
        key_ord = ord(key_letter)

        # subtracting by A
        message_accumulator = message_ord - 65
        key_accumulator = key_ord - 65

        # converting back to characters and adding them to the accumulator
        new_ord = (message_accumulator + key_accumulator) % 58
        new_chr = new_ord + 65
        new_letter = chr(new_chr)

        new_message = new_message + new_letter
    # output
    print(new_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
