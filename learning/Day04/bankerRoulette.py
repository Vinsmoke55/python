# Import the random module here
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_person=len(names)-1
random_no=random.randint(0,number_of_person)
print(f'{names[random_no]} is going to buy the meal today!')