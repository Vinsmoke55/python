# function with more than 1 inputs
def greet(name,address):
	print(f"Hello {name}")
	print(f"whats the weather in {address}")


greet("ayush","kathmandu")	#positional argument: the value is assigned to parameter in order of the argument


greet(address="canada",name="aaron")	#keyword argument :this resolves the problem in positional argument