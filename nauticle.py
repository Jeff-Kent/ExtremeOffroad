"""
Program: nauticle.py
Author: Jeff Kent
Last date modified: 10/6/2020
calculate the number of kilometers in nauticle miles.

The purpose of this program is to take the number of kilometers
and convert the kilometers into nauticle miles using the formula:
nauticle_miles = km * 00.5399568035
1. Siginificant constrants
    kilometers
2. The inputs are
    kilometers
3. Computations
    nauticle_miles = km * 0.5399568035
4. The output is
    nautical miles
"""

km = float(input("Enter the number of kilometers: "))
nauticle_miles = km * 0.5399568035
print(km, "kilometers is equal to", nauticle_miles, "nauticle miles.")
