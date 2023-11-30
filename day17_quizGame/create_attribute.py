class User:#PascalCase for class
    def __init__(self,user_id,username):# must provide user id and username
        self.id = user_id 
        self.username = username
user_1 = User("001","sworim")
user_2 = User("002","shrestha")

print(user_1.id)