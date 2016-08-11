distance=10
angle=90

from turtle import *
goto(0,0)
pendown()
for i in range(4):
    forward(50)
    right(90)
penup()

goto(60,60)
pendown()
for i in range(3):
    forward(40)
    right(-120)
penup()

goto(110,110)
pendown()
def square(length):
    for i in range(4):
        forward(length)
        right(90)
    penup()
    goto(110,150)
    pendown()
    for i in range(3):
        forward(length)
        right(-120)

square(50)
penup()
goto(-100,0)
pendown()
def squares(length, color):
    for i in range(4):
        pencolor(color)
        forward(length)
        right(90)
    penup()
    back(50)
    pendown()
def tri(length, color):
    for i in range(3):
        pencolor(color)
        forward(length)
        right(-120)
    penup()
    back(50)
    pendown()
squares(20,"blue")
squares(20,"green")
squares(20,"pink")

tri(20,"blue")
tri(20,"green")
tri(20,"pink")

def poly(length, color):
    for i in range(6):
        pencolor(color)
        forward(length)
        right(-100)
poly(20, "purple")
    




    


