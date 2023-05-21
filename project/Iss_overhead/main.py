import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 27.7172
MY_LONG =  85.3240
EMAIL="neupaneayush3@gmail.com"
APPPASSWORD="qqyitcsxljkhkrwj"

def iss_overhead():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])

	# #Your position is within +5 or -5 degrees of the ISS position.
	if 22>=iss_latitude<=32 and 80>=iss_longitude<=90:
		return True

def is_night():
	parameters = {
	    "lat": MY_LAT,
	    "lng": MY_LONG,
	    "formatted": 0,
	}

	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

	time_now = datetime.now()

	if time_now.hour<sunrise or time_now.hour>sunset:
		return True
while True:
	time.sleep(60)
	if is_night() and iss_overhead():
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user=EMAIL,password=APPPASSWORD)
			connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg="Subject:iss overhead\n\nLook up in the sky")


