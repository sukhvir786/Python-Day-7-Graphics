import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light yellow") 
sc.title("10. Concentric Circles") 

sh = turtle.Turtle()
sh.showturtle()
sh.pensize(2)
sh.penup()

for i in range(1,200,15):
    sh.right(90)
    sh.forward(i)
    sh.right(270)
    sh.pendown()
    sh.circle(i)
    sh.penup()
    sh.home()
turtle.done() 