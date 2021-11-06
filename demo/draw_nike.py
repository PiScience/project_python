import turtle as tl

tl.hideturtle()

tl.speed(10)

tl.bgcolor('#2d4059')

tl.fillcolor('#28abb9')
tl.begin_fill()
tl.circle(100,35)
tl.forward(500)
tl.left(169)
tl.forward(445)
tl.seth(290)
tl.circle(130,-50)
tl.seth(199)
tl.circle(151,107)
tl.end_fill()

tl.color('#ec0101')
tl.penup()
tl.forward(80)
tl.pendown()
tl.write("NIKE | Just do it",align="left", font=("Comic Sans MS", 30, "normal"))

tl.done()
