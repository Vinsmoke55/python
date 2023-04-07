#importing the class Turtle and Screen from turtle graphics module
from turtle import Turtle,Screen

tom=Turtle()	#here tom is a object and Turtle is the class name
print(tom)
tom.shape("turtle")	#changing the shape of tom to turtle uding shape method inside Turtle class
tom.color("coral")	#changing the color of tom to coral using color method inside Turtle class
tom.forward(100)	#making the tom move 100 pace

my_screen=Screen()	#here my)screen is object and Screen is class 
print(my_screen.canvheight)	#printing the height of the screen which is the attribute canvheight in Screen class
my_screen.exitonclick()	#making the screen exit only on cick using exitonclick method in Screen class