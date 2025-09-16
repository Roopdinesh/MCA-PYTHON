from turtle import*
speed('slowest')
pencolor('red')
pensize(3)



side=6
for i in range(side):
    fd(200)
    lt(360/side)
    
    
hideturtle()
mainloop()