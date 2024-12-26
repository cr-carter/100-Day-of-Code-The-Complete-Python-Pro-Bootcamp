'''
The purpose of this project was to gain experience with list comprehension. This was in order
to make code shorter, more concise, and easier to read. List comprehension also was applied to
dictionary comprehension. Further experience was gained with pandas and reading CSVs. I also
wanted to start practicing more with error handling, such as the user inputting a character other
than an alphabetic character.
'''

import pandas

nato_alphabet_csv = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_csv.iterrows()}

word = input("Enter a word:")
try:
    phonetic = [nato_alphabet[letter.capitalize()] for letter in word]
    print(phonetic)
except:
    print("Only use alphabetic characters.")

