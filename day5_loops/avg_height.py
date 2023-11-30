#sum(list)
#len(list)
height = input("enter a list of student heights ").split()

for n in range(0,len(height)):
    height[n] = int(height[n])

print(height)

count = 0
sum = 0 
for num in height:
    sum += num
    count += 1
avg = sum / count

print(f'{avg} is the average height')