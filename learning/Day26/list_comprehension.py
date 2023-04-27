number=[1,2,3,4]

# new_list=[]

# for n in number:
# 	n+=1
# 	new_list.append(n)

# print(new_list)


# above code using list comprehension
new_list=[n+1 for n in number]
print(new_list)


#list comprehension can also be done for strings
name="Ayush"
letter_list=[letter for letter in name]
print(letter_list)

# list comprehension using range()
double=[number*2 for number in range(1,5)]
print(double)

# conditional list comprehension
names=["ram","harish","sita","rockey"]
short_names=[name for name in names if len(name)<5]
long_names=[name.upper() for name in names if len(name)>5]
print(short_names)
print(long_names)