"""
File name: passwordgenerator.py
Author: Victor Santana
Latest update: 05/03/2024

PROGRAM DESCRIPTION: This program will ask some questions to the user in order to generate a random password.
"""

# This imports the needed libraries
import random

# This displays the introduction of the 
print(" ",
      "Welcome to the Password Generator",
      "---------------------------------",
      " ", sep= "\n")

# This variable contains all of the characters that will be randomly picked to generate the password
chars = "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ`~!@#$%^&*()_-+=[]{}\|;:',.<>/?1234567890"

# This asks the user for the amount of passwords he/she would like that the program generates
password_amount = int(input("Please enter the amount of passwords you would like to generate: "))

# This asks the user for lenght of the password that the user prefers
password_lenght = int(input("Please enter the preferred lenght for each password: "))

# This will display a header showing the passwords
print("\nHere are your generated passwords:")

# This nested for loop will generate the random password
for pwd in range(password_amount):

    # This variable will be use to store the generated password
    passwords = ""

    # This nested for loop will generate the random password
    for c in range(password_lenght):

        # This will store and generate the password in the created variable
        passwords += random.choice(chars)

    # This will display the passwords
    print(passwords)

# This will display an empty space
print()