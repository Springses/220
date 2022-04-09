"""
Elijah Springs

hw10.py

This program creates a function that grabs a number from the fibonacci sequence, how many years it takes to double
interest, and creates a syracuse sequence. Also creates a the sphere class to calculate surface area and face class that
draws a face that changes when called.

This is my work.
"""

def fibonacci(n):
    if n < 1:
        return None
    else:
        fibonacci_list = [1, 1]
        acc = 1
        for i in range(n):
            new_num = fibonacci_list[acc] + fibonacci_list[acc - 1]
            fibonacci_list.append(new_num)
            acc = acc + 1
        fibonacci_num = fibonacci_list[n - 1]
        return fibonacci_num

def double_investment(principle, rate):
    acc = 0
    number_of_years = 0

    while not acc / 2 == principle:
        number_of_years = number_of_years + 1
        acc = principle(number_of_years + rate)

    return number_of_years

def syracuse(n):
    sequence = [n]

    while not sequence[len(sequence) - 1] == 1:
        if sequence[len(sequence) - 1] / 2 == int:
            num = sequence[len(sequence) - 1] / 2
            sequence.append(num)
        else:
            num = (3 * sequence[len(sequence) - 1]) + 1
            sequence.append(num)

    return sequence

def goldbach(n):
    pass




