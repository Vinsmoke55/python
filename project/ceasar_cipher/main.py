alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#encrypting the message by moving the index to index+shift_amount
#and to prevent index out of range error adding alphabet two times in the list
def encrypt(plain_text,shift_amount):
	cipher_text=""
	for letter in plain_text:
		position=alphabet.index(letter)
		new_position=position+shift_amount
		new_letter=alphabet[new_position]
		cipher_text+=new_letter
	print(cipher_text)

encrypt(plain_text=text,shift_amount=shift) #calling the encrypt function