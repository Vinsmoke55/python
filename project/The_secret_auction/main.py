from art import logo
import os

print(logo)
print("Welcome to the secret auction program")

condition=True
bid_list=[]
while condition:
	bid_dictionary={}
	name=input("What is your name? ")
	bid=int(input("What's your bid? $"))
	other_bidder=input("Are there any other bidders? Type 'yes' or 'no'. ")
	bid_dictionary["name"]=name
	bid_dictionary["bid"]=bid
	bid_list.append(bid_dictionary)
	if other_bidder=="no":
		condition=False
	else:
		os.system('clear') #clearing the input screen after one person have entered their bid(privacy)

highest_bid={"name":" ","bid":0}
for each_bid in bid_list:
	if each_bid["bid"]>highest_bid["bid"]:
		highest_bid["name"]=each_bid["name"]
		highest_bid["bid"]=each_bid["bid"]

print(f'{highest_bid["name"]} had the highest bid of ${highest_bid["bid"]} and have won the auction.')