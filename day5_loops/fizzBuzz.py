for i in range(0,51):
    if i % 15 == 0:
        i = 'fizzbuzz'
    elif i % 3 == 0:
        i = 'fizz'
    elif i %5 == 0:
        i = 'buzz'
    print(i)