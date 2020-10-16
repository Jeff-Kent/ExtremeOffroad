"""
Program: populationGrowth
Author: Jeff Kent
Last date modified: 10/8/2020

The purpose of this program is to predict the total
    population growth of an organism.
"""

#define the function

def predict_population():

    #Import math

    import math

    #get the intial number of organisms

    orgNum = int(input("Enter the initial number of organisms: "))

    #get the rate of organism growth

    growthRate = float(input("Enter the organisms rate of growth [a real number > 0]: "))

    while(growthRate<1):

        print("Invalid population growth rate.")

        growthRate = float(input("Enter the rate of growth [a real number > 0]: "))

    #get the total number of hours for the rate of growth

    rate = int(input("Enter the number of hours to achieve the rate of growth: "))

    #prompt for total hours

    time = int(input("Enter the total hours of growth: "))

    #initialize the values totalPop and hours

    totalPop=orgNum

    hours = 1

    while (hours < time):

        #calculate the total population

        totalPop *= growthRate

        #calculate hours

        hours += rate

    #print the total population

    print("The total population is " + str(int(totalPop)))

#call the function

predict_population()
