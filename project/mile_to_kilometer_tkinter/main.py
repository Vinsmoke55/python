from tkinter import *

window=Tk()
window.title("Mile to Kilomter converter")
window.minsize(width=500,height=300)


def click_command():
	input_text=int(entry.get())
	answer_value=calculate(input_text)
	answer_label["text"]=answer_value

def calculate(value):
	return value*1.60934


entry=Entry(width=10)
entry.grid(column=2,row=1)

label=Label(text="Miles")
label.grid(column=3,row=1)

second_label=Label(text="is equal to ")
second_label.grid(column=1,row=2)

answer_label=Label(text="0")
answer_label.grid(column=2,row=2)

km_label=Label(text="KM")
km_label.grid(column=3,row=2)

button=Button(text="Calculate",command=click_command)
button.grid(column=2,row=3)


window.mainloop()