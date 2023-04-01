from art import logo
import os

#calculator

# for add
def add(n1,n2):
	return n1+n2

# for subtraction
def subtract(n1,n2):
	return n1-n2

# for division
def divide(n1,n2):
	return n1/n2

# for multiplication
def multiply(n1,n2):
	return n1*n2


# dictionary
operations={
	"+":add,
	"-":subtract,
	"/":divide,
	"*":multiply
}


def calculator():
	print(logo)
	num1=float(input("Input the first number: "))


	for key in operations:
		print(key)


	should_continue=True

	while should_continue:
		operation_symbol=input("Pick an operation")

		num2=float(input("Input the second number: "))

		calculation_function=operations[operation_symbol]
		answer=calculation_function(num1,num2)

		print(f"{num1} {operation_symbol} {num2}= {answer}")

		if input('Type "y" to continue and "n" to start new calculation : ')=="y":
			num1=answer
		else:
			should_continue=False
			os.system('clear')
			calculator()
calculator()
	