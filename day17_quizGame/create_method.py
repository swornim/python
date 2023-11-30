class User:#PascalCase for class
    def __init__(self,user_id,username):# must provide user id and username
        self.id = user_id 
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers +=1
        self.following +=1 # afnai class
user_1 = User("001","sworim")
user_2 = User("002","shrestha")

print(user_1.id)

user_1.follow(user_2)

print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)