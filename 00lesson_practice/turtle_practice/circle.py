import turtle as t

cl=("red","blue","green","yellow","black")

for x in range(270):
    t.pencolor(cl[x%5])
    t.circle(x)
    t.left(90)
t.exitonclick()