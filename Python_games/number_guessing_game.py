# Number Guessing Game
# The player has to guess a number between 1 and 100

import random  # we need this to generate random numbers

secret_number = random.randint(1, 100)  # computer picks a number
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# loop until the player guesses it right
while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it in", attempts, "tries.")
        break
