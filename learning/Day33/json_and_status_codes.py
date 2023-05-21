# requests module is used to work with api
import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")	#we have to provide api endpoint for it to work

print(response)	# this line gives the object 

print(response.raise_for_status())	# this line raise the exception for the status code other than 200

data=response.json()	#this line conver the data into json format

print(data)

# working with json data
longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]

lat_long=(latitude,longitude)

print(lat_long)