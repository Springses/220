"""
Elijah Springs

lab12.py

This file removes a value within a list and replaces it, finds every number in a file and puts it into a list,
searches for a value in a list, returns the number of digits in an integer, and creates a higher or lower game.

This is my work.
"""
from random import randint

def find_and_remove_first(the_list, value):
    # value finder accumulator
    value_finder = ""

    # index accumulator
    index_accumulator = -1

    # while value finder doesn't equal the value desired
    while not value_finder == value:
        index_accumulator = index_accumulator + 1
        value_finder = the_list[index_accumulator]

    # removes value if found
    the_list.remove(value)
    # replaces the value
    the_list.insert(index_accumulator, "Elijah Springs")


def read_data(filename):
    # opens the file and reads the first line
    the_file = open(filename, "r")
    line = the_file.readline()

    # list accumulator
    list_acc = []

    # while there are lines, it strips, splits, and adds the numbers to the list accumulator
    while line:
        strip_line = line.strip()
        split_line = strip_line.split()
        list_acc = list_acc + split_line
        line = the_file.readline()

    return list_acc



def is_in_linear(search_val, values):
    # setting the identifier boolean
    identifier = False

    # i variable
    i = 0

    # while i is shorter than the length of list and the value has not been found
    while i < len(values) - 1 and not identifier:
        # if the value indexed at i is the desired value
        if values[i] == search_val:
            identifier = True
        # if not found, increase the indexer variable
        else:
            i = i + 1

    # if the value has been found, return True, otherwise return False
    if identifier:
        return True
    else:
        return False


def good_input():
    # user input
    user_number = eval(input("Insert a number: "))

    # if user_number is over or less than the good range.
    if user_number > 10 or user_number < 1:
        # while the user number is higher or lower than the good range, it will request a number until then.
        while user_number > 10 or user_number < 1:
            if user_number > 10:
                print("Number is too high.")
                user_number = eval(input("Insert another number: "))
            elif user_number < 1:
                print("Number is too low.")
                user_number = eval(input("Insert another number: "))

    print("Good input")
    return user_number


def num_digits():
    # string accumulator
    num_accumulator = ""
    # user input
    user_input = input("Enter a number: ")

    # while the user inputs a number above 0
    while user_input.count("0") == 0 and user_input.count("-") == 0:
        # add user input to string accumulator
        num_accumulator = num_accumulator + user_input
        user_input = input("Enter another number: ")

    # evaluate string accumulator
    num_accumulator = eval(num_accumulator)
    accumulator = num_accumulator
    # number of digits accumulator
    num_of_digits = 0

    # while the number has not reached 0
    while accumulator > 0:
        accumulator = accumulator // 10
        num_of_digits = num_of_digits + 1

    # returns the number of digits via the number of digits accumulator
    print("Your number,", num_accumulator, "has", num_of_digits, "digits")

def hi_lo_games():
    # generates random number
    random_num = randint(1, 101)
    # sets the amount of guesses
    guesses = 7
    # sets default boolean
    is_correct = False

    # while the user input is not correct and the user still has guesses remaining
    while not guesses == 0 and not is_correct:
        print("Guesses remaining: ", guesses)
        user_num = eval(input("Enter a number 1-100: "))
        # if user number is higher than random number
        if user_num > random_num:
            print("Try going lower.")
            guesses = guesses - 1
        # if user number is lower than random number
        elif user_num < random_num:
            print("Try going higher.")
            guesses = guesses - 1
        # if user guesses the number correctly
        elif user_num == random_num:
            is_correct = True

    # if the guess was correct, it displays a winning message. Otherwise, it displays a losing message.
    if is_correct:
        print("You Win!!! The number was", random_num)
    else:
        print("Sorry, the number was", random_num)
