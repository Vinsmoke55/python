#dictionary
student={
	"name":"Ayush Neupane",		#we have to assign two part in he dictionary key and the value
	"address":"kathmandu",
}

# retriving items from the dictionary
print(student["name"])

# adding item to the dictionary
student["roll"]=14
print(student)

# # creating an empty dictionary
# student={}

# # wiping out the entire dictionary
# student={}
# print(student)

# editing the item in the dictionary
student["name"]="Ram Khatri"
print(student)

# looping through the dictionary
for key in student:
	print(key)		#this only prints the key value in the dictionary
	print(student[key])