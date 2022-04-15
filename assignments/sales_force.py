"""
Elijah Springs

sales_force.py

This class imports from the SalesPerson class, and creates a list of employees from a text document, see's if
employees match a quota, grabs an individual employee from their id, finds the top seller, and grabs sale frequencies.

This is my work.
"""
# imports from class
from sales_person import SalesPerson

class SalesForce:
    # creates an empty list
    def __init__(self):
        self.sales_people = []

    # opens the file and reads
    def add_data(self, file_name):
        the_file = open(file_name, "r")
        line = the_file.readline()

        # goes through all the lines of document
        while line:
            # creates a list of each line
            strip_line = line.strip()
            strip_line = strip_line.replace(",", " ")
            split_line = strip_line.split()
            employee_info = split_line

            # indexes and stores id and name
            employee_id = int(employee_info[0])
            employee_name = str(employee_info[1])+ " " + str(employee_info[2])

            employee = SalesPerson(employee_id, employee_name)

            # loops and stores employees sales
            for i in range(3, len(employee_info)):
                employee.enter_sale(float(employee_info[i]))

            # adds employee to list
            self.sales_people.append(employee)

            # reads next line
            line = the_file.readline()

    def quota_report(self, quota):
        # list accumulators
        list_of_employee_info = []
        list_of_all_employees = []

        for i in self.sales_people:
            # stores all of employees info in one list
            list_of_employee_info.append(i.get_id)
            list_of_employee_info.append(i.get_name)
            list_of_employee_info.append(i.total_sales)
            list_of_employee_info.append(i.met_quota(quota))

            # adds that list to this list
            list_of_all_employees.append(list_of_employee_info)

        return list_of_all_employees

    def top_seller(self):
        # accumulators
        top_sellers_list = []
        top_seller = SalesPerson(222, "Fake Employee")

        # loops through all employees
        for i in self.sales_people:
            seller = i
            # if employees total_sales beats previous employees sales, it stores them as the top seller.
            if seller.total_sales() > top_seller.total_sales():
                top_seller = seller
            # if there is a tie, stores them both in a list
            elif seller.total_sales() == top_seller.total_sales():
                top_seller = [top_seller, seller]

        # returns list if tie, otherwise returns a list of the top seller only
        if top_seller == list:
            return top_seller
        else:
            top_sellers_list.append(top_seller)
            return top_sellers_list

    def individual_sales(self, employee_id):
        # variables and default booleans
        i = 0
        recog = False

        # loops through all employees and sees if id matches.
        while i < len(self.sales_people) - 1 and not recog:
            employee = self.sales_people[i]

            if employee.get_id() == employee_id:
                recog = True

            # if it doesn't find the employee, adds one to the indexer
            i = i + 1

        # if the employee was found, it returns the employee. Otherwise, it returns None
        if recog:
            employee = self.sales_people[i]
            return employee
        else:
            return None

    def get_sale_frequencies(self):
        # accumulators
        dictionary_of_sales = {}
        list_of_sales = []
        list_of_unique_sales = []

        # loops through all employees and grabs all their sales.
        for i in self.sales_people:
            for j in i.get_sales():
                list_of_sales.append(j)

        # loops through all sales, and only stores one of each.
        for k in list_of_sales:
            if list_of_unique_sales.count(k) == 0:
                list_of_unique_sales.append(k)

        # stores the frequencies of each sale in the dictionary
        for l in list_of_unique_sales:
            dictionary_of_sales[l] = [list_of_sales.count(l)]

        # returns dictionary
        return dictionary_of_sales







