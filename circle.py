import turtle as t
from itertools import cycle

t.bgcolor('black')
t.pensize(4)
colours=cycle(['red','yellow','blue','brown','pink','orange','purple','green','black'])





t.penup()
t.goto(90,-200)
t.pendown()
t.pencolor('red')
for r in range(10,100,2):
    t.pencolor(next(colours))
    t.circle(r)
    t.left(90)
    t.forward(r+4)
    t.right(90)
    t.forward(3)
    
