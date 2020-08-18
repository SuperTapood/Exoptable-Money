from random import randint
from pygame.draw import *
from colors import GREEN
from time import time
from collision import sprite_sprite_collision


class Falling_Object:
	def __init__(self, scr, value, machine):
		self.value = value
		self.scr = scr
		self.x = 450
		self.y = 350
		self.g = 50
		self.last = time()
		self.machine = machine
		## TODO: implement the angle thingy ##
		self.angle = randint(0, 180)
		self.up = False
		self.remain_time = 3
		self.started = time()
		return

	def go_up(self, a, b):
		self.up = True
		self.started = time()
		return

	def fall(self):
		# temp function, will later replace with an actual physics engine
		# god what did i get myself into
		if not self.up:
			self.y += self.g * (time() - self.last)
			self.last = time()
		else:
			self.y -= self.g * (time() - self.last)
			self.last = time()
		if self.up and time() - self.started >= self.remain_time:
			self.up = False
		sprite_sprite_collision(self, self.machine, self.go_up)


class Dollar(Falling_Object):
	w = 50
	h = 50

	def blit(self):
		rect(self.scr, GREEN, (self.x, self.y, self.w, self.h))
		self.fall()
		return
	pass