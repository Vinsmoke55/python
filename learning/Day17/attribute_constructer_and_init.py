# # step:1- creating a attribute
# class User:
# 	pass

# user_1=User()

# #creating an attribute
# user_1.id="1"
# user_1.name="ayush"
# print(user_1.name)


# # step:2-creating a constructer
# class User:
# 	def __init__(self,user_id,username):
# 		self.id=user_id
# 		self.username=username

# user_1=User("1","ayush")	#we have to give the value for id and user name while creating a object
# print(user_1.username)


# step:3-creating a constructer where value should no be initialized while creating object
class User:
	def __init__(self,user_id,username):
		self.id=user_id
		self.username=username
		self.follower=0

user_1=User("1","ayush")




