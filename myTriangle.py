"""
Program: myTriangle.py
Author: Jeff Kent
Last date modified: 10/13/2020

The purpose of this program is to determine if
the lengths given produce an equalateral triangle or not.
"""

print("Enter the length of each side of the triangle: ")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if x == y == z:
    print("This is an qualateral triangle")
else:
    print("This is not an equalateral triangle")
