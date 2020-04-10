import turtle
import random

t=turtle.Turtle()
t.speed(-1)
t.width(5)
t.color('red')

for x in range(500):
    t.circle(50)
    t.left(45)


for x in range(100):
    t.penup()
    t.setpos(100,-150)
    t.pendown()
    t.circle(30)
    t.left(60)

turtle.mainloop()
