from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 1
checkmarks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, checkmarks, reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks = ""
    reps = 1
    checkmark.config(text=checkmarks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, checkmarks
    if reps == 8:
        timer_label.config(text="Long break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reps = 1
    elif reps % 2 == 1:
        timer_label.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 2 == 0:
        checkmarks += CHECKMARK
        checkmark.config(text=checkmarks)
        timer_label.config(text="Short break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    time_text = "{:02d}:{:02d}".format(count // 60, count % 60)
    canvas.itemconfig(timer_text, text=time_text)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=75, pady=35, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start_btn = Button(text='Start', command=start_timer, width=5, highlightthickness=0)
start_btn.grid(column=1, row=3)

reset_btn = Button(text='Reset', command=reset_timer, width=5, highlightthickness=0)
reset_btn.grid(column=3, row=3)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, 'normal'))
checkmark.grid(column=2, row=4)

window.mainloop()
