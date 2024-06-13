#The purpose of this project is to practice with if, elif, and else statements, and multiple if statements in succession.
#This project also uses logical operators, while loops, and string case manipulation. Not shown is practice using modulo (%).

print('''
   *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
         
      ''')
print("Welcome to Treasure Island.\nYour goal is to find the treasure.")
decision = ""
while decision != "left" and decision != "right":
    decision = input("You are walking down a path and find yourself at a fork in the road. Do you go left or right? (Type \"left\" or \"right\")\n").lower()

if decision == "right":
    print("You are attacked by a tiger. Game over.")
else:
    print("You continue walking down the path.")

    decision = ""
    while decision != "wait" and decision != "swim":
        decision = input ("You come to a dock on a lake. You see an island in the distance. Do you wait for a boat or attempt to swim? (Type \"wait\" or \"swim\")\n").lower()

    if decision == "swim":
        print("You are attacked by a shark. Game over.")
    else:
        print("A boat floats toward the dock. You get on and row to the island.")

        decision = ""
        while decision != "red" and decision != "yellow" and decision != "blue":
            decision = input("You dock on the island, and see three mysterious doors. Do you choose the red, yellow, or blue door? (Type \"red\", \"yellow\", or \"blue\")\n").lower()
    
        if decision == "red":
            print("It's a room of fire. Game over.")
        elif decision == "blue":
            print("It's a room full of beasts. Game over.")
        else:
            print("You found the treasure! You win!")

