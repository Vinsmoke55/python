from turtle import Turtle,Screen
import random

tim=Turtle()

colors=["antiquewhite4","aquamarine","azure4","blueviolet","brown2","cadetblue","chocolate1","darkorchid"]
angle=[0,90,180,270]
tim.width(15)
tim.speed("fastest")
for _ in range(200):
	tim.color(random.choice(colors))
	tim.forward(30)
	tim.setheading(random.choice(angle))

screen=Screen()
screen.exitonclick()
