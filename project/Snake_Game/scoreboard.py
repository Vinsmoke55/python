from turtle import Turtle,Screen
ALIGNMENT="center"
FONT=("ariel",20,"normal")

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score=0
		self.high_score=0
		self.goto(0,270)
		self.color("white")
		self.scoreboard_text()
		self.hideturtle()

	def scoreboard_text(self):
		self.clear()
		self.write(f"SCORE: {self.score} HIGH SCORE:{self.high_score}",align=ALIGNMENT,font=FONT)

	def increase_score(self):
		self.score+=1
		self.scoreboard_text()

	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)


	def reset(self):
		if self.score>self.high_score:
			self.high_score=self.score
		self.score=0
		self.scoreboard_text()

		
		