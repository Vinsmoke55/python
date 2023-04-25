# program for counting the squirrel with the fur color 
import pandas

data=pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

color_list=data["Primary Fur Color"].to_list()


gray_no=0
black_no=0
Cinnamon_no=0
for color in color_list:
	if color=="Gray":
		gray_no+=1
	elif color=="Black":
		black_no+=1
	elif color=="Cinnamon":
		Cinnamon_no+=1

color_dict={
	"Fur_Color":["Gray","Black","Cinnamon"],
	"Count":[gray_no,black_no,Cinnamon_no]
}

squirrel_count=pandas.DataFrame(color_dict)

squirrel_count.to_csv("squirrel_count.csv")