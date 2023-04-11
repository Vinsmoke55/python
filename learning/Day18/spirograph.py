import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

tim.speed("fastest")

def color_picker():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	color=(r,g,b)
	return color

def draw_spirograph(size):
	for _ in range(int(360/size)):
		tim.color(color_picker())
		tim.circle(100)
		tim.setheading(tim.heading()+10)

draw_spirograph(10)
		

screen=t.Screen()
screen.exitonclick()