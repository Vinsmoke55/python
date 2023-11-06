from bs4 import BeautifulSoup
#import lxml

with open("website.html",encoding="utf8") as file:
	content=file.read()

soup=BeautifulSoup(content,"html.parser")

# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

all_anchor_tag=soup.find_all(name="a")
print(all_anchor_tag)

for tag in all_anchor_tag:
	# print(tag.getText())
	# print(tag.get("href"))
	pass

header=soup.find(name="h1",id="name")
print(header)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.getText())

company_url=soup.select_one(selector="p a")
print(company_url)

headings=soup.select("#name")
print(headings)