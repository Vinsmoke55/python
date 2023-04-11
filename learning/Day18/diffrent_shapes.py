from turtle import Turtle,Screen

tim=Turtle()

angle=0
sides=2
condition=True
while condition:
	angle=360/sides
	for _ in range(sides):
		tim.forward(50)
		tim.right(angle)
	sides+=1
	if sides==11:
		condition=False
	
	


screen=Screen()
screen.exitonclick()
