import os
from asci_art import art
os.system('clear')


list_of_bidder = []



def add_new_bidder():
    bidder = {}
    name = input("what is your name?: ")
    bid = int(input("what is your bid? "))
    bidder["name"] = name
    bidder['bid'] = bid
    list_of_bidder.append(bidder)

def max_bid():
    max = 0
    name_of_bidder = ''
    for dict in list_of_bidder:
        if dict['bid'] > max:
            max = dict['bid']
            name_of_bidder = dict['name']
    print(f"The winner is {name_of_bidder} with a bid of $ {max} ")
there_is_next_bidder = 'yes'

while there_is_next_bidder == 'yes':
    add_new_bidder()
    next_bidder = input("is there next bidder?yes or no ")
    os.system('clear')
    if next_bidder == 'no':
        there_is_next_bidder = 'no'
        print(list_of_bidder)
        max_bid()