import turtle
import random

#heads=turtle.left(90)
#tails=turtle.right(90)
#n=random.randrange(heads,tails)

#for i in range(100):

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)

wn=turtle.Screen()

distance=10
angle=90
is_in_screen=True
colors=["red", "blue", "green", "orange"]

while is_in_screen:
    coin= random.randrange(0,2)
    if coin:
        t.right(angle)
    else:
        t.left(angle)
    t.forward(distance)

    turtleX=t.xcor()
    turtleY=t.ycor()

    x_range=wn.window_width()/2
    y_range=wn.window_height()/2

    t.color(random.choice(colors))

    if abs(turtleX)>x_range or abs(turtleY)>y_range:
        is_in_screen=False

