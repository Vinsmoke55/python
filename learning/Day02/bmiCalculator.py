# bmi calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_m=float(height)
weight_kg=int(weight)
bmi=weight_kg/(height_m**2)
print(int(bmi))
