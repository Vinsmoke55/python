#program for the hangman game

import random
from hangman_art import logo,stages
from hangman_words import word_list

# Updating the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#using logo form hangman_art which we imported at the top
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks for the words
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and letting them know.
    if guess in display:
        print(f"you have already guessed the letter {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #printing out and letting know that the entered letter is not in the word and decrementing life
        print("The letter you guessed in not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Joining all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #printing the hangman form the hangman_art module that we imported stages
    print(stages[lives])