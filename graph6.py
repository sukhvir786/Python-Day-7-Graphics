import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light green") 
sc.title("6. Pentagon Designing") 

sh = turtle.Turtle()
sh.pencolor("blue")
sh.pensize(3)
sh.showturtle()

for i in range(5):
    sh.forward(100)
    sh.left(72) # 360//5
    
turtle.done()