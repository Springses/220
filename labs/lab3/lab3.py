'''
Elijah Springs

lab3.py

This program is written to find the daily average of cars traveled on a road for different days, and the
overall average of cars traveled on all roads and days.

This is my work.
'''

def traffic():
    #input for the amount of roads surveyed
    roads_surveyed = eval(input("how many roads were surveyed?:"))

    #accumulators
    daily_addition_accumulator = 0
    daily_mean_accumulator = 0
    cars_accumulator = 0

    #start of loop with first input for the amount of days surveyed
    for i in range(roads_surveyed):
        print("how many days was road", i+1,"surveyed?:",end=" ")
        days_surveyed = eval(input(" "))

    #start of nested loop with the input of cars for each day.
        for j in range(days_surveyed):
            print("\t how many cars traveled on day", j+1,"?:", end=" ")
            cars_traveled = eval(input(" "))
            cars_accumulator = cars_accumulator + cars_traveled
    #calculations for daily means.
            daily_addition_accumulator = daily_addition_accumulator + cars_traveled
            daily_mean_accumulator = daily_addition_accumulator / days_surveyed

    #resetting values and printing daily mean
        print("Road", i+1,"average vehicles per day is:", daily_mean_accumulator)
        daily_addition_accumulator = 0
        daily_mean_accumulator = 0

    #calculating overall mean and outputting it as well as the total amount of cars.
    print("Total number of vehicles traveled on all roads: ", cars_accumulator)
    overall_average = cars_accumulator / roads_surveyed
    print("Average number of vehicles per road: ", round(overall_average,2))
traffic()