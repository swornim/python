print("welcome to Python pizza deliveries!")
size = input("what size pizza do you want? S,M, or L")
add_pepperoni = input("do you want pepperoni? Y or N")
extra_cheese = input("do you want extra cheese?")

bill = 0

if size == 's':
    bill += 15
    if add_pepperoni == 'y':
        bill += 2
elif size == 'm':
    bill += 20
    if add_pepperoni == 'y':
        bill += 3
elif size == 'l':
    bill += 25
    if add_pepperoni == 'y':
        bill += 3
if extra_cheese == 'y':
    bill +=1

print(f"{bill} is you final bill")