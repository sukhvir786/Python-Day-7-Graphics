import turtle

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light green") 
sc.title("4. Stairs using for loop") 

sh = turtle.Turtle()
sh.showturtle()

for i in range(6):
    sh.left(90)
    sh.forward(40)
    sh.right(90)
    sh.forward(40)
    
for j in range(2):
    sh.right(90)
    sh.forward(240)
    
turtle.done()
