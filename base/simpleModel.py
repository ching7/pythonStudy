import turtle
t = turtle.Pen()
for i in range(0,4):
    t.forward(100)
    t.left(90)
t.reset
i=0
while True:
    t.forward(100)
    t.left(90)
    i=i+1
    if i>3:
        break