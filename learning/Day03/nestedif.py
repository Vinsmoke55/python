# control flow
# control flow is use to control the flow of program with the given conditon
print("Welcome to the Roller Coster")
height=int(input("Enter your height in cm? "))
if height>120:
	print("You can ride the roller coaster")
	age=int(input("Enter your age:"))
	if age<12:		#it is a conditon inside condition so called as nested
		print("You should pay $5")
	elif age>=12&age<=18:
		print("you should pay $7")	#with the help of elif we can check as many condition as we wan
	else:
		print("You should pay $12")
else:
	print("You have to grow more taller to ride the roller coaster")