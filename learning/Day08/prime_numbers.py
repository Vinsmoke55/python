#Write your code below this line 👇
def prime_checker(number):
	condition=0
	for no in range(2,6):
		if number%no==0:
			condition+=1
	if condition !=0:
		print("It's not a prime number.")
	else:
		print("It's a prime number.")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
