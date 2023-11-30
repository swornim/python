import random

names_string = input("enter everybodys name seperated by a comma")
names = names_string.split(", ") 

# length = len(names)

print(f"{random.choice(names)} pays the bill")
