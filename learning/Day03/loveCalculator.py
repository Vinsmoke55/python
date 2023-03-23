# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string=name1+name2
lowercase_string=combined_string.lower()

t=lowercase_string.count("t")
r=lowercase_string.count("r")
u=lowercase_string.count("u")
e=lowercase_string.count("e")

first_digit=t+r+u+e

l=lowercase_string.count("l")
o=lowercase_string.count("o")
v=lowercase_string.count("v")
e=lowercase_string.count("e")

second_digit=l+o+v+e

combined_digit=str(first_digit)+str(second_digit)

score=int(combined_digit)

if score<10 or score>90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")