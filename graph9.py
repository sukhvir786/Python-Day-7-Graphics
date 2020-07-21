import turtle 

sc = turtle.Screen() # let sc for screen
sc.bgcolor("light yellow") 
sc.title("9. STAR formation") 

sh = turtle.Turtle() 
sh.fillcolor("yellow")
sh.begin_fill()
sh.pencolor("blue")
sh.pensize(3)

for i in range(30):
    sh.forward(200) 
    sh.right(140) 
sh.end_fill()
	
turtle.done() 