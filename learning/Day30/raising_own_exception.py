height=int(input("Enter your heihgt: "))
weight=int(input("enter your weight: "))

if height>3:
	raise ValueError("Human height cannot be greater then 3 m")	#we can create our own error and the code will not proceed forward

bmi=weight/height**2
print(bmi)