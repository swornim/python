import random
chance = 0
random_num = random.randint(1,100)
print(random_num)

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    chance = 10
else:
    chance = 5

def guess_the_num():
    global chance
    while chance != 0:
       
        print(f"You have {chance} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        if guess == random_num:
            print("correct!")
            chance = 0

        elif guess > random_num:
            print("too high \nguess again\n")
            chance -=1
        else:
            print("too low\nguess again\n")
            chance -=1
        print(f"chance = {chance}")

print(f"initial chance = {chance}")
guess_the_num()

        

