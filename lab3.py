import turtle

turtle.register_shape("heart.gif")
#turtle.shape("heart.gif")
turtle.tracer(100)
b = 1
a = 1
for i in range(a):
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(85)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.right(b)
	b = b+1
turtle.mainloop()