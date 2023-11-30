print("welcome to roller coster")
height = int(input('enter your height'))
age = int(input("enter your age") )

if height >= 120:
    if age < 12: 
        print("pay 5 dollars")
    elif age >= 12 and age <18:
        print("pay 7 dollars")
    else:
        print("pay 12 dollars")
else:
    print("you cannot go to roller coster")
     