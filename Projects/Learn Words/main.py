
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
curretCard= {}
to_learn={}
try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn=orignal_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global curretCard,flip_timer
    window.after_cancel(flip_timer)
    curretCard=random.choice(to_learn)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word, text=curretCard["French"],fill="black")
    canvas.itemconfig(bgImage, image=card_front)
    flip_timer=window.after(3000, func=flip)


def is_known():
    to_learn.remove(curretCard)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


def flip():
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=curretCard["English"],fill="white")
    canvas.itemconfig(bgImage,image=card_back)

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")

canvas.create_text(200,150)

bgImage=canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

title=canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

card_right=PhotoImage(file="images/right.png")
tick_button=Button(image=card_right,highlightthickness=0,command=is_known)
tick_button.grid(column=0,row=1)
card_wrong=PhotoImage(file="images/wrong.png")
cross_button=Button(image=card_wrong,highlightthickness=0,command=next_card)
cross_button.grid(column=1,row=1)


next_card()

window.mainloop()