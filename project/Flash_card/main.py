from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data=pandas.read_csv("./data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}

def next_card():
	global current_card,flip_timer
	window.after_cancel(flip_timer)
	current_card=random.choice(to_learn)
	canvas.itemconfig(card_image,image=card_front)
	canvas.itemconfig(card_title,text=f"French",fill="black")
	canvas.itemconfig(card_word,text=f'{current_card["French"]}',fill="black")
	flip_timer=window.after(3000,func=flip_card)

def flip_card():
	global current_card
	canvas.itemconfig(card_image,image=card_back)
	canvas.itemconfig(card_title,text=f"English",fill="white")
	canvas.itemconfig(card_word,text=f'{current_card["English"]}',fill="white")


# creating the user interface
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file="./images/card_back.png")
card_image=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")
right_button=Button(image=right,highlightthickness=0,command=next_card)
right_button.grid(row=1,column=0)

wrong_button=Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=1)

next_card()

mainloop()
