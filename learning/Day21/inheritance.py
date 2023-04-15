class Animal:
	no_of_eyes=2

	def breathe(self):
		print("Inhale ,Exhale")


class Dog(Animal):
	def __init__(self):
		super().no_of_eyes
	def takebreathe(self):
		super().breathe()

jack=Dog()
jack.takebreathe()
print(jack.no_of_eyes)