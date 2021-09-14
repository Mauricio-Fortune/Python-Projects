# Mauricio Fortune Panizo
# COP 2930
# Python turtle with random number
# 09/10/12

import turtle
import random


#what do they want to draw
shape = (input("Do you want a rectangle, triangle, or both?\n"))

turtle.pencolor("violet")
turtle.fillcolor("blue")
#Rectangle
if shape == "rectangle" or shape == "Rectangle" or shape == "RECTANGLE":
    #sides of rectangle and turtle alignment
    Sside= random.randint(100, 220)
    Lside= random.randint(320, 520)
    turtle.penup()
    turtle.left(180)
    turtle.forward(Lside/2)
    #rectangle being drawn
    turtle.begin_fill()
    turtle.pendown()
    turtle.right (90)
    turtle.forward(Sside)
    turtle.right (90)
    turtle.forward(Lside)
    turtle.right(90)
    turtle.forward(Sside)
    turtle.right (90)
    turtle.forward(Lside)
    turtle.end_fill()
#Triangle
elif shape == "triangle" or shape == "Triangle" or shape == "TRIANGLE":
    length = random.randint (100, 500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(150)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.end_fill()
#Both
else:
    #Sides of rectangle
    Sside= random.randint(60, 170)
    Lside= random.randint(200, 310)
    #Sides of triangle
    length = random.randint (100, 400)
    turtle.penup()
    turtle.left(180)
    turtle.forward(Lside + 10)
    turtle.pendown()
    #rectangle
    turtle.right (90)
    turtle.forward(Sside)
    turtle.right (90)
    turtle.forward(Lside)
    turtle.right(90)
    turtle.forward(Sside)
    turtle.right (90)
    turtle.forward(Lside)
    turtle.penup()
    turtle.right(180)
    turtle.forward(Lside+20)
    turtle.pendown()
    #triangle
    turtle.left(60)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
