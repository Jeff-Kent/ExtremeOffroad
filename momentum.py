"""
Program: momentum.py
Author: Jeff Kent
Last date modified 9/29/2020

The purpose of this program is calculate the momentum of an object in motion
Input an object's mass (in kilograms) and an object's velocity (in meters per second)
Calculates an object's momentum using the formula
    momentum = mass * velocity
Outputs the object's momentum labled as momentum
"""

mass = float(input("Enter the mass of the object (in kilograms): "))
velocity = float(input("Enter the velocity of the object in (meters per second): "))
momentum = mass * velocity

print("The momentum of the object is " + str(momentum) + " kg m/s.")

