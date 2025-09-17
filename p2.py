from turtle import *
speed(-1)   #fastest
side = 6
for i in range(side):
    for i in range(side-1):
        for i in range(side-1):
            fd(25)
            lt(300/side-1) 
            dot(2)
        fd(50)
        lt(360/side-1)
    fd(100)
    lt(360/side-1)

hideturtle()
mainloop()