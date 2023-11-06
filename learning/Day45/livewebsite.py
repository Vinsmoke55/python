from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")

text=[]
first_heading=soup.select(".titleline a")

for tag in first_heading:
	article_text=tag.getText()
	text.append(article_text)
	article_link=tag.find("href")

article_upvote=[score.getText() for score in soup.find_all(name="span",class_="score")]

print(text)
# print(article_link)
# print(article_upvote)

# # print(first_heading)