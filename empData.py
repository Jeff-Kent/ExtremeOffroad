"""
Program: empData.py
Author: Jeff Kent
Date: 10/14/2020

The purpose of this program is the take data from a .txt file and output
the data in a tabular format that displays the employee's name, wages paid,
and the hours worked for that period.
"""

file_name = input('Enter input data file name: ')
print('\n%-15s%-10s%-10s' % ('Name', 'Hours', 'Wages Paid'))

for line in open(file_name):
    line = line.strip()
    
    if line != '':        
        (name, wage, hours) = line.split()        
        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

        print('%-15s%-10d%-10.2f' % (name, hours, pay))
