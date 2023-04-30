# unlimited positional arguments
# * and a name is used inside the function arguments which is represented as a tuple 
def add(*args):
	sum=0
	for n in args:
		sum+=n
	return sum


print(add(1,2,3))