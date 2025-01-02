#The purpose of this project was to practice with global and local variables.

import random

def choose_difficulty():
    """Easy gives you 10 guesses, hard gives you 5 guesses."""
    difficulty = ""
    while not difficulty == "easy" and not difficulty == "hard":
        difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\": ").lower()
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts

#Ask user to guess number. Only accept integers between 1 and 100. Reduce global variable
#attempts by 1.
def make_guess():
    global attempts
    guess = ""
    while not type(guess) == int:
        guess = input("Make a guess: ")
        try:
            guess = int(guess)
            if guess > 100 or guess < 1:
                print("Please guess a number between 1 and 100")
                guess = ""
        except:
            print("Please guess a number between 1 and 100.")
    attempts -= 1
    return guess

#This will compare the user guess against the global variable of secret_number.
#If the user guessed the number, set global variable correct_guess to True.
def check_guess(guess):
    global secret_number
    global correct_guess
    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print ("Too low.")
    else:
        print ("You guessed the secret number!")
        correct_guess = True

#Greet user, define global variables.
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
secret_number = random.randint(1,101)
attempts = choose_difficulty()
correct_guess = False

#While loop that prompts user for a guess if there are remaining attempts
#and user has not already guessed the number
while attempts > 0 and not correct_guess:
    print(f"You have {attempts} {"attempts" if attempts > 1 else "attempt"} remaining to guess the number.")
    user_guess = make_guess()
    check_guess(user_guess)
if not correct_guess:
    print("Better luck next time.")
