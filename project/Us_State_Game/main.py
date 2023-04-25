from turtle import Turtle,Screen

screen=Screen()
turtle=Turtle()

#setting up image as the background for the screen
screen.title("Us State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state=screen.textinput(title="Guess the state",prompt="What's another state name ? ")

print(answer_state)