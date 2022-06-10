import turtle
def rectangle(color):
     t.begin_fill()
     t.fillcolor(color)
     for i in range(2):
          t.fd(300)
          t.rt(90)
          t.fd(100)
          t.rt(90)
     t.end_fill()     
     
t=turtle.Turtle()
t.up()
t.pensize(2)
t.goto(0,-300)
t.down()
t.goto(0,300)
rectangle("orange")

t.goto(0,200)
t.forward(150)
t.color("blue")
t.circle(-50)
t.setheading(270)
t.forward(50)
t.setheading(0)
for i in range(24):
     t.fd(45)
     t.bk(45)
     t.lt(15)
t.setheading(90)
t.forward(50)
t.setheading(0)
t.color("black")
t.forward(150)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(100)
t.rt(90)

t.goto(0,100)
rectangle("green")








