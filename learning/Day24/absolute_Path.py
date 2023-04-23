# getting the file in the desktop with absolute path
#absoulte path start with root which is denoted by / at the front that is Drive C in windows
with open("/Users/AYUSH/Desktop/file.txt") as file:
	content=file.read()
	print(content)


with open("../../../file.txt") as file:
	content=file.read()
	print(content)