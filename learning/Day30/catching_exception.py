# # there is error while try block executes so except block runs
# try:
# 	with open("file.txt") as fs:
# 		fs.read()
# except:
# 	print("file not found")

# there is not the file file.txt so running except ie creating file.txt and writing hello world to it
try:
	file=open("file.txt")
	dict={"key":"hello"}
	print(dict["asd"])
except FileNotFoundError:	#if FileNotFoundError occurs then only except block will run
	file=open("file.txt","w")
	file.write("hello world")
# except KeyError:	#we can have more than one except for the type of error
# 	print("key not found")
except KeyError as error:	#we can also provide with the erorr in the code
	print(f"the key {error} was not found")
else:	#this line only runs if there was not any error in try 
	print("there was no error during try")
finally:	#this block will always run although there is error or not
	print("this code runs")