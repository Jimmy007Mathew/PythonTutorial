import turtle
import math
t=turtle.Turtle()
t.up()

def star(length):
    x=math.sin(math.radians(18))*length
    y=x/math.cos(math.radians(54))

    t.left(126)
    t.forward(y)
    t.left(54)
    t.forward(length)
    t.right(180)

    t.down()
    for i in range(5):
        t.forward(length)
        t.left(72)
        t.forward(length)
        t.right(144)
        
    t.up()
    t.forward(length)
    t.right(54)
    t.forward(y)
    t.left(54)
    
sides=int(input("Enter the number of stars"))
size=int(input("Enter the size of star"))
color=input("Enter the color")
angle=360/sides

t.pencolor(color)
t.left(angle)
for i in range(sides):

    t.forward(200)
    t.right(angle)
    star(size)
    t.goto(0,0)

    
 

