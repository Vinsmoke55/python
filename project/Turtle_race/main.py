from turtle import Turtle,Screen
import random

screen=Screen()

#lists to store the values
color=["red","blue","yellow","green","orange","purple"]
turtle_position=[-170,-115,-50,15,80,155]
turtles=[]

#setting the size of the screen
screen.setup(width=500,height=400)
# taking the user input in a popup window
user_bet=screen.textinput(title="Make a bet.",prompt="Which turtle will win the race? Chooe a color: ")

# creating six turtles ,setting their color and sending them to starting position
for index in range(0,6):
	new_turtle=Turtle(shape="turtle")
	new_turtle.color(color[index])
	new_turtle.penup()
	new_turtle.goto(-240,turtle_position[index])
	turtles.append(new_turtle)

#setting condition for loop after user makes the bet
if user_bet:
	race_is_on=True

#making the turtle move randomly
while race_is_on:
	for turtle in turtles:
		if turtle.xcor()>230:	#if any turtle coordinate is greater than 230 exit the loop and taking the color of turtle in a variable
			race_is_on=False
			won_color=turtle.color()
		turtle.forward(random.randint(0,10))
		
#making the user know if he won or lose and which turtle won
if user_bet.lower==won_color[1]:
	print(f"You won the bet!!\n{won_color[1]} turtle won the race")
else:
	print(f"You lost the bet!!\n{won_color[1]} turtle won the race")



screen.exitonclick()