from turtle import *
import random


tim = Turtle()

tim.pensize(10)
angle = [0,90,180,360]

for i in range(30):
    tim.forward(15)
    tim.right(random.choice(angle))

exitonclick()