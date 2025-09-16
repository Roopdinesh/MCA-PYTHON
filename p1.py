from turtle import*
speed(-1)  #fastest
side=6
for i in range(side):
    for i in range(side):
        for i in range(side):
            fd(30)
            lt(360/side)
        fd(50)
        lt(360/side)
    fd(100)
    lt(360/side)
    
hideturtle()
mainloop()
    
