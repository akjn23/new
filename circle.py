import turtle as t
from itertools import cycle

t.bgcolor('black')
t.pensize(4)
colours=cycle(['red','yellow','blue','brown','pink','orange','purple','green'])





t.penup()
t.goto(90,-200)
t.pendown()
t.pencolor('red')
for r in range(0,100,2):
    t.pencolor(next(colours))
    t.circle(r)
    t.left(90)
    t.forward(r+2)
    t.right(90)
    t.forward(2)
    
