##to make a colr palatte from a picture
# import colorgram

# colors=colorgram.extract('hirst.jpg',25)

# rgb_colors=[]
# for color in colors:
# 	r=color.rgb.r
# 	g=color.rgb.g
# 	b=color.rgb.b
# 	color_tuple=(r,g,b)
# 	rgb_colors.append(color_tuple)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim=t.Turtle()
color=[(236, 235, 240), (236, 231, 234), (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111)]

tim.speed("fastest")	#making the speed of turltle fast
tim.hideturtle()		#hiding the arrow show while drawing
tim.penup()				#no showing the line while moving
tim.setheading(225)		#moving the turltle by 255 degree
tim.forward(300)		#moving the turtle by 300 paces
tim.setheading(0)		#and turning to right

for dot_count in range(1,101):
	tim.dot(20,random.choice(color))	#drawing the dot with thickness 20 and random color form color[]
	tim.forward(50)						#moving forward by 50 pace and again drawing throught the loop
	if dot_count%10==0:					#if 10 dots are made then run if statement
		tim.setheading(90)				#face up
		tim.forward(50)					#move up by 50 paces
		tim.setheading(180)				#turn left
		tim.forward(500)				#go forward to the left by 500 paces
		tim.setheading(0)				#and face forward



screen=t.Screen()
screen.exitonclick()