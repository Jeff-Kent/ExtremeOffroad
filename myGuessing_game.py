import random       
import math
print("In your head, quess a number")       
smaller = int(input("Enter the smaller number:"))       
larger = int(input("Enter the larger number:"))       
numOfChances = math.ceil((math.log(larger)))           
count=0                                               
while(True):
   if(count >= numOfChances):                           
       print(" Sorry, I'm out of guesses, and you cheated.")
       break                                       
   else:
       print(smaller," ",larger)                   
       count+=1
       myNumber = random.randint(smaller,larger)       
       print("Your Number is:", myNumber)
       Response = input("Enter =,<, or >:")           
       if (Response=='='):                           
           print(" Congratulations, you've guessed it in", count, "tries.")
           break
       elif (Response=='<'):
            larger=myNumber-1
       elif (Response=='>'):
            smaller=myNumber+1
