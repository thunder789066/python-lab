import turtle

##color('black', 'blue')
##begin_fill()
##while True:
##    forward(200)
##    left(170)
##    if abs(pos()) < 1:
##        break
##end_fill()
##done() 

#star = turtle.Turtle()

##star = turtle.Turtle()
##
##for i in range(50):
##    star.forward(50)
##    star.right(144)
##    
##turtle.done()
##
##star = turtle.Turtle()
##
##star.color('blue')
##star.begin_fill()
##for i in range(5):
##    star.forward(200)
##    star.right(144)
##star.end_fill()
##turtle.done()

#def draw_star(x : int, y : int, width : int, height : int, color : str):
star = turtle.Turtle()
star.penup()
star.setpos(-200.00, 200.00)
star.pendown()
star.color('blue')
star.begin_fill()
for i in range(5):
    star.forward(200)
    star.right(144)
star.end_fill()
turtle.done()

