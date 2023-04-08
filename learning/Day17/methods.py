class User:
	def __init__(self,user_id,username):
		self.id=user_id
		self.username=username
		self.follower=0
		self.following=0

	def follow(self,user):
		user.follower+=1
		self.following+=1

user_1=User("1","ayush")
user_2=User("2","ank")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)