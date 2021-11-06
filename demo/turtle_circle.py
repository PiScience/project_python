import turtle 

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

i = 0
for i in range(0, 100, 5):
    for colors in ['red', 'magenta', 'blue', 'cyan', 'crimson', 'green', 'yellow', 'white']:
        turtle.color(colors)
        turtle.circle(i)
        turtle.right(45)
    
turtle.showturtle()
turtle.done()
