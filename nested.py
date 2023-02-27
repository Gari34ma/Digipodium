from turtle import*
speed('fastest')
pencolor('#8989ff')
fillcolor('blue')
pensize(5)
side = 6
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(50)
        for i in range(side):
            bk(25)
            rt(360/side)
            dot(20)
        lt(360/side)
    rt(360/side)
    end_fill()
    lt(360/side)

hideturtle()
mainloop()