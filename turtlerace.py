import turtle
import random
from turtle import Screen


#window setup

screen=Screen()
t=turtle.Turtle()
t.getscreen()
t.speed(1)
t.color('white')
turtle.bgcolor("green")
turtle.title("TURTLE RACE")
t.penup()
t.hideturtle()

#finishline

#turtles
t1=turtle.Turtle()
t1.color('pink')
t1.shape('turtle')
t1.speed(1)
t1.penup()
t1.goto(-250,100)
t1.pendown()

t2=turtle.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.speed(1)
t2.penup()
t2.goto(-250,50)
t2.pendown()

t3=turtle.Turtle()
t3.color('purple')
t3.shape('turtle')
t3.speed(1)
t3.penup()
t3.goto(-250,0)
t3.pendown()
#Turtlemove

for i in range(200):
    t1.forward(random.randint(1,5))
    t2.forward(random.randint(1,5))
    t3.forward(random.randint(1,5))

turtle.exitonclick()

turtle.mainloop()
