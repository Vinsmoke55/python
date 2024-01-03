# # this is a python class

# class Car:
# 	name="lamborgini"

# car1=Car()
# print(car1.name)




# # the init function

# class Car:
# 	def __init__(self):
# 		self.name="ferrari"
# 		self.no=2234

# 	def concat(self):
# 		print(self.name,self.no)

# car2=Car()
# car2.concat()



# # init function with arguments

# class Car:
# 	def __init__(self,name,no):
# 		self.name=name
# 		self.no=no

# 	def concat(self):
# 		print(self.name,self.no)

# car2=Car("mercedes",2545)
# car2.concat()




# # Inheritance

# class Car:
# 	def __init__(self,name,no):
# 		self.name=name
# 		self.no=no

# 	def concat(self):
# 		print(self.name,self.no)

# class Boat(Car):
# 	pass

# boat1=Boat("ank",2)
# boat1.concat()


# # if init function in used inside child class then it do not inherit init from child class
# # so the code below will give error

# class Car:
# 	def __init__(self,name,no):
# 		self.name=name
# 		self.no=no

# 	def concat(self):
# 		print(self.name,self.no)

# class Boat(Car):
# 	def __init__(self):
# 		self.brand="ayush"

# boat1=Boat("ank",2)
# boat1.concat()



# #so to solve above problem super() is used

# class Car:
# 	def __init__(self,name,no):
# 		self.name=name
# 		self.no=no

# 	def concat(self):
# 		print(self.name,self.no)

# class Boat(Car):
# 	def __init__(self,name,no):
# 		# super().__init__(name,no)	#instead of super() we can also use parents class name but self has to be added as argument
# 		Car.__init__(self,name,no)
# 		self.brand=2

# boat1=Boat("ank",2)
# boat1.concat()
# print(boat1.brand)

