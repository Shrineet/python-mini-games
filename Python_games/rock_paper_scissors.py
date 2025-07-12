# Rock Paper Scissors game vs computer

import random

# Options to choose from
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

# Compare choices
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
