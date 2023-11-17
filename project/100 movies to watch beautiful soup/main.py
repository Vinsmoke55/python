import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)

site=response.text

soup=BeautifulSoup(site,"html.parser")

title=soup.find_all(name="h3",class_="title")

movies=[movie.getText() for movie in title]

# # getting only the text from each tag and appending in movies list
# for tag in title:
# 	name=tag.getText()
# 	movies.append(name)

# making the list to be in ascending order
movies.reverse()

print(movies)

# #writing the list in .txt file
# with open("Top100movies.txt","w",encoding="utf8") as file:	
# 	for movie in movies:
# 		file.write(f"{movie}\n")