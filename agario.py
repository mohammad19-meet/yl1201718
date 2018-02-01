from turtle import *
import turtle
import random
import math
import time
from Ball import *

turtle.tracer(0)

turtle.hideturtle()
getscreen().setup(1.0, 1.0)

turtle.bgcolor("black")

running = True
SLEEP = 0.0077

screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)

my_ball = Ball(0,0,0,0,30, "red")

number_of_balls = 20 
minimum_ball_radius = 10
maximum_ball_radius = 25
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
balls = []

for i in range(number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	if dx == 0:
		dx += 1
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	if dy == 0:
		dy += 1
	radius = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

	ball = Ball(x,y,dx,dy,radius,color)
	
	balls.append(ball)

	while x - radius < 100 and x - radius > 100 and y - radius < 100 and y + radius > -100:
		x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
		y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
def move_all_balls():
	for i in balls:
		i.move(screen_width,screen_height)



def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

	
	balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5
	if balls_distance+10 <= ball_a.r+ball_b.r:
		return True
	else:
		return False




def checkAllBallsCollision():
	for ball_a in balls:
		for ball_b in balls:
			if collide(ball_a,ball_b) == True:
				r_x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
				r_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
				r_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				while r_dx == 0:
					r_dx = random.randint(minimum_ball_dx, maximum_ball_dx)
				r_dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				while r_dx == 0:
					r_dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				r_r = random.randint(minimum_ball_radius, maximum_ball_radius)
				r_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
			
				if ball_a.r > ball_b.r:
					ball_b.goto(r_x,r_y)
					ball_b.dx = r_dx
					ball_b.dy = r_dy
					ball_b.r = radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color
					ball_a.r += 0.5
					ball_a.shapesize(ball_a.r/10)
					
				elif ball_a.r < ball_b.r:
					ball_a.goto(r_x,r_y)
					ball_a.dx = r_dx
					ball_a.dy = r_dy
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color
					ball_b.r += 0.5
					ball_b.shapesize(ball_b.r/10)
			
def check_myball_collision():
	for ball in balls:
		r_x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
		r_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
		r_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while r_dx == 0:
			r_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		r_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while r_dy == 0:
			r_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		if collide(my_ball,ball) == True:
			if my_ball.r < ball.r:
				print("Game Over")
				return False
			else:
				my_ball.r += 2
				my_ball.shapesize(my_ball.r/10)
				ball.goto(r_x,r_y)
				ball.dx = r_dx
	return True 


def movearound(event):
	my_ball.goto(event.x - screen_width, screen_height - event.y)

getcanvas().bind("<Motion>", movearound)
getscreen().listen()

while running == True:
	if screen_width != getcanvas().winfo_width()/2 or screen_height!=getcanvas().winfo_height()/2:
		screen_width = getcanvas().winfo_width()/2 
		screen_height=getcanvas().winfo_height()/2
	move_all_balls()
	check_myball_collision()
	checkAllBallsCollision()
	my_ball.move(screen_width,screen_height)
	running = check_myball_collision()
	update()
	time.sleep(sleep)
time.sleep(2)
