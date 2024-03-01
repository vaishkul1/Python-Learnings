# rock paper scissors
import random


options = ["rock", "paper", "scissors"]

computer_guess = random.choice(options)

user_guess = input("enter rock/paper/scissor= ")

if user_guess == "rock":
    if computer_guess == "paper":
        print("computer wins")
    elif computer_guess == "scissors":
        print("user wins")
    elif computer_guess == "rock":
        print("tie")


if user_guess == "paper":
    if computer_guess == "scissors":
        print("computer wins")
    elif computer_guess == "rock":
        print("user wins")
    elif computer_guess == "paper":
        print("tie")


if user_guess == "scissors":
    if computer_guess == "paper":
        print("user wins")
    elif computer_guess == "rock":
        print("user wins")
    elif computer_guess == "paper":
        print("scissors")
