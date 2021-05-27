# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info

USER_NAME = os.getenv("USER_NAME", default="Player One") 

print("Hello",USER_NAME,"welcome to my game")

print("Rock, Paper, Scissors, Shoot!")


#user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

#print("User Choice: ", user_choice)

#validate the input such that only if it is one of the selected values
#... will we continue with the rest of the program
#... otherwise we'll stop the program before it tries to do anything else
#... and we'll ask the user to run the program again

#The following is a loop until the user enters a valid entry

#while True:

while True:
    user_choice = str(input("Please choose one of 'rock', 'paper', 'scissors':"))
    print("User Choice: ", user_choice)
    if user_choice in ('rock', 'paper', 'scissors'):
        break
    print("Oops, invalid input. Try again!")
    




valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer Choice: ", computer_choice)


if (user_choice == "rock") and (computer_choice == "scissors"):
   print("You won!")
if (user_choice == "scissors") and (computer_choice == "paper"):
    print("You won!")
if (user_choice == "paper") and (computer_choice == "rock"):
    print("You won!")
if (user_choice == "rock") and (computer_choice == "paper"):
    print("You lost!")
if (user_choice == "scissors") and (computer_choice == "rock"):
    print("You lost!")
if (user_choice == "paper") and (computer_choice == "scissors"):
    print("You lost!")
if (user_choice == computer_choice):
    print("You tied!")


#user_choice_2 input("Do you want to play again? (Y/N): ")
#print ("User Choice: ", user_choice_2)

#if user_choice_2 == Y

#if (user_choice_2 == "Y") or (user_choice == "N"):
#    print("Let's play again!")
#else:
#    print("Oops, please enter a valid entry")
#    exit()

#print("This is the end of our game. Please play again!")

#    answer = str(input('Run again? (Y/N): '))
#    if answer == 'Y':
#        continue
#    else:
#        print("Goodbye")
#        break