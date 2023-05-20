import datetime as dt

now=dt.datetime.now()	#to get the date and time of now
print(now)

year=now.year	#to get the year
print(year)

day=now.day 	#to get the day of the month
print(day)

day_of_week=now.weekday()	#to get which day it is
print(day_of_week)


# to specify our own datetime
my_birth_date=dt.datetime(year=2002,month=7,day=18)
print(my_birth_date)
