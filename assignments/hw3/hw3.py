"""
Name: Elijah Springs
hw3.py

Problem: This is a series of functions that help accumulate grade average, total of tips, calculate a square root
of a number, and create a sequence of terms. I could not quite figure out how to create the calculation for pi
unfortunately.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    grades_amount = eval(input("how many grades will you enter?: "))
    accumulator = 0
    for i in range(grades_amount):
        grade = eval(input("Enter grade: "))
        accumulator = accumulator + grade
    grade_average = accumulator / grades_amount
    print("the average is:", grade_average)


def tip_jar():
    tip_accumulator = 0
    for i in range(5):
        donation = eval(input("how much would you like to donate?"))
        tip_accumulator = tip_accumulator + donation
    print("total tips:", tip_accumulator)

def newton():
    sqrt_number = eval(input("what number would you like to square root?"))
    approx_times = eval(input("how many times should we improve the approximation?"))
    approx = sqrt_number
    for i in range(approx_times):
        approx = (approx + (sqrt_number/approx)) / 2
    print("the square root is approximately:", approx)



def sequence():
    terms = eval(input("how many terms would you like?"))
    for i in range(1,terms+1,2):
        print(i, end= " ")
        print(i, end= " ")



def pi():
    pass


if __name__ == '__main__':
    pass
