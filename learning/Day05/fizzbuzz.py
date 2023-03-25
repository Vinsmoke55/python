#program for fizzbuzz game form 1 to 100
for n in range(1,100):
	if n%5==0 and n%3==0:
		print("FizzBuzz")
	elif n%3==0:
		print("Fizz")
	elif n%5==0:
		print("Buzz")
	else:
		print(n)