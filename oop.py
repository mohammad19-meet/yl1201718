import random

class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		self.food = food
		print("Yummy!! " + self.name + " is eating " + self.food)
	def description(self):
		print(self.name + " is " + str(self.age) + "years old and loves the color" + self.favorite_color)
	def msound(self):
		print(self.sound * 2)



sheep = Animal("mooo", "shoopie",4,"Red")
sheep.eat("Pizza")
sheep.msound()

class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def breakfast(self,food):
		self.food = food
		print("yummm " + self.food)
	def fsport(self,sport):
		self.sport = sport
		print("I love " + self.sport)

bruh = Person("bruh", 15, "Jerusalem", "Male")
bruh.breakfast("pizza")
bruh.fsport("Tennis")


class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		a = 0
		for i in range(len(self.lyrics)):
			print(self.lyrics[a])
			a += 1


flower_song = Song(["Roses are red,",
			"Violets are blue,",
			"I wrote this poem for you."])

flower_song.sing_me_a_song()

another_song = ("skrrra,", "bap bap da da,","doo doo.")
another_song1 + ("yo yo,", "yo yoyo,",)

song_list = [another_song1, another_song, flower_song]
