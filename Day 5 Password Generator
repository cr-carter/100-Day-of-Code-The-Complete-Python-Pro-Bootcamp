#The purpose of this project is to practice with for loops, random functions, and converting strings to lists and vice versa

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "|", ":", ";", "\"", "'"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(len("B2['!kLd$8D242oEO=pw"))
print("Welcome to the PyPassword Generator!")
low = int(input("How many lowercase letters would you like in your password?\n"))
up = int(input("How many uppercase letters would you like in your password?\n"))
sym = int(input("How many symbols would you like in your password?\n"))
num = int(input("How many numbers would you like in your password?\n"))

import random
password = ""
for i in range (1, low + 1):
    password += random.choice(lowercase)
for i in range(1, up + 1):
    password += random.choice(uppercase)
for i in range(1, sym + 1):
    password += random.choice(symbols)
for i in range(1, num + 1):
    password += random.choice(numbers)

#I originally built this program using a for loop that would take a character position from the password,
# and add it to the "random_password" string. I then used string spliting to remove the character from the
# "password" string. However, I then read about using the random.shuffle function, so I changed the code. 
#random_password = ""
#for i in range(0, len(password)):
#   x = random.randint(0,len(password)-1)
#   random_password += password[x]
#   password = password[:x] + password[x+1:]

password = list(password)
random.shuffle(password)
random_password = ""
for char in password:
    random_password += char

print(f"Your password is: {random_password}")
