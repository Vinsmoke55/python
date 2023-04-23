#taking the name in invited_names.txt and storing them in list using readlines()
with open("./Input/Names/invited_names.txt",mode="r") as file:
	content=file.readlines()
	
# Create a letter using starting_letter.txt 
with open("./Input/letters/starting_letter.txt") as file:
	letter=file.read()
	

#for each name in invited_names.txt
for name in content:
	each=name.strip()
	with open(f"./Output/ReadyToSend/letter_for_{each}.txt",mode="w") as file:
		final_letter=letter.replace("[name]",f"{each}")	#Replacing the [name] placeholder with the actual name.
		file.write(final_letter)	#Saving the letters in the folder "ReadyToSend".