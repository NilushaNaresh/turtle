import turtle
from turtle import Screen

t=turtle.Turtle()
screen=Screen()
t.speed(0)
t.shape()


def drag(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(drag)


def clickright(x,y):
    t.clear()


def main():
    turtle.listen()
    t.ondrag(drag)
    turtle.onkey(clickright,'space')
    screen.mainloop()


main()