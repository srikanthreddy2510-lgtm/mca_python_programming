from turtle import *
speed('fast')
pencolor("blue")
pensize(3)

side = 6
for i in range(20):
    for i in range(side):
        fd(20)
        lt(360/side)
    fd(10)
    lt(360/side)

hideturtle()
mainloop()