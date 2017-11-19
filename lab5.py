from turtle import * 
import turtle
import random

colormode(255)
red = random.randint(0,255)
blue = random.randint(0,255)
green = random.randint(0,255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		self.color(red,green,blue)
	def random_color(self):
		
		print(red,green,blue)

square1 = Square(5)
square1.random_color()
turtle.mainloop()