from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

	def __init__(self,quizbrain:QuizBrain):
		self.quiz=quizbrain
		self.window=Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20,pady=20,bg=THEME_COLOR)

		self.qsn=Label(text=f"Score: 0",fg="white",bg=THEME_COLOR)
		self.qsn.grid(row=0,column=1)

		self.canvas=Canvas(height=250,width=300,bg="white")
		self.question_text=self.canvas.create_text(150,120,text="some question",width=280,font=("Arial",20,"italic"),fill=THEME_COLOR)
		self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

		false_img=PhotoImage(file="./images/false.png")
		true_img=PhotoImage(file="./images/true.png")


		self.true_button=Button(image=true_img,highlightthickness=0,command=self.true_pressed)
		self.true_button.grid(row=2,column=0)

		self.false_button=Button(image=false_img,highlightthickness=0,command=self.false_pressed)
		self.false_button.grid(row=2,column=1)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg="white")
		if self.quiz.still_has_questions():
			self.qsn.config(text=f"Score: {self.quiz.score}")
			q_text=self.quiz.next_question()
			self.canvas.itemconfig(self.question_text,text=q_text)
		else:
			self.canvas.itemconfig(self.question_text,text="You have reached the end.")
			self.true_button.config(state="disable")
			self.false_button.config(state="disable")

	def true_pressed(self):
		is_right=self.quiz.check_answer("True")
		self.give_feedback(is_right)

	def false_pressed(self):
		is_right=self.quiz.check_answer("False")
		self.give_feedback(is_right)

	def give_feedback(self,is_right):
		if is_right==True:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")
		self.window.after(1000,self.get_next_question)
		


