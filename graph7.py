import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light green") 
sc.title("7. Polygon Designing") 

sh = turtle.Turtle()
n = int(input("Enter number of sides : "))
sh.pencolor("blue")
sh.pensize(3)
sh.showturtle()

for i in range(n):
    sh.forward(100)
    sh.left(360//n)
    
turtle.done()