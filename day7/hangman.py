import random
stages = ['''
    +---+          
    |   |
    0   |
   /|\  |      
   / \  |
        |
  =========  
''','''
    +---+          
    |   |
    0   |
   /|\  |      
   /    |
        |
  =========  
''','''
    +---+          
    |   |
    0   |
   /|\  |      
        |
        |
  =========  
''','''
    +---+          
    |   |
    0   |
   /|   |      
        |
        |
  =========  
''','''
    +---+          
    |   |
    0   |
    |   |      
        |
        |
  =========  
''','''
    +---+          
    |   |
    0   |
        |      
        |
        |
  =========  
''','''
    +---+          
    |   |
        |
        |      
        |
        |
  =========  
'''          
]




word_list = ['ardvark', 'baboon','camel']
win = 0
lives = 6
loop = 0
display = ''

chosen_word = word_list[random.randint(0,len(word_list)-1)]



word_length = len(chosen_word)
#put "_" instead of word
guessed_word = []
for i in range(len(chosen_word)):
    guessed_word.append('_')
#testing code
print(chosen_word)

while not win :
    guess = input("enter a single letter").lower()
    print(stages[lives])
    #check condition for right or wrong
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guessed_word[i] = guess

    if guess not in chosen_word:
        lives -=1
        if lives ==0:
            win = 1  
            print("you loose")
            


    print(guessed_word)
    if '_' not in guessed_word:
        win = 1
        print("you win!")
    elif lives == 0:
        print("you lose!")
