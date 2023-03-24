import random #importing a random module
import myModule

#to generate a random integer from 0 to 10
random_int=random.randint(0,10)		
print(random_int)

#to generate a float from 0.000 to 0.999
random_float=random.random()
print(random_float)

#to call from a external module
print(myModule.name)


