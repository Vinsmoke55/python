# sending an email using smtplib
import smtplib

EMAIL="neupaneayush3@gmail.com"
APPPASSWORD="qqyitcsxljkhkrwj"

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=EMAIL,password=APPPASSWORD)
	connection.sendmail(from_addr=EMAIL,
		to_addrs="neupane_ayush@yahoo.com",
		msg="Subject:hello\n\nhello world"
		)
