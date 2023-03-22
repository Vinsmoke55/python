#Tip calculator

print("Welcome to the tip Calculator.")
total=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_amount=1+tip/100
bill=(total/people)*tip_amount
round_bill=round(bill,2)
print(f"Each person should pay: ${round_bill}")
