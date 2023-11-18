from bs4 import BeautifulSoup
import requests



year=input("what year you would like to travel in YYYY-MM-DD format:\n")

print(year)

response=requests.get(f"https://www.billboard.com/charts/hot-100/{year}")

top_hundred=response.text

soup=BeautifulSoup(top_hundred,"html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)