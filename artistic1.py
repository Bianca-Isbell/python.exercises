from turtle import *
t=Turtle()
t.screen.bgcolor('black')
t.color('yellow')
colors = ['yellow']
for x in range(360):
    pencolor(colors[x % 6])
    pensize(15)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    forward(50)
    right(145)
    forward(150)
    right(80)
    forward(120)
    right(135)
    forward(400)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(200)
    left(90)
    forward(100)
    mainloop()