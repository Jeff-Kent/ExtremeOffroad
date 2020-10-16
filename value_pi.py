"""
Program: value_pi.py
Author: Jeff Kent
Last date modified: 10/8/2020

The purpose of this program is to output the calculated value of pi
based on the number of iterations specified by the user.
"""

def main():
    num = int(input("Enter total number of iterations: "))
    total = 0
    for i in range(num):
        total += ((-1) ** i) * (1 / ((2 * i) + 1))
    total *= 4
    print("The calculated value of pi is " + str(total))
main()
