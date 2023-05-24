import os
import requests
from twilio.rest import Client

API_ENPOINT="https://api.openweathermap.org/data/2.5/onecall?lat=27.717245"
API_KEY=os.environ.get('API')	#working with the environment variable
PARAMETER={
	"lat":27.717245,
	"lon":85.323959,
	"appid":API_KEY,
	"exclude":"daily,minutely,current"
}

response=requests.get(url=API_ENPOINT,params=PARAMETER)

weather_data=response.json()

carry_umbrella=False

weather=weather_data["hourly"][:12]
for hour_data in weather:
	data=hour_data["weather"][0]["id"]
	if data<700:
		carry_umbrella=True

if carry_umbrella:
	print("please carry your umbrealla")
	account_sid = "AC128774b39c6633ab4b8ce97dc966f809"
	auth_token ="f1579e2770ecdc77f50d180105035b6a"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	  body="Its going to rain please carry your umbrella",
	  from_="+13156673970",
	  to=os.environ.get('MY_PHONE_NO')
	)
	# print(message.status)
