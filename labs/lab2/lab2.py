'''
Elijah Springs

lab2.py

This program is written to find the RMS mean, harmonic mean, and geometric mean of the values inputted by the user.

This is my work.
'''

import math

def means():
    #user input for total values
    amount_of_values = eval(input("Enter the amount of values you would like: "))

    #accumulators
    accumulator_rms = 0
    accumulator_harmonic = 0
    accumulator_geometric = 1

    #user input for values and loop
    for i in range(amount_of_values):
        input_value = eval(input("Enter value: "))

        #RMS calculation loop
        accumulator_rms = math.pow(input_value,2) + accumulator_rms

        #Harmonic calculation loop
        accumulator_harmonic = (1/input_value) + accumulator_harmonic

        #Geometric calculation loop
        accumulator_geometric = accumulator_geometric * input_value

    #RMS final calculations
    rms_total = accumulator_rms / amount_of_values
    rms_mean = math.sqrt(rms_total)

    #Harmonic final calculations
    harmonic_mean = amount_of_values/accumulator_harmonic

    #Geometric final calculations
    geometric_total = math.pow(accumulator_geometric,1/amount_of_values)


    print("The RMS mean is:", round(rms_mean,3))
    print("The harmonic mean is: ", harmonic_mean)
    print("The geometric mean is: ", round(geometric_total,3))

means()
