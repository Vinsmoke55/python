import requests

API_ENPOINT="https://api.openweathermap.org/data/2.5/onecall?lat=27.717245"
API_KEY="28a10b750cb699fcccf93c656372db0c"
PARAMETER={
	"lat":27.717245,
	"lon":85.323959,
	"appid":API_KEY
}

response=requests.get(url=API_ENPOINT,params=PARAMETER)

data=response.json()
print(data)