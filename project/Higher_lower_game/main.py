import random
import os
from art import logo,vs
from game_data import data


score=0
condition=True

#playing the game till the given choice is false which is implemented by loop
while condition:

	#printing the logo of Higher lower
	print(logo)

	#assigning a random choice from data list for first thing
	first_person=random.choice(data)

	#assigning a random choice form data list for against
	second_person=random.choice(data)

	#if same value is assigned from the list to both the variables then again assigning the value
	if first_person==second_person:
		second_person=random.choice(data)

	#displaying the information about the first and second variable
	print(f'Compare A: {first_person["name"]}, a {first_person["description"]}, from {first_person["country"]}.')
	print(vs)
	print(f'Against B: {second_person["name"]}, a {second_person["description"]}, from {second_person["country"]}.')

	#taking the input for the choice which the user think may have more followers
	choice=input("Who has more followers? Type 'A' or 'B': ")

	#checking if the first or the second variable have more follower and following the condition statements
	followers_checking=first_person["follower_count"]>second_person["follower_count"]
	if choice=='A' and followers_checking:
		score+=1
		print(f"You are right! The current score is : {score}")
	elif choice=='B' and not followers_checking:
		score+=1
		print(f"You are right! The current score is : {score}")
	else:
		print(f"sorry, that's wrong. Final score: {score}")
		condition=False

	#clearing the screen after each level of the game
	os.system('clear')


