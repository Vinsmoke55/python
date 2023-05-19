from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data=pandas.read_csv("./data/french_words.csv")
to_learn=data.to_dict(orient="records")

def next_card():
	current_card=random.choice(to_learn)
	canvas.itemconfig(card_title,text=f"French")
	canvas.itemconfig(card_word,text=f'{current_card["French"]}')





# creating the user interface
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file="./images/card_back.png")
canvas.create_image(400,263,image=card_front)
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
