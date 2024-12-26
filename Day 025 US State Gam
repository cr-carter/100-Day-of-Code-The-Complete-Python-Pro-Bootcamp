'''
The purpose of this project is to practice with CSV files, both reading and creating them.
This was done using the pandas library.
I also gained more experience with accepting user input, handling different scenarios (such
as the user clicking 'cancel' instead of inputting text.
'''

import pandas
import turtle

screen = turtle.Screen()
screen.title("USA States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data["state"].tolist()

t = turtle.Turtle()
t.hideturtle()
t.penup()

while len(all_states) > 0:
    answer_state = screen.textinput(title=f"{len(all_states)} states remaining", prompt="Enter a state's name.")
    if answer_state is None:
        break
    else:
        answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        answer_data = data[data["state"] == answer_state]
        t.goto(answer_data.x.item(), answer_data.y.item())
        t.write(answer_data.state.item())
        all_states.remove(answer_data.state.item())

#Export unnamed states to a CSV file
states_to_learn = pandas.DataFrame(all_states)
states_to_learn.to_csv("states_to_learn.csv")

turtle.mainloop()
