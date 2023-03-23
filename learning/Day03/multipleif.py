# control flow is use to control the flow of program with the given conditon
print("Welcome to the Roller Coster")
height=int(input("Enter your height in cm? "))
bill=0
if height>120:
	print("You can ride the roller coaster")
	age=int(input("Enter your age:"))
	if age<12:		#it is a conditon inside condition so called as nested
		bill=5
		print(f"children bill is ${bill}")
	elif age>=12&age<=18:
		bill=7
		print(f"teen bill is ${bill}")	#with the help of elif we can check as many condition as we wan
	else:
		bill=12
		print(f"adult bill is ${bill}")

	photo=input("Do you want to take a photo? Y or N")
	if photo=="Y":
		bill+=3
	
	print(f"you should pay ${bill}")
else:
	print("You have to grow more taller to ride the roller coaster")