# #classic way of opening the file and reading from it
# file=open("readfile.txt")
# content=file.read()
# print(content)
# file.close()


# #second way of open a file and reading from it
# with open("readfile.txt") as file:
# 	content=file.read()
# 	print(content)


# #writing to a file
# with open("writefile.txt",mode="w") as file:		#we have to define the mode to write in a file which is set read "r" to default
# 	file.write("hello user")
	

#writing to a file without deleting the previous content(append)
with open("readfile.txt",mode="a") as file:
	file.write("\n and i am from bafal")
