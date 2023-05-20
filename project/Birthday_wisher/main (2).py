import pandas
import smtplib
import datetime as dt
import random

EMAIL="neupaneayush3@gmail.com"
APPPASSWORD="qqyitcsxljkhkrwj"

todays_date=dt.datetime.now()
today=(todays_date.month,todays_date.day)


data=pandas.read_csv("birthdays.csv")


new_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in new_dict:
	birthday_person=new_dict[today]
	random_number=random.randint(1,3)

	with open(f"./letter_templates/letter_{random_number}.txt") as f:
		letter=f.read()
		new_letter=letter.replace("[NAME]",birthday_person["name"])

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(EMAIL,APPPASSWORD)
		connection.sendmail(from_addr=EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Birthday wish \n\n{new_letter}")
		


