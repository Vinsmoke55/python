# number guessing game
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
number=random.randint(1,100)
print(number)
condition=True
if level=='easy':	#if easy is chosen you will get 10 attempts
	attempts=10
	print(f"You have {attempts} attempts remaining to guess the number.")
else:	#if hard is chosen you will get 5 attempts to guess the number
	attempts=5
	print(f"You have {attempts} attempts remaining to guess the number.")
while condition:
	
	guess=int(input("Make a guess: "))
	if guess<number:
		attempts-=1
		print("Too Low")
		print(f"You have {attempts} attempts remaining to guess the number.")
	elif guess>number:
		attempts-=1
		print("Too high")
		print(f"You have {attempts} attempts remaining to guess the number.")
	else:		#if guess is correct then you win
		print(f"your guess {guess} is correct .YOU WIN")
		condition=False
	if attempts==0:		#if there is no attempt left then you lose
		print("YOU LOSE")
		condition=False

