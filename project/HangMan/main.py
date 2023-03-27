#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#To randomly choose a word from the word_list and assigning it to a variable called chosen_word.
chosen_word=random.choice(word_list)
print(chosen_word)

#To ask the user to guess a letter and assign their answer to a variable called guess. Making guess lowercase.
guess=input("Guess the letter:").lower()

#To check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
	if guess==letter:
		print('right')
	else:
		print('wrong')
