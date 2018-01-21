from turtle import *
import turtle
import random
import time
from Ball import *

#turtle.tracer(0)

turtle.hideturtle()

running = True
sleep = 0.0077
screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)

my_ball = Ball(0,0,10,10,7, "red")

number_of_balls = 5 
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
balls = []

for i in range(number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while dx == 0:
		dx += 1
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	while dy == 0:
		dy += 1
	dy = random.randint(minimum_ball_radius, maximum_ball_radius)
	radius = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

	ball = Ball(x,y,dx,dy,radius,color)
	balls.append(Ball)

def move_all_balls():
	for x in balls:
		x.move(screen_width,screen_height)


while True:
	move_all_balls()
def collide(ball_a,ball,b):
	if ball_a == ball_b:
		return False





turtle.mainloop()