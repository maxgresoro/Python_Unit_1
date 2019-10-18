#  Max Gresoro - IT075 Sierra College
#  Assingment to create a picture in Turtle Graphics

import turtle

myturtle = turtle.Turtle()

myturtle.speed(0)

myturtle.pencolor("black")
myturtle.penup()
myturtle.setposition(0, 0)
myturtle.setheading(0)
myturtle.pendown()
for i in range(1,300):
    myturtle.forward(i*5)
    myturtle.right(120)
    myturtle.forward(i*5)
    myturtle.right(120)
    myturtle.right(2)

myturtle.pencolor("white")
myturtle.penup()
myturtle.setposition(0, 0)
myturtle.setheading(0)
myturtle.pendown()
for i in range(1,300):
    myturtle.forward(i*5)
    myturtle.right(120)
    myturtle.forward(i*5)
    myturtle.right(120)
    myturtle.right(2)

turtle.done()
