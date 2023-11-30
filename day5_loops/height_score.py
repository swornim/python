score = input("enter a list of score").split()
for n in range(0,len(score)):
    score[n] = int(score[n])
highscore = 0
n = 0
for m in score:
   
    if m > highscore:
        highscore = m

print(highscore)
