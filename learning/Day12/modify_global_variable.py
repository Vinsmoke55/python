#modifying the global variabl
num=1

def number_modifier():
	global num 		#we can use the global keyword to use global variable inside the local scope
	num=2
	print(num)

number_modifier()
print(num)



