from turtle import Screen,Turtle

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")

starting_position=[(0,0),(-20,0),(-40,0)]

for position in starting_position:
	new_segment=Turtle(shape="square")
	new_segment.color("white")
	new_segment.goto(postion[index],0)

screen.exitonclick()