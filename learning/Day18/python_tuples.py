import turtle as t
import random


tim=t.Turtle()
t.colormode(255)
def color_picker():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	random_color=(r,g,b)
	return random_color

colors=["antiquewhite4","aquamarine","azure4","blueviolet","brown2","cadetblue","chocolate1","darkorchid"]
angle=[0,90,180,270]
tim.width(15)
tim.speed("fastest")
for _ in range(200):

	tim.color(color_picker())
	tim.forward(30)
	tim.setheading(random.choice(angle))

screen=t.Screen()
screen.exitonclick()
