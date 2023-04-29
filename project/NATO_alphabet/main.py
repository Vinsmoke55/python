

import pandas
# Creating a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data=pandas.read_csv("nato_phonetic_alphabet.csv")

data_dictionary={rows.letter:rows.code for (index,rows) in data.iterrows()}


# Creating a list of the phonetic code words from a word that the user inputs.

user_input=input("Enter a word: ").upper()

words=[data_dictionary[letter] for letter in user_input]
print(words)

