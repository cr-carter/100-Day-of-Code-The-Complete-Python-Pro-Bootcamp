#The purpose of this project is to practice with random generation, basic arrays, while loops, and creating functions within the program

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    SCISSORS
'''

player = input("Welcome to Rock, Paper, Scissors! Please type \"R\" for rock, \"P\" for paper, \"S\" for scissors.\n").upper()
choices = ["R", "P", "S"]

while player not in choices:
    player = input("Please type \"R\" for rock, \"P\" for paper, \"S\" for scissors.\n").upper()

import random
computer = random.choice(choices)

def print_choice(who):
    if who == "R":
        print(rock)
    elif who == "P":
        print(paper)
    else:
        print(scissors)
print("Player")
print_choice(player)
print("Computer")
print_choice(computer)

if player == computer:
    print("It's a tie!")
elif (player == "R" and computer == "S") or (player == "S" and computer == "P") or (player == "P" and computer == "R"):
    print("You win!")
else:
    print("You lose.")
