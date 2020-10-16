"""
Program: fiveStar.py
Author: Jeff Kent
Last date modified: 9/29/2020

Input the number of new and used video rentals
Compute the total cost using the formula
totalCost = new * newRelease + old * oldies
Print the total cost of rental videos
"""
new = 3.00
old = 2.00
newRelease = float(input("Enter the number of new release rentals: "))
oldies = float(input("Enter the number of oldie rentals: "))
totalCost = new * newRelease + old * oldies
print("The total cost is $" + str(totalCost))
