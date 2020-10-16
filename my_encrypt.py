"""
Program: my_encrypt.py
Author: Jeff Kent
Date: 10/14/2020

The purpose of this progran is to take the inputs from the user
and output the encrypted text.  
"""
encryptText = ''
plainText = input("\nEnter the Plain Text : ")
distance = int(input("Enter the distance : "))

for i in plainText:    
    Val = ord(i)    
    cipher = Val + distance
    
    if cipher > ord('z'):
        cipher = ord('a') + distance - (ord('z') - Val + 1)
    encryptText = encryptText + chr(cipher)
print('The Cipher Text is : ', encryptText)
