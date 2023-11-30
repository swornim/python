from turtle import *

for i in range (15):
    if i % 2 == 0:
        pendown()
    else:
        penup()
    forward(10)

exitonclick()