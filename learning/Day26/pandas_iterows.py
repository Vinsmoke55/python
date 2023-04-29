# python dictionary
student_score={
	"name":["ayush","ram","hari"],
	"score":[80,90,70]
}

# # looping through python dictionary
# for (key,value) in student_score.items():
# 	print(key)
# 	print(value)

# creating a python dataframe
import pandas

student_score_data_frame=pandas.DataFrame(student_score)

# python dataframe can be iterated in the same way as dictonary but pandas also have a built in function for iteration
for (index,rows) in student_score_data_frame.iterrows():
	print(rows["name"])
