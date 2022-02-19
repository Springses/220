"""
Name: Elijah Springs
hw5.py

Problem: This program puts a first and last name in reverse order, finds the company name in a website domain, and finds
initials of names given by the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    # input
    name = input("enter a name (first last): " )

    # finds the space between first and last name
    space_find = name.find(" ")

    # finds first and last name
    last_name = name[space_find + 1:len(name)]
    first_name = name[0:space_find]

    # output
    print(last_name + ", " + first_name)


def company_name():
    # user input
    domain = input("enter a domain: ")

    # finds the first dot
    dot = domain.find(".")

    # finds the company name between first dot and second dot
    company = domain[dot + 1 : domain.rfind(".")]

    # output
    print(company)


def initials():
    # user input for total # of students
    total_students = eval(input("how many students are in the class?: "))

    # loop
    for i in range(total_students):
        # user input for name
        student_name = input("What is the name of student " + str(i + 1) + "?: ")
        # finds the space between first and last name
        space_find = student_name.find(" ")
        # finds first initial
        first_initial = student_name[0]
        # finds last initial
        last_initial = student_name[space_find + 1]
        # output
        print(first_initial + last_initial)


def names():
    # i didn't have enought time for the rest :(
    pass


def thirds():
    pass


def word_average():
    pass


def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
