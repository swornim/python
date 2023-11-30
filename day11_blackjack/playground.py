chance = 1 

def func():
    print("chance \n again")
    if chance == 10:
        return 'ok'
    else:
        print("not ok")

g = func()

print(g)