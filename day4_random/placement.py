row1 = ['1','2','3']
row2 = ['4','5','6']
row3 = ['9','8','7']
#print(f'{row1}\n{row2}\n{row3}')

matrix = [row1 ,row2,row3]

postion = int(input("where do you want to put the treasure"))

rem = postion%10
# print(rem)
postion = int(postion/10)
# print(postion)

if postion == 1:
    row1[rem-1] = 'X'
elif postion == 2:
    row2[rem-1] = 'X'
elif postion == 3:
    row3[rem-1] = 'X' 
else:
    print("out of index")

print(f'{row1}\n{row2}\n{row3}')

