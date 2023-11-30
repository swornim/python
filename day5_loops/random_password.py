import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']

print("welcome to the PyPassword Generator")
nr_letters = int(input("how many letters would you like in you pasword"))
nr_symbols = int(input("how many symbols would you like? "))
nr_numbers = int(input("how may numbers would you like? "))

total_length = nr_letters+nr_numbers+nr_symbols

password = []

for i in range(0,nr_letters):
    password.append(letters[random.randint(0,len(letters)-1)])

for j in range(0,nr_symbols):
    random_int = random.randint(0,len(password))
    random_symbol = symbols[random.randint(0,len(symbols)-1)]
    password.insert(random_int,random_symbol)


for k in range(0,nr_numbers):
    random_int = random.randint(0,len(password))
    random_number = numbers[random.randint(0,len(numbers)-1)]
    password.insert(random_int,random_number)

display_password = ''

for i in range(0,len(password)):
    display_password += password[i]

print(display_password)