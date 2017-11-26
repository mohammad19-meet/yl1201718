from turtle import * 
import random

colormode(255)



class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		# self.color(red,green,blue)
	def random_color(self):
		red = random.randint(0,255)
		blue = random.randint(0,255)
		green = random.randint(0,255)
		print(red,green,blue)

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.hideturtle()
		self.width = width
		self.height = height
		register_shape("rectangle", ((height,0), (height,width), (0,width), (0,0)))
		shape("rectangle")
		self.setheading(90)

class Square2(Rectangle):
	def __init__(self,size):
		Turtle.__init__(self)
		Rectangle.__init__(self,size,size)
		self.shape("square")
		self.shapesize(size)

class Hexagon(Turtle):
	def __init__(self,len):
		Turtle.__init__(self)
		penup()
		self.len = len
		setheading(90)
		self.begin_poly()
		for i in range(6):
			self.pu()
			self.fd(len)
			self.right(60)
			self.pd()
		self.end_poly()
		hex = self.get_poly()
		register_shape("hexagon",hex)
		self.shape("hexagon")


hexagon = Hexagon(50)

#Hexagon(4)
#square1 = Square(5)
#square1.random_color()

#rectangle1 = Rectangle(500,200)
#Square1 = Square2(40)
mainloop()