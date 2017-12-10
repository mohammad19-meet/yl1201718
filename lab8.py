from turtle import *
import turtle
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

a = Ball(10, "blue",5)
a.pu()
a.goto(100,100)
a.pd()
b = Ball(3, "red", 1)
b.pu()
b.goto(100,100)
b.pd()

ball1_x = a.xcor()
ball1_y = a.ycor()
ball2_x = b.xcor()
ball2_y = b.ycor()

a_placex = random.randint(-200, 200)
a_placey = random.randint(-200, 200)

b_placex = random.randint(-200, 200)
b_placey = random.randint(-200, 200)

def Check_collisions(ball1,ball2):
	if (ball1.shapesize()[0] + ball2.shapesize()[0]) >= math.sqrt(math.pow(ball1_x - ball2_x,2)+math.pow(ball1_y - ball2_y,2)):
		ball1.color('green')
		ball2.color('yellow')
	if b.shapesize()[0] < a.shapesize()[0]:
		b.pu()
		b.goto(a_placex,a_placey)
		a.pu()
		a.goto(b_placex,b_placey)
	else:
		a.pu()
		a.goto(placex,placey)


Check_collisions(a,b)
turtle.mainloop()