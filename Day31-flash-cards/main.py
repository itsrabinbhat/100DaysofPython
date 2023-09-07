from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------- WORKING WITH CSV FILE ----------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')
current_card = {}
words_to_learn = {'French': data.French.to_list(), 'English': data.English.to_list()}


def remove_word():
    words_to_learn['French'].remove(current_card['French'])
    words_to_learn['English'].remove(current_card['English'])
    to_learn.remove(current_card)
    gen_new_card()


def gen_new_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    if len(to_learn) == 0:
        to_learn = [{'French': "You've completed the basic.", 'English': "You've completed the basic."}]

    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(lang_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


# ------------------------------- UI SETUP ------------------------------------- #
window = Tk()
window.title('French - English flashcards')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=810, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
canvas_img = canvas.create_image(410, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=remove_word)
right_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=gen_new_card)
wrong_btn.grid(row=1, column=0)

lang_text = canvas.create_text(400, 150, text="title", font='Helvetica 32 italic')
word_text = canvas.create_text(400, 265, text="word", font="Helvetica 42 bold")

gen_new_card()

window.mainloop()

print('Progress Saved...')
pandas.DataFrame(words_to_learn).to_csv('data/words_to_learn.csv')
