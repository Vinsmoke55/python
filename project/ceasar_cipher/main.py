# from art import logo
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(logo) #to print the logo

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # #encrypting the message by moving the index to index+shift_amount
# # #and to prevent index out of range error adding alphabet two times in the list
# # def encrypt(plain_text,shift_amount):
# # 	cipher_text=""
# # 	for letter in plain_text:
# # 		position=alphabet.index(letter)
# # 		new_position=position+shift_amount
# # 		new_letter=alphabet[new_position]
# # 		cipher_text+=new_letter
# # 	print(f"The encoded message is {cipher_text}")

# # #decrypting the message by moving the index to index-shift_amount
# # def decrypt(cipher_text,shift_amount):
# # 	plain_text=""
# # 	for letter in plain_text:
# # 		position=alphabet.index(letter)
# # 		new_position=position-shift_amount
# # 		new_letter=alphabet[new_position]
# # 		plain_text+=new_letter
# # 	print(f"The decoded message is {plain_text}")



# # if direction=='encode':
# # 	encrypt(plain_text=text,shift_amount=shift) #calling the encrypt function
# # elif direction=='decode':
# # 	decrypt(cipher_text=text,shift_amount=shift)	#calling the decrypt function


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:	#if other character other than the alphabet are passed than leave tham as they are
      end_text += char
  print(f"The {cipher_direction}d result: {end_text}")

# Importing and printing the logo from art.py when the program starts.
from art import logo
print(logo)

should_end = False
while not should_end:	#to continue the program 

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 
  shift = shift % 26	#if the shift is a very large number than to bring it under 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("type yes if you want to continue otherwise type no.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

