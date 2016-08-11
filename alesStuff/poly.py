from turtle import *
shape=3
def poly(time, length, height, color):
    if time==3:
        goto(0,0)
        pendown()
        for i in range(3):
            pencolor(color)
            forward(length)
            right(-120)
        goto(0,y+2)
    elif time==4:
        goto(0,0)
        pendown()
        for i in range(4):
            pencolor(color)
            forward(length)
            right(90)
        e=0
        if e<16:
            goto(0,e)
            e+=2
            
        
    elif time==5:
        for i in range(5):
            pencolor(color)
            forward(length)
            right(-108)
    elif time==6:
        for i in range(6):
            pencolor(color)
            forward(length)
            right(-100)
    elif time==7:
        for i in range(7):
            pencolor(color)
            forward(length)
            right(-128)

poly(4, 50, 40, "green")
poly(4, 50, 40, "green")
poly(4, 50, "green")
poly(4, 50, "green")
poly(4, 50, "green")
poly(4, 50, "green")
poly(4, 50, "green")
