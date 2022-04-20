"""
Elijah Springs

lab13.py

This file solves the capstone 2 question, finding signals in the range 4000-5000, at most 5 of those signals.

This is my work.
"""

def star_find(filename):
    # opens the file
    file = open(filename, "r")
    # store the first line
    line = file.readline()
    # accumulators
    signal_accumulator = 0
    list_of_neutrons = []

    # while there are lines in the file and 5 neutron stars at most have not been found
    while line and len(list_of_neutrons) < 5:

        # creates a list of all numbers
        strip_line = line.strip()
        split_line = strip_line.split()

        # runs through the list of all number
        for i in split_line:
            # adds one to the signal accumulator for each signal that has been searched.
            signal_accumulator = signal_accumulator + 1
            # if the value in the list is a neutron star, it adds it to the neutron star accumulator.
            if eval(i) > 4000 and eval(i) < 5000:
                list_of_neutrons.append(i)
        # reads the next line if there is a next line.
        line = file.readline()

    # outputs
    print("Amount of signals:", len(list_of_neutrons))
    print("Signal strengths:", list_of_neutrons)
    print("Signals searched in total:", signal_accumulator)
    # closes file.
    file.close()

