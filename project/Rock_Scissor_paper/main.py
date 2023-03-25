rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice==0:
  print(rock)
elif user_choice==1:
  print(paper)
else:
  print(scissors)

print("Computer chose:\n")
computer_choice=random.randint(0,2)
if computer_choice==0:
  print(rock)
elif computer_choice==1:
  print(paper)
else:
  print(scissors)

if user_choice==0 and computer_choice==2:
  print("you win")
elif computer_choice==0 and user_choice==2:
  print('you lose')
elif user_choice>computer_choice:
  print("you win")
elif computer_choice>user_choice:
  print('you lose')
elif computer_choice==user_choice:
  print('Its a draw')
else:
  print('you typed an invalid number you lose!')