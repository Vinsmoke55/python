# there are three type of layout mangers in python pack(), place() and grid()
# the layout manager should be specifed for the gui to be shown on the screen
from tkinter import *

window=Tk()
window.title("Button-GUI")
window.minsize(width=500,height=300)
#adding the padding to the window
window.config(padx=100,pady=200)

#this code is for pack and place
# def button_function():
# 	my_label.config(text="you clicked the button")
# 	print(entry.get())

# # label
# my_label=Label(text="this is a label",font=("ariel",22,"bold"))
# my_label["text"]="hello world!"
# my_label.config(text="hello world!")
# my_label.pack()		#pack() packs the gui from top to bottom

# # Button
# button=Button(text="click me",command=button_function)
# button.place(x=100,y=200) 	#place() takes the x and y coordinate of the place to put in screen

# # entry
# entry=Entry(width=10)
# entry.pack()



#this code is for grid

def button_function():
	my_label.config(text="you clicked the button")
	print(entry.get())

# label
my_label=Label(text="this is a label",font=("ariel",22,"bold"))
my_label["text"]="hello world!"
my_label.config(text="hello world!")
my_label.config(padx=50,pady=50)
my_label.grid(column=1,row=1)		#adding padding to the label

# Button
button=Button(text="click me",command=button_function)
button.grid(column=2,row=2)

# new_button
new_button=Button(text="also click me",command=button_function)
new_button.grid(column=1,row=3)	


# entry
entry=Entry(width=10)
entry.grid(column=3,row=4)

window.mainloop()