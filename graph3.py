import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light green") 
sc.title("3. Square using for loop") 

sh = turtle.Turtle()
sh.showturtle()
for i in range(4):
    sh.forward(200)
    sh.left(90)
turtle.done()
