with open("file1.txt") as file:
	data1=file.readlines()


with open("file2.txt") as file:
	data2=file.readlines()
	

result=[int(n) for n in data1 if n in data2]

# Write your code above 👆

print(result)
