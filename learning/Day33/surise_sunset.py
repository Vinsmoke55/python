import requests
import datetime as dt

latitude=27.7172
longitude=85.3240

today=dt.datetime.now()


parameter={
	"lat":latitude,
	"lng":longitude,
	"formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)

data=response.json()


sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(today.hour)