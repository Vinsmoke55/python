import pandas

data=pandas.read_csv("weather-data.csv")

# #whole table is a dataframe, it 2D
# print(data)

# #a single column is a series, it is 1D
# print(data["temp"])


# #conversion of dataframe to dictionary
# data_dict=data.to_dict()
# print(data_dict)

# #coversion of series to a list
# temp_list=data["temp"].to_list()
# print(temp_list)

# #normal way of finding the average 
# sum_of_list=sum(temp_list)
# length=len(temp_list)
# avg=sum_of_list/length
# print(avg)

# #average using pandas methods
# print(data["temp"].mean())

# #getting the maximum value form the column/series
# print(data["temp"].max())

# #these two are same
# print(data["condition"])
# print(data.condition)


# #getting the row from the table
# print(data[data.day=="Monday"])

# #getting the row with the maximum temp
# print(data[data.temp==data.temp.max()])


# #geting the temperature of monday and converting it into farenheit
# monday=data[data.day=="Monday"]
# print(monday.condition)

# monday_temp=int(monday.temp)
# faranheit=monday_temp*9/7+32
# print(faranheit)


#creating our own dataframe from scratch
student_dict={
	"student":["ayush","ram","hari"],
	"score":[90,80,100]
}

#converting to dataframe
student_data=pandas.DataFrame(student_dict)
print(student_data)

# saving as a .csv file in pc
student_data.to_csv("studendata.csv")