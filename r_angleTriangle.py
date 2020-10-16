"""
Program:r_angleTriangle.py
Author: Jeff Kent
Last date updated: 10/13/2020

The purpose of this program is to determine
if a triangle is a right angle.
"""
side1 = int(input("Enter the length of the first side of the triangle: "))
side2 = int(input("Enter the length of the second side of the triangle: "))
side3 = int(input("Enter the length of the third side of the triangle: "))
if (side1 * side1 + side2 * side2) == side3 * side3 \
           or (side1 * side1 + side3 * side3) == side2 * side2 \
           or (side2 * side2 + side3 * side3) == side1 * side1:
    print("This triagle is a right angle triangle.")
else:
    print("This is not a right angle triangle.")
