from turtle import *
import turtle
import math
import random

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		turtle.shape("circle")
		turtle.shapesize(r/10)
		turtle.color("red")

def move(self, screen_width, screen_height):
	current_x = self.xcor()
	current_y = self.ycor()
	new_x = current_x + dx
	new_y = current_y + dy
	right_side_ball = new_x + r
	left_side_ball = new_x - r
	top_side_ball = new_y + r
	bottom_side_ball = new_y - random
	self.goto(new_x, new_y)
	if right_side_ball >= 300:
		new_x = current_x - new_x
	if left_side_ball >= -300:
		new_x = current_x + new_x
	if top_side_ball >= 300:
		new_y = current_y - new_y
	if bottom_side_ball >= -300:
		new_y = current_y + new_y