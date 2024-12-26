#The purpose of this project was to work with multiple lists and other variables,
#giving a user multiple choices of input, focusing on logic, and validating user input.

#Function to create a cipher alphabet to encode/decode the user message
def create_cipher(direction, letters):
    cipher = []
    if direction == "encode":
        for i in range(0,26):
            if i + shift < 26:
                cipher.append(alphabet[i + shift])
            else:
                cipher.append(alphabet[(i + shift) - 26])
    else:
        for i in range(0,26):
            if i - shift >= 0:
                cipher.append(alphabet[i - shift])
            else:
                cipher.append(alphabet[(i - shift) + 25])
    return cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = True

#variables are defined at the start of the while loop in order to reset them after each iteration
while run:
    cipher_alphabet = []
    message = ""
    cipher_message = ""
    encode_decode = ""
    shift = 0

    while encode_decode != "encode" and encode_decode != "decode":
        encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    message = input("Type your message:\n").lower()

    while not shift > 0 or not shift < 26:
        shift_input = input("Type the shift number (1-25):\n")
        try:
            shift = int(shift_input)
        except:
            print("Please type a number between 1 and 25.")

    cipher_alphabet = create_cipher(encode_decode, alphabet)

    #Cycle through each letter in the user message, apply cipher to it
    for i in range(0, len(message)):
        letter = message[i]
        if letter in alphabet:
            index = alphabet.index(letter)
            cipher_message += cipher_alphabet[index]
        else:
            cipher_message += letter

        print(f"Here is the {encode_decode}d result:\n{cipher_message}")
    
    again = ""
    while not again == "yes" and not again == "no":
        again = input("Do you want to go again? (yes/no)\n")
    if again == "no":
        run = False
