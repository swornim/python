
def prime_checker(number):
    not_prime = 0
    if number == 2:
        print("prime")
    else:
        for i in range(2,number-1):
            if number % i == 0:
                not_prime = 1
        if not_prime:
            print("not prime")
        else:
            print("prime")





n = int(input(" check this number:"))
prime_checker(number = n)