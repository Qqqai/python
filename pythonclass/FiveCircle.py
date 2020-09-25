#FiveCircle
import turtle

turtle.setup(650,350,200,200)
turtle.pensize(10)

turtle.pu()
turtle.goto(-100,50)
turtle.pd()
turtle.pencolor("blue")
turtle.circle(50,360)

turtle.pu()
turtle.goto(0,50)
turtle.pd()
turtle.pencolor("black")
turtle.circle(50,360)

turtle.pu()
turtle.goto(100,50)
turtle.pd()
turtle.pencolor("green")
turtle.circle(50,360)

turtle.pu()
turtle.goto(-50,0)
turtle.pd()
turtle.pencolor("yellow")
turtle.circle(50,360)

turtle.pu()
turtle.goto(50,0)
turtle.pd()
turtle.pencolor("red")
turtle.circle(50,360)

turtle.done()
