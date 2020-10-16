"""
Program: bounciness.py
Author: Jeff Kent
Last dat modified: 10/8/2020

The purpose of this program is to calculate the total
    distance traveled by bouning a ball
"""



# Get the input for bounce index

index=float(input("Enter the bounce index: "))

# Get the input for height the ball is dropped from

ball_height=float(input("Enter the height from which the ball was dropped: "))

# Get the number of times the ball bounces

Total_bounces=int(input("Enter the number of bounces: "))

# initialize the distance variable

dist=0

# iterate the loop

while Total_bounces > 0:

    # Distance befor bounce

    dist=dist+ball_height

    # Updated height

    ball_height=ball_height * index

    # distance after bounce

    dist=dist + ball_height

    # Decrement the value of bounces

    Total_bounces-=1

# Display the output

print("The ball travels the distance of %.2f feet." % dist)
