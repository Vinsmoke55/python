from tkinter import *

window=Tk()
window.title("Button-GUI")
window.minsize(width=500,height=300)

# label
my_label=Label(text="this is a label",font=("ariel",22,"bold"))
my_label["text"]="hello world!"
my_label.config(text="hello world!")
my_label.pack()

def button_function():
	my_label.config(text="you clicked the button")
	print(entry.get())
	

# Button
button=Button(text="click me",command=button_function)
button.pack()

# entry
entry=Entry(width=10)
entry.pack()


window.mainloop()