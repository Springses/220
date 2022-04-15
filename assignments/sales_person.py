"""
Elijah Springs

sales_person.py

This class is made to store and create functions for an employee and their id, name, and sales.

This is my work.
"""



class SalesPerson:

    #storing variables
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        # returns id
        return self.employee_id

    def get_name(self):
        # returns name
        return self.name

    def set_name(self, name):
        # sets name
        self.name = name

    def enter_sale(self, sale):
        # adds a sale to sales list
        self.sales.append(sale)

    def total_sales(self):
        # finds the total of sales in sales list
        accumulator = 0
        for i in self.sales:
            accumulator = accumulator + i

        return accumulator

    def get_sales(self):
        # returns all sales in a list
        return self.sales

    def met_quota(self, quota):
        # if the total amount of all sales equals or is greater than quota, it returns true
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        # stores other SalesPersons total sales
        other_sales = other.total_sales()

        # returns values if the total sales is more, less, or equal than self total sales.
        if other_sales > self.total_sales():
            return -1
        elif other_sales < self.total_sales():
            return 1
        elif other_sales == self.total_sales():
            return 0

    def __str__(self):
        # returns all details of employee
        return "{}-{}:{}".format(self.employee_id,self.name,self.total_sales())




