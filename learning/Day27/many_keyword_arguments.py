## creating unlimited keyword argument requires two(**) signs
# def calculate(**kwargs):
# 	print(kwargs["sum"])
# 	print(kwargs["multiply"])

# calculate(sum=10,multiply=20)


class Car:
	def __init__(self,**kw):
		self.make=kw.get("make")
		self.model=kw.get("model")


car=Car(make=2000,model="lamborgini")
print(car.make)
print(car.model)