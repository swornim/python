from turtle import *
import random

theta = 0
angle = 0

tim = Turtle()



for i in range (3,11):
    random_color1 = random.random()
    random_color2 = random.random()
    random_color3 = random.random()
    tim.pencolor((random_color1,random_color2,random_color3))
    theta = 0
    angle = 360/i
    while theta < 360:
        tim.forward(90)
        tim.right(angle)
        theta += angle

screeTime = Screen()
screeTime.exitonclick()