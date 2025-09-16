from turtle import*
speed(1)
pencolor('red')
pensize(2)

heart=3

for i in range(heart):
    fd(50)
    lt(360/heart)
    dot(2)
    circle(10,15)
hideturtle()
mainloop()
    
    