from game_data import data
from asci_art import logo,vs
import os

import random

data
score = 0
a ={}
b = {}
lost = False

def generate_A():
    global a,b
    a = random.choice(data)
    data.remove(a)

def generate_B():
    global a,b
    b = random.choice(data)
    data.remove(b)

def compare_follower(guess):

    global a,b

    if a['follower_count'] > b['follower_count']:
        a = b
        return guess == 'a'
   
    else:
        return guess == 'b'

print(logo)
generate_A()
generate_B()
while data != ['\0'] or lost == False:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    guess = input("Who has more followers? 'A' or 'B'?").lower()
    if compare_follower(guess) == 'False':
        print("you loose")
        lost = True
        data = ['\0']
    else:
        score += 1
        print(f"you are right! Current score: {score}")
        generate_B()
    