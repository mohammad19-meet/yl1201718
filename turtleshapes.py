import turtle

turtle.speed(5)

angle = 144
sideslength = 100

"""for i in range(5):
	turtle.pencolor("red")
	turtle.forward(sideslength)
	turtle.right(angle)
"""
"""turtle.goto(0,50)
turtle.goto(50,50)
turtle.goto(50,0)
turtle.goto(25,-25)
turtle.goto(0,0)"""
turtle.register_shape("Marker", ((0,50),(50,50), (50,0),(25,-25), (0,0)))
turtle.shape("Marker")
turtle.addshape("Marker")
turtle.getshape(turtle.goto(0,50))

turtle.mainloop()