"""
Elijah Springs

algorithms.py

This is the algorithms.py file, containing the functions read_data, is_in_linear, selection_sort, calc_area, and
rec_sort.

This is my work.
"""
from graphics import *

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

    the_file.close()
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

def selection_sort(values):
    # finder accumulators
    min_finder = 0
    max_finder = 0
    # maximum and minimum value setters
    max_val = values[0]
    min_val = values[0]
    # loops through every value
    for i in values:
        # if this number is more than the number set as the maximum, it sets this number as the maximum
        if i > max_val:
            max_val = i
            max_finder = values.index(i)
        # if this number is smaller than the number set at the minimum, it sets it as the minimum
        if i < min_val:
            min_val = i
            min_finder = values.index(i)

    # swaps the first value in the list to the minimum, and the last to the maximum
    values[0], values[min_finder] = min_val, values[0]
    values[len(values) - 1], values[max_finder] = max_val, values[len(values) - 1]

    # indexer accumulator
    indexer = 1

    # while indexer is smaller than the amount of values between the minimum and maximum.
    while indexer < len(values) - 1:
        # sets the minimum as the maximum
        min_val = max_val

        for j in range(indexer, len(values) - 1):
            # loops through every value, finding the next smallest number
            if values[j] < min_val:
                min_val = values[j]
                min_finder = j
        # swaps the next smallest number in the correct place
        values[indexer], values[min_finder] = min_val, values[indexer]
        # increases the indexer accumulator by 1
        indexer = indexer + 1


def calc_area(rect):
    # stores the rectangles points
    rect_p1 = rect.getP1()
    rect_p2 = rect.getP2()
    # stores each points x and y values
    rect_1_x = rect_p1.getX()
    rect_1_y = rect_p1.getY()
    rect_2_x = rect_p2.getX()
    rect_2_y = rect_p2.getY()
    # finds the length of the horizontal and vertical sides
    horizontal = rect_2_x - rect_1_x
    vertical = rect_2_y - rect_1_y
    # calculates area
    area = horizontal * vertical
    # returns area
    return area

def rect_sort(rectangles):
    # list of all rectangles areas accumulator
    list_of_areas = []

    # loops through every rectangle, and adds every one of their areas to the area accumulator
    for i in rectangles:
        area_grabber = calc_area(i)
        list_of_areas.append(area_grabber)

    # finder accumulators
    min_finder = 0
    max_finder = 0
    # maximum and minimum value setters
    max_val = list_of_areas[0]
    min_val = list_of_areas[0]
    # loops through every value
    for i in list_of_areas:
        # if this number is more than the number set as the maximum, it sets this number as the maximum
        if i > max_val:
            max_val = i
            max_finder = list_of_areas.index(i)
        # if this number is smaller than the number set at the minimum, it sets it as the minimum
        if i < min_val:
            min_val = i
            min_finder = list_of_areas.index(i)

    # swaps the first value in the list to the minimum, and the last to the maximum
    list_of_areas[0], list_of_areas[min_finder] = min_val, list_of_areas[0]
    list_of_areas[len(list_of_areas) - 1], list_of_areas[max_finder] = max_val, list_of_areas[len(list_of_areas) - 1]

    # indexer accumulator
    indexer = 1

    # while indexer is smaller than the amount of values between the minimum and maximum.
    while indexer < len(list_of_areas) - 1:
        # sets the minimum as the maximum
        min_val = max_val

        for j in range(indexer, len(list_of_areas) - 1):
            # loops through every value, finding the next smallest number
            if list_of_areas[j] < min_val:
                min_val = list_of_areas[j]
                min_finder = j
        # swaps the next smallest number in the correct place
        list_of_areas[indexer], list_of_areas[min_finder] = min_val, list_of_areas[indexer]
        # increases the indexer accumulator by 1
        indexer = indexer + 1




