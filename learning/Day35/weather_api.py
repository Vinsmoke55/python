import requests

API_ENPOINT="https://api.openweathermap.org/data/2.5/onecall?lat=27.717245"
API_KEY="28a10b750cb699fcccf93c656372db0c"
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
	print("Carry your umbrella")




