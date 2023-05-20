import datetime as dt
import smtplib
import random

EMAIL="neupaneayush3@gmail.com"
APPPASSWORD="qqyitcsxljkhkrwj"

now=dt.datetime.now()
day_of_week=now.weekday()

print(day_of_week)

if day_of_week==5:
	with open("quotes.txt") as f:
		quote_list=f.readlines()

	quote_to_send=random.choice(quote_list)

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=EMAIL,password=APPPASSWORD)
		connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject:quote\n\n{quote_to_send}")




