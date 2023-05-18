from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file="./images/card_back.png")
canvas.create_image(400,263,image=card_front)
canvas.create_text(400,150,text="french",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="trouve",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")
right_button=Button(image=right,highlightthickness=0)
right_button.grid(row=1,column=0)

wrong_button=Button(image=wrong,highlightthickness=0)
wrong_button.grid(row=1,column=1)

mainloop()
