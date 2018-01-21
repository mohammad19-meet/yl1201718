from turtle import *
import turtle
import math
import random
colormode(255)


running = True
sleep = 0.0077
screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)


class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)




	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.goto(new_x, new_y)
	

		if right_side_ball >= screen_width:
			self.dx = -self.dx

		elif left_side_ball >= -screen_width:
			self.dx = - self.dx

		elif top_side_ball >= screen_height:
			self.dy = -self.dy

		elif bottom_side_ball >= -screen_height:
			self.dy = -self.dy
