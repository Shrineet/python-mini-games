# Hangman ---> guess the hidden word letter by letter

# List of possible words
words = ["apple", "banana", "grapes", "mango", "peach"]

import random
word = random.choice(words)  # computer picks a word
guessed = ["_"] * len(word)  # blank letters
tries = 6  # number of attempts

print("Welcome to Hangman!")
print("You have", tries, "tries to guess the word.")

while tries > 0 and "_" in guessed:
    print("\nCurrent word: " + " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nYou lost! The word was:", word)
