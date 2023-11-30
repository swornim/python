import random
import os

os.system('clear')
play = 'y'
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
blackJack = 21

user_card1 = 0
user_card2 = 0

computer_card1 = 0
computer_card2 = 0

user_deck = []
computer_deck = []

def check_ace(user_card):
    if user_card == cards[0]:
        choice = int(input("do you want your ace to be 1 or 11?"))
        if choice == 1:
            return choice
        elif choice == 11:
            return choice
    else:
        return user_card
    
def generate_first_cards():
    global user_deck 
    global computer_deck

    user_deck = []
    computer_deck = []

    user_card1 = random.choice(cards)
    
    user_deck.append(check_ace(user_card1))

    user_card2 = random.choice(cards)
    user_deck.append(check_ace(user_card2))

    computer_card1 = random.choice(cards)
    computer_deck.append(computer_card1)

    computer_card2 = random.choice(cards)
    computer_deck.append(computer_card2)

    print(f"computer card = {computer_deck}")
    print(f"your card = {user_deck}")

def generate_random_card():
    random_card = random.choice(cards)
    return random_card

def in_user_hand():
    global user_total
    user_total = 0
    for card in user_deck:
        user_total = user_total + card #treats it as local variable hence we need to set it to global
    print(f"user total = {user_total}")
    return user_total

def in_computer_hand():
    global computer_total
    computer_total = 0
    for cards in computer_deck:
        computer_total += cards
    print(f"computer total = {computer_total}")
    return computer_total

def you_loose_or_win(in_user_hand_total,condition):
    print(f"your socre ={in_user_hand_total} you {condition}!!")
    play_again = print("do you want to play again?Y or N")
    if play_again == 'n':
       do_you_want_to_play = 'n'




def game():
    hit = 'y'
    while hit == 'y':
        global in_user_hand_total
        global in_computer_hand_total

        in_user_hand_total = in_user_hand()
        in_computer_hand_total = in_computer_hand()

        if in_computer_hand_total < 17:
            computer_deck.append(generate_random_card())
            in_computer_hand()
            print(f"computer deck = {computer_deck}")

        if in_user_hand_total  == 21:
            return 'win'

        elif in_user_hand_total > 21:
            return 'lost'
            
        else:

            global computer_total
            global user_total
            hit_or_stop = input("do you want to hit or stop?")

            if hit_or_stop == 'stop':

                if in_computer_hand() > 21:
                    return 'win'

                computer_total -= blackJack
                user_total -= blackJack
                if user_total > computer_total:

                    return 'win'

                elif computer_total > user_total:
                    return 'lost'
                
                else:
                    return 'drawn'
            elif hit_or_stop == 'hit':
                user_deck.append(generate_random_card())
                print(user_deck)


                

"""actual game starts from here"""

do_you_want_to_play = input("do you want to play? y or n")

while do_you_want_to_play == 'y':

    generate_first_cards()

    user_total = 0
    computer_total = 0 

    print(f"you have {game()}!!")

    continue_game = input("do you want to play again? y or n ")
    if continue_game == 'n':
        do_you_want_to_play = 'n'

print("thank you for playing!")