import random
scissor ='''
    -------
---'    ___)____  
         _______) 
       __________)
       (____)
---.___(___)       

'''
rock='''
    -------
---'    ____)
       (_____) 
       (____)
---.___(___)       

'''
paper='''
    --------
---'    ____)___  
         _______) 
       __________)
         _______)
---.__________)       

'''
user = int(input("pick 1.rock or 2.paper or 3.scissor"))
if user >3 or user < 1:
    print("invalid choice")
else:
    game = [rock,paper,scissor]

    random_int = random.randint(0,2)

    pick = game[user-1]
    cpu = game[random_int]

    print(f'your - {game[user-1]}')

    print(f'computer- {game[random_int]}')



    if (pick == cpu):
        print("it's a draw")
    elif (pick == game[1] and cpu == game[0])or (pick == game[2] and cpu == game[1]) or (pick == game[0] and cpu == game[2]):
        print("you win!!")
    else:
        print("you lose")
