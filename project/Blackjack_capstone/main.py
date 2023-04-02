############### Blackjack Project #####################

import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
	return random.choice(cards)

restart=True
while restart:
	print(logo)
	#Deal the user and computer 2 cards each using deal_card() and append().
	user_cards = []
	computer_cards = []
	user_cards.append(deal_card())
	user_cards.append(deal_card())
	computer_cards.append(deal_card())
	computer_cards.append(deal_card())


	#Create a function called calculate_score() that takes a List of cards as input 
	#and returns the score. 
	#Look up the sum() function to help you do this.
	def calculate_score(list_of_cards):
		if sum(list_of_cards)==21:
			return 0
		elif list_of_cards[0]==11 or list_of_cards[1]==11:
			if sum(list_of_cards)>21:
				list_of_cards.remove(11)
				list_of_cards.append(1)
				return sum(list_of_cards)

		else:
			return sum(list_of_cards)


	# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
	# 0 will represent a blackjack in our game.

	# Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
	# You might need to look up append() and remove().

	# Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
	print(f"your cards are {user_cards}:The current score is {calculate_score(user_cards)}\nComputer first card is {computer_cards[0]}")
	game_end=0
	if calculate_score(user_cards)==0 or calculate_score(computer_cards)==0 or calculate_score(user_cards)>21:
		print("game ends")
	else:
		game_end=1
		print("game didnt end")


	# If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to 
	# add another card to the user_cards List. If no, then the game has ended.
	if game_end==1:
		another_card=input("do you want to draw another card. Type 'y' for yes and 'n' for no: ")
		if another_card=='y':
			user_cards.append(deal_card())
		else:
			print("game ends")

	

	# Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score 
	# less than 17.
	if calculate_score(computer_cards)<17:
		computer_cards.append(deal_card())

	# Creating a function called compare() and pass in the user_score and computer_score. If the computer and user both have the 
	# same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the 
	# user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. 
	# If none of the above, then the player with the highest score wins.
	def compare(computer_score,user_score):
		print(f"your cards are {user_cards}:The current score is {calculate_score(user_cards)}\nComputer card is {computer_cards}")
		if computer_score==user_score:
			print("Its a draw")
		elif computer_score==0:
			print("you lose")
		elif user_score==0:
			print("you win")
		elif user_score>21:
			print("you lose")
		elif computer_score>21:
			print("computer loses")
		else:
			if user_score>computer_score:
				print("user wins")
			else:
				print("computer wins")

	compare(calculate_score(computer_cards),calculate_score(user_cards))
	# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
	ask_user=input("do you want to restart type 'y' for yes and 'n' for no: ")
	os.system('clear')
	if ask_user=='n':
		restart=False
