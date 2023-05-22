from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

	def __init__(self,quizbrain:QuizBrain):
		self.quiz=quizbrain
		self.window=Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20,pady=20,bg=THEME_COLOR)

		self.score=Label(text="score:0",fg="white",bg=THEME_COLOR)
		self.score.grid(row=0,column=1)

		self.canvas=Canvas(height=250,width=300,bg="white")
		self.question_text=self.canvas.create_text(150,120,text="some question",width=280,font=("Arial",20,"italic"),fill=THEME_COLOR)
		self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

		false_img=PhotoImage(file="./images/false.png")
		true_img=PhotoImage(file="./images/true.png")


		self.true_button=Button(image=true_img,highlightthickness=0)
		self.true_button.grid(row=2,column=0)

		self.false_button=Button(image=false_img,highlightthickness=0)
		self.false_button.grid(row=2,column=1)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		q_text=self.quiz.next_question()
		self.canvas.itemconfig(self.question_text,text=q_text)

