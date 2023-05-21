# requests module is used to work with api
import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")	#we have to provide api endpoint for it to work

print(response)