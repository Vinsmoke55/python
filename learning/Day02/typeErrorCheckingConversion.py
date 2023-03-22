# #Type error
# #the code below will generate a type error because length is  a string
# length=len(input("what is your name?"))
# print("your name is "+length+" character long")

#Type checking 
#we can check the data type of the with type function
my_name="ayush"
print(type(my_name))

#Type conversion
#we can convert the data type as follow so that the above type error code runs
length=len(input("what is your name?"))
new_length=str(length)
print("your name is "+new_length+" character long")
