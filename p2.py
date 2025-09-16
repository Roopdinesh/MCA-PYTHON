from turtle import*
speed('fast')
pencolor('red')
pensize(3)



side=6
for i in range(side):
    for i in range(side):
        fd(50)
        lt(360/side)
    fd(100)
    lt(360/side)
    
    
hideturtle()
mainloop()