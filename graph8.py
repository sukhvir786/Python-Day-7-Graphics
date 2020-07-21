import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light green") 
sc.title("8. fill Polygon") 
sh = turtle.Turtle()

sh.fillcolor("yellow")
sh.begin_fill()
sh.pencolor("blue")
sh.pensize(3)
sh.showturtle()
for i in range(5):
    sh.forward(100)
    sh.left(72)
sh.end_fill()

turtle.done()
