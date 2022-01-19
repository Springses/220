"""
Elijah Springs
lab1.py
This is my work
"""

def monthly_interest():
    ## The Inputs
    annual_interest = eval(input("What is your annual interest?: "))
    billing_cycle = eval(input("What is the number of days in your billing cycle?: "))
    prev_net_balance = eval(input("What is your previous net balance?: "))
    payment_amount = eval(input("What is your payment amount?: "))
    day_of_billing_cycle = eval(input("What day of your billing cycle was your payment made?: "))

    ## Calculations
    Step_One = prev_net_balance * billing_cycle
    Step_Two = payment_amount * (billing_cycle - day_of_billing_cycle)
    Step_Three = Step_One - Step_Two
    Step_Four = Step_Three / billing_cycle
    monthly_interest_rate = (annual_interest/100) / 12
    monthly_interest_charge = Step_Four * monthly_interest_rate

    ## Output
    print("Your monthly interest charge is: $", round(monthly_interest_charge,2))

monthly_interest()

