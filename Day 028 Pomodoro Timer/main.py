'''
The purpose of this project was to gain further experience with tkinter. I gained exposure to the use of
the .after method to count the passage of time within tkinter. I also gained exposure to more of the 
methods and attributes of various tkinter widgets. A focus was also placed on recursive or self-referencing
functions.
'''
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 36, "bold")
BUTTON_FONT = ("Courier", 18, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig("timer_text", text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global reps, timer
    minutes_left = math.floor(seconds / 60)
    seconds_left = seconds % 60
    canvas.itemconfig("timer_text", text=f"{minutes_left:02d}:{seconds_left:02d}")
    if seconds > 0:
        seconds -= 1
        timer = window.after(1000, count_down, seconds)
    else:
        window.lift()
        work_sessions = math.floor(reps%2)
        start_timer()
        check_marks.config(text=(work_sessions * "✔"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=60, pady=60, bg=YELLOW)
window.resizable(width=False, height=False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_background = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_background)
canvas.create_text(100, 128, text=f"{0:02d}:{0:02d}", fill="white", font=FONT, tags=("timer_text",))
canvas.grid(column=1, row=1)

timer_label = Label()
timer_label.config(text="Timer", font=FONT, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(bg=YELLOW, highlightthickness=1, bd=0)
start_button.config(text="Start", font=BUTTON_FONT, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(bg=YELLOW, highlightthickness=1, bd=0)
reset_button.config(text="Reset", font=BUTTON_FONT, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
