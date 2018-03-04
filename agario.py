from turtle import *
SCORE = 0
import turtle
import random
import math
import time
from Ball import *
import pygame

pygame.init()

clapping = pygame.mixer.Sound("clapping.ogg")

losing = pygame.mixer.Sound("lose.ogg")

turtle.title("Agario")

turtle.tracer(0)

#turtle.hideturtle()
getscreen().setup(1.0, 1.0)

turtle.bgcolor("black")

running = True
SLEEP = 0.0077

screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)


turtle.register_shape("score.gif")
turtle.shape("score.gif")
turtle.pu()
turtle.goto(-595,339)






my_ball = Ball(0,0,0,0,50, "red")



number_of_balls = 10 
minimum_ball_radius = 10
maximum_ball_radius = 50
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
balls = []



m_f_r = 10
M_f_r = 10
maximum_food_number = 10
FOOD = []



for i in range(number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	if dx == 0:
		dx += random.randint(int(minimum_ball_dx ),int (maximum_ball_dx))
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	if dy == 0:
		dy += random.randint(int(minimum_ball_dy ),int (maximum_ball_dy))
	radius = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

	

	while x - radius < 100 and x - radius > 100 and y - radius < 100 and y + radius > -100:
		x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
		y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)

	ball = Ball(x,y,dx,dy,radius,color)
	

	balls.append(ball)



ctdwn = Turtle()
ctdwn.hideturtle()
ctdwn.clear()
ctdwn.color("white")
ctdwn.write("3", move=False, align="center", font=("Arial", 200, "bold"))
time.sleep(1)
ctdwn.clear()
ctdwn.write("2", move=False, align="center", font=("Arial", 200, "bold"))
time.sleep(1)
ctdwn.clear()
ctdwn.write("1", move=False, align="center", font=("Arial", 200, "bold"))
time.sleep(1)
ctdwn.clear()

turtle.bgpic("Agario.png")


def options():
	def Replay():
		pass
	def MainMenu():
		turtle.clearscreen()
		import mainMenu
	def Quit():
		quit()


	turtle.onkey(Replay,"r")
	turtle.onkey(MainMenu, "m")
	turtle.onkey(Quit, "q")

	turtle.listen()






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



def createFood():
	isCreateFood = random.random()

	if isCreateFood < 0.2 and len(FOOD) < maximum_food_number:
		x = random.randint(-screen_width + m_f_r, screen_width - m_f_r)
		y = random.randint(-screen_height + m_f_r, screen_height - m_f_r)
		radius = random.randint(M_f_r, m_f_r)
		#color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		color = (0,200,0)
		food = Ball(x, y, 0, 0, radius, color)
		FOOD.append(food)





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
		if collide(my_ball,ball)==True:
			radius1=my_ball.r
			radius2=ball.r

			if radius1<radius2:
				return False
			else:
					my_ball.r=radius1+1
					x=random.randint(int(-screen_width) + int(maximum_ball_radius), int(screen_width) - int(maximum_ball_radius))
					y=random.randint(int(-screen_width) + int(maximum_ball_radius), int(screen_width) - int(maximum_ball_radius))
					dx=random.randint(int(minimum_ball_dx ),int (maximum_ball_dx))
					dy=random.randint(int(minimum_ball_dy ),int (maximum_ball_dy))
					r=random.randint(int(minimum_ball_radius),int(maximum_ball_radius))
					color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))


					while dx==0:
						dx=random.randint(int(minimum_ball_dx ),int (maximum_ball_dx))
					while dy==0:
						dy=random.randint(int(minimum_ball_dy ),int (maximum_ball_dy))



					ball.goto(x,y)
					ball.dx=dx
					ball.dy=dy
					ball.r=r
					ball.shapesize(r/10)
					radius1+=1
					my_ball.shapesize(radius1/10)

			if my_ball.r == 55:
#				image = Turtle()
				turtle.clearscreen()
				turtle.register_shape("YouWin.gif")
				turtle.shape("YouWin.gif")
				turtle.goto(0,0)
				clapping.play()
				time.sleep(8)
				quit()


	return True


def movearound(event):
	my_ball.goto(event.x - screen_width, screen_height - event.y)

getcanvas().bind("<Motion>", movearound)
getscreen().listen()


def col_food():
	index = 0
	for food in FOOD:
		if collide(my_ball, food) == True:
			my_ball.r += 1
			x=random.randint(int(-screen_width) + int(maximum_food_number), int(screen_width) - int(maximum_food_number))
			y=random.randint(int(-screen_width) + int(maximum_food_number), int(screen_width) - int(maximum_food_number))
			radius = random.randint(maximum_food_number, maximum_food_number)


			food.move(x,y)

			



def score():
	score = Turtle()
	score.hideturtle()
	#score.register_shape("score.gif")
	#score.shape("score.png")
	score.pu()
	score.color("white")
	score.goto(-600,310)
	turtle.clear()
#	score.write(str(SCORE), font = ("Arial", 18, "italic"))
	score.write(str(int((my_ball.r-24) + 1)), False, "left", font=("Arial", 20, "italic"))
	score.clear()







while running == True:
	if screen_width != getcanvas().winfo_width()/2 or screen_height!=getcanvas().winfo_height()/2:
		screen_width = getcanvas().winfo_width()/2 
		screen_height=getcanvas().winfo_height()/2
	move_all_balls()
	check_myball_collision()
	createFood()
#	col_food()
	score()
	checkAllBallsCollision()
	#options()
	my_ball.move(screen_width,screen_height)
	running = check_myball_collision()
	update()
	time.sleep(sleep)
	if running == False:
		turtle.clearscreen()
		losing.play()
		turtle.register_shape("YouLose.gif")
		turtle.shape("YouLose.gif")
		turtle.goto(0,0)
		time.sleep(5)

		
options()

time.sleep(0.5)
