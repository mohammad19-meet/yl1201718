from turtle import *
import turtle

turtle.hideturtle()

getscreen().setup(1.0, 1.0)

screen = Screen()


def mainMenu():
	import turtle
	turtle.bgpic("Main_Menu.gif")
	def start():
		turtle.clearscreen()
		import agario

	turtle.onkey(start, "space")

	turtle.listen()

	

mainMenu()

turtle.mainloop()