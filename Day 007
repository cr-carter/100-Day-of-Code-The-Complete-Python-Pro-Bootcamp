#The purpose of this project is to get more experience using while and for loops, including loops within loops.
#Additionally, this project also is to work more on logic within programs.
#Experience was also gained in string splitting, checking user input, and converting between variable types.
#I also included a comment that is code that should pull a larger list of words from the dictionary included on *nix systems.
#What I did not do in this program that was done in the Udemy course was include ascii art, as this did not provide any value.


import random
word_list = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
#Alternative, pull from local file on *nix systems
#word_file = "/usr/share/dict/words"
#word_list = open(word_file).read().splitlines()

#Variables needed. display will be what is shown to the user, guesses will store all guesses, correct and incorrect will store respective guesses, letter_guess will be current guess
word = random.choice(word_list).lower()
display = "_" * len(word)
guesses = []
correct = []
incorrect = []
letter_guess = "  "
attempts_allowed = 0
attempts_made = 0

#Ask user how many tries they would like after seeing the number of blanks.
#Use "try" and "except" to check if user entered an integer
print(f"Guess the word:\n{display}")
while attempts_allowed < 1:
    try_request = input("How many guesses would you like?: ")
    try:
        attempts_allowed = int(try_request)
    except:
        attempts_allowed = 0

while "_" in display and attempts_allowed > attempts_made:
    #Prompt user for a letter, check that it has not already been guessed,
    #and that it is a single letter
    while letter_guess in guesses or len(letter_guess) > 1:
        letter_guess = input("Enter a letter you have not already guessed:").lower()
    guesses.append(letter_guess)

    #Check if the guess is in the word. If it is, then cycle through the word,
    #find where the guess is located in the word, and replace the "_" in the display
    if str(letter_guess) in str(word):
        print("Good guess")
        for i in range (0, len(word)):
            if letter_guess == word[i]:
                display = display[:i] + letter_guess + display[i+1:]
        correct.append(letter_guess)
    else:
        print("Bad guess")
        incorrect.append(letter_guess)
        attempts_made += 1
    print(display + "    Lives left: " + str(attempts_allowed - attempts_made) + "  Wrong Guesses: " + str(incorrect) + "\n")
    

#Check if the user has guessed the entire word
if display == word:
    print("You win!")
else:
    print("You lose!")
