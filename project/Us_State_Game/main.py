from turtle import Turtle,Screen
import pandas

screen=Screen()
turtle=Turtle()
t=Turtle()

#setting up image as the background for the screen
screen.title("Us State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




data=pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()
guessed_state=[]

while len(guessed_state)<50:
	guess=screen.textinput(title=f"{len(guessed_state)}/50 correct",prompt="What's another state name ? ").title()
	
	if guess in states_list:
		correct_state=data[data.state==guess]
		t.penup()
		t.hideturtle()
		t.goto(int(correct_state.x),int(correct_state.y))
		t.write(guess)
		guessed_state.append(guess)
	
		