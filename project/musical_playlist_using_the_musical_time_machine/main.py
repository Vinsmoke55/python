from bs4 import BeautifulSoup
import requests



date=input("what year you would like to travel in YYYY-MM-DD format:\n")


response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

top_hundred=response.text

soup=BeautifulSoup(top_hundred,"html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)


Client_id='d9b713525fc346dd9e73edae5dbe7f97'
Client_secret='7e345baa86ff448394f6c39ca46bc820'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_id,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")