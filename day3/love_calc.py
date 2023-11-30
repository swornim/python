name1 = input("enter your name ")
name2 = input("enter their name ")

name = (name1 + name2).lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

total1 = t+r+u+e
total2 = l+o+v+e
print(total1)
print(total2)
total = str(total1) + str(total2)
total = int(total)

if total <10 or total > 90:
    print(f"your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"your score is {total}, you ar ealright together")
else:
    print(f"your score is {total}")