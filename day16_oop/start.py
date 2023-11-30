from turtle import Turtle,Screen
x = 0
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")
for i in range(0,100):
    timmy.forward(x)
    x =+ 1

my_screen =  Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


