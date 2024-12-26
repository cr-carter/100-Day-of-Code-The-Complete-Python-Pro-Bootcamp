'''
The purpose of thie project was to gain experience with tkinter, using a better gui than turtle.
I gained experience with various widgets in tkinter, including labels, buttons, entry boxes,
text boxes, spinboxes, scales, check buttons, radio buttons, and list boxes. I also learned
how to apply functionality to each of those widgets.
'''

from tkinter import *

window = Tk()
window.title("Mile-Kilometer Converter")
window.minsize(width=200, height=200)

user_input = Entry(width=20)
user_input.insert(END, string="Enter distance.")
user_input.grid(column=1, row=1)

radio_state = IntVar()
radio_state.set(1)
radiobutton1 = Radiobutton(text="Miles to Kilometers", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="Kilometers to Miles", value=2, variable=radio_state)
radiobutton1.grid(column=1, row=2)
radiobutton2.grid(column=1, row=3)


def button_clicked():
    try:
        distance = float(user_input.get())
        if radio_state.get() == 1:
            new_distance = distance * 1.61
            label.config(text=f"{str(distance)} mile(s) = {str(new_distance)} kilometer(s)")
        elif radio_state.get() == 2:
            new_distance = distance * 0.62
            label.config(text=f"{str(distance)} kilometer(s) = {str(new_distance)} mile(s)")
    except:
        label.config(text="Enter a number.")


button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=4)

label = Label(text="", font=("Arial", 12))
label.grid(column=1, row=5)

window.mainloop()
