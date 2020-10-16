"""
Program"overtime_pay.py
Author: Jeff Kent
Last date modified: 10/6/2020

The purpose of this program is to calculate the total amount of
weekly pay, including overtime, due an employee.

1. Significant constrants
        hourly wage
2. The inputs are
        hourly wage
        number of regular hours
        number of overtime hours
3. Computations:
        weekly_pay = (hr_wage * reg_hours) + (1.5 * hr_wage * ot_hours)
4. The output is
        the total weekly pay
"""

#Get the hourly wage of the employee
hr_wage = float(input("Enter the hourly wage: "))

#Get the total number of regular hours of the employee
reg_hours = float(input("Enter the number of regular hours of the employee: "))

#Get the total number of overtime hours of the employee
ot_hours = float(input("Enter the number of overtime hours of the employee: "))

#calculate the weekly pay
weekly_pay = (hr_wage * reg_hours) + (1.5 * hr_wage * ot_hours)

#print the weekly pay due the employee
print(weekly_pay)
