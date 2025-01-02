'''
The purpose of this project is to gain experience with opening, editing, and creating
files using Python. I also gained experience using the "with ... as" statement.
I also received more practice modifying strings, such as the "splitlines" and "replace"
functions. Lastly, the Udemy course taught relative and absolute file paths, which I
already had experience with as a system and network adminstrator.
'''

with open("/Users/Chase/PycharmProjects/pythonProject/Input/Names/invited_names.txt", mode="r") as name_document:
    name_list = name_document.read().splitlines()

with open("/Users/Chase/PycharmProjects/pythonProject/Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_template = letter.read()

for name in name_list:
    with open(f"/Users/Chase/PycharmProjects/pythonProject/Output/ReadyToSend/{name}_letter", mode="w") as custom_letter:
        new_letter = letter_template.replace("[name]", name)
        custom_letter.write(new_letter)
