import random
import turtle
from turtle import *

my_turtle=turtle.Turtle()
colors=['red','green','blue','yellow','purple']
my_turtle.width(5)


def up():
    my_turtle.setheading(90)
    my_turtle.forward(100)


def down():
    my_turtle.color(random.choice(colors))
    my_turtle.setheading(270)
    my_turtle.forward(100)


def left():
    my_turtle.setheading(180)
    my_turtle.forward(100)


def right():
    my_turtle.setheading(0)
    my_turtle.forward(100)


def clickleft(x,y):
    my_turtle.color(random.choice(colors))


def clickright(x,y):
    my_turtle.stamp()


turtle.listen()

turtle.onclick(clickleft,1)
turtle.onclick(clickright,3)

turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')

turtle.mainloop()
