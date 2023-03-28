import random
word_list = ["aardvark", "baboon", "camel"] 
chosen_word = random.choice(word_list)


print(f'the solution is {chosen_word}.')


display=[]
word_length=len(chosen_word)

# showing the _ for the character in chosen_word
for _ in range(word_length):
	display+='_'
print(display)

end_of_game=False
# looping till the _ sign is all removed in display
while not end_of_game:
	guess = input("Guess a letter: ").lower()


	for position in range(word_length):
		letter=chosen_word[position]
		if letter==guess:
			display[position]=letter

	print(display)
	if "_" not in display:
		end_of_game=True
		print('you win')


