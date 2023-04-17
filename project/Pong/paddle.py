from turtle import Turtle

class Paddle(Turtle):
	def __init__(self,coordinate):
		super().__init__()
		self.penup()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5,stretch_len=1)	#all turtle start at 20,20 making it 100,20
		self.goto(coordinate)

	def go_up(self):
		new_y=self.ycor()+20
		self.goto(self.xcor(),new_y)


	def go_down(self):
		new_y=self.ycor()-20
		self.goto(self.xcor(),new_y)
