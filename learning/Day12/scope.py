# local scope
def name():
	my_name='ayush'
	print(my_name)

name()
# print(my_name)	#this line will give an error because my_name is have a local scope



# global scope

dog_name="jack"

def pet_name():
	print(dog_name)

pet_name()
print(dog_name)	#this line wil not give error becuase dog_name have global scope