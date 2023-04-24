## this method of reading is to hard to follow up
# with open("weather-data.csv") as data_file:
# 	data=file.readlines()
# 	print(data)


## this mehtod requires too much code to be written 
# import csv
# with open("weather-data.csv") as data_file:
# 	data=csv.reader(data_file)
# 	temperature=[]
# 	for row in data:
# 		temperature.append(row[1])

# 	print(temperature)


# so we use pandas to work with the .csv files
import pandas

data=pandas.read_csv("weather-data.csv")

print(data)

