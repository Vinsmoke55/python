import tkinter

window=tkinter.Tk()	#creating the window
window.title("My first GUI")
window.minsize(width=500,height=300) #setting up the window size

#label
my_label=tkinter.Label(text="I am a label",font=("Arial","25","bold"))
my_label.pack()

window.mainloop()