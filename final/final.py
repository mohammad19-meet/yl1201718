from turtle import *
import turtle
import time
import random
import math
import pygame


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()


pu()
colormode(255)
getscreen().setup(1.0,1.0)
tracer(0)
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

turtle.register_shape("player.gif")
turtle.register_shape("target.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("fat.gif")
turtle.register_shape("fast.gif")


bullet_sound = pygame.mixer.Sound("bullet_sound.ogg")
lose = pygame.mixer.Sound("lose.ogg")

turtle.shape("target.gif")

turtle.pu()
turtle.bgcolor("black")
turtle.bgpic("MainMenu.png")
turtle.color("red")
turtle.goto(0,0)
turtle.clear()
turtle.write(str(3) , align="center", font=("Arial", 40, "normal"))
time.sleep(1)
turtle.clear()
turtle.write(str(2) , align="center", font=("Arial", 40, "normal"))
time.sleep(1)
turtle.clear()
turtle.write(str(1) , align="center", font=("Arial", 40, "normal"))
time.sleep(1)
turtle.clear()

def movearound(event):
	turtle.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.bgpic("grass4.gif")

class player(Turtle):
	def __init__(self,x,y,r,health):
		Turtle.__init__(self)
		self.shape("player.gif")
		self.color("green")
		self.goto(x,y)
		self.r = r 
		self.health = health
		self.shapesize(r/10)

class Bullet(Turtle):
	def __init__(self,dx,dy,r):
		Turtle.__init__(self)
		self.pu()
		self.ht()
		self.goto(0, 0)
		self.st()
		self.r = r
		self.dx = dx
		self.dy = dy
		self.shape("bullet.gif")
		self.shapesize(r/10)
		self.color("yellow")

	def move(self):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy

		self.goto(new_x, new_y)

number_of_zombies = 10
zombie_list = []

class Zombie(Turtle):
	def __init__(self,x,y,dx,dy,r,color,pic):
		Turtle.__init__(self)
		self.pu()
		self.shape(pic)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.x = x
		self.y = y
		self.shapesize(r/10)
		self.goto(x,y)
		self.color(color)
		#self.shape("fat.gif")

	def move(self):
		global new_x , new_y
		current_x = self.xcor()
		current_y = self.ycor()

		if current_x > 0:
			new_x = current_x - self.dx
		if current_x < 0:
			new_x = current_x + self.dx
		if current_y > 0:
			new_y = current_y - self.dy
		if current_y < 0:
			new_y = current_y + self.dx

		self.goto(new_x,new_y)

x_1 = 550
y_1 = 450
fast_zombie_dx_dy = 2
fat_zombe_dx_dy = 1
def make_zombie():
	for i in range(int(number_of_zombies/2)):
		radnom_X = random.randint(-x_1,x_1)
		while radnom_X == 0:
			radnom_X = random.randint(-x_1,x_1)
		random_y_list =[y_1,-y_1]
		random_y = random.choice(random_y_list)
		fat_zombe = Zombie(radnom_X , random_y,fat_zombe_dx_dy,fat_zombe_dx_dy,20,"red","fat.gif")
		zombie_list.append(fat_zombe)
		radnom_X = random.randint(-x_1,x_1)
		while radnom_X == 0:
			radnom_X = random.randint(-x_1,x_1)
		random_y = random.choice(random_y_list)
		fast_zombe = Zombie(radnom_X,random_y,fast_zombie_dx_dy,fast_zombie_dx_dy,10,"blue","fast.gif")
		zombie_list.append(fast_zombe)

def move_dem_zombies():
	for variable in range(len(zombie_list)):
		zombie_list[variable].move()

player_list = []
player1 = player(0,0,10,5)
player_list.append(player1)
Bullets = []

def create_bullet(event):
	bullet_sound.play()
	global NUMBER_OF_BULLETS , Bullets
	NUMBER_OF_BULLETS = 1
	for i in range(NUMBER_OF_BULLETS):
		x = 0
		y = 0
		dx = event.x - SCREEN_WIDTH - x
		dy = SCREEN_HEIGHT - event.y - y
		new_bullet = Bullet(dx/30, dy/30,4)
		Bullets.append(new_bullet)
		new_bullet.move()
	

def check_collide(zombie,bullet):
	if zombie == bullet:
		return False
						#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
	distance = ((zombie.xcor()-bullet.xcor())**2 +(zombie.ycor()-bullet.ycor())**2)**0.5

	if distance+5 <= (zombie.r+bullet.r):
		return True 
	else:
		return False

def check_all_collions():
	for zombie in zombie_list:
		for bullet in Bullets:
			if check_collide(zombie,bullet):

				random_numberx = random.randint(-700,700)
				random_numbery = random.randint(-700,700)
				zombie.goto(random_numberx,random_numbery)

				idkkk = Bullets[-1]
				Bullets.remove(idkkk)
				bullet.goto(-5000,-5000)

healthturtle = turtle.clone()
healthturtle.ht()


def check_player_collision():
	for zombie in zombie_list:
		for player in player_list:
			if check_collide(zombie,player):
				random_numberx = random.randint(-700,700)
				random_numbery = random.randint(-700,700)
				zombie.goto(random_numberx,random_numbery)
				player.health = player.health - 1
				healthturtle.clear()
				healthturtle.pu()
				healthturtle.goto(450,350)
				healthturtle.write("health : " + str(player1.health), align="center", font=("Arial", 15, "normal"))

				if player.health == 0 :
					turtle.clear()
					turtle.goto(0,0)
					lose.play()
					turtle.write("GAME OVER",align="center",font = ("Arial", 100 , "normal"))
					time.sleep(7)
					bye()



make_zombie()        
getcanvas().bind("<Button-1>", create_bullet)
getcanvas().bind("<Motion>", movearound)
getscreen().listen()

while True:
	move_dem_zombies()
	check_player_collision()
	check_all_collions()
	getscreen().update()
	time.sleep(0.032)

	for bullet in Bullets:
		bullet.move()

turtle.mainloop()