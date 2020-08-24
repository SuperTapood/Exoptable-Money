from random import randint, uniform
from pygame.draw import *
from colors import GREEN
from time import time
from collision import sprite_sprite_collision


class Falling_Object:
	def __init__(self, scr, value, machine):
		self.value = value
		self.scr = scr
		self.x = 540 - self.w / 2
		self.y = 350
		self.g = 100
		self.last = time()
		self.machine = machine
		## TODO: implement the angle thingy ##
		angle = randint(35, 45)
		self.dir = randint(0, 1)
		self.t = uniform(0.1, 0.3)
		self.ratio = self.__get_ratio(angle)
		self.up = False
		self.remain_time = 3
		self.started = time()
		return

	def __get_ratio(self, angle):
		# some trigonometry for good measure #
		adj = 500
		# adj / hyp = cos(angle) | * hyp
		# adj = cos(angle) * hyp | / cos(angle)
		# adj / cos(angle) = hyp
		hyp = adj / cos(angle)
		op = sqrt(hyp ** 2 - adj ** 2)
		ratio = op / adj
		return ratio

	def go_up(self, a, b):
		self.up = True
		self.started = time()
		return

	def fall(self):
		# temp function, will later replace with an actual physics engine
		# god what did i get myself into
		# | below is a surprise tool that will help us later |
		# V                                                  V
		# if not self.up:
		# 	self.y += self.g * (time() - self.last)
		# 	self.last = time()
		# else:
		# 	self.y -= self.g * (time() - self.last)
		# 	self.last = time()
		# if self.up and time() - self.started >= self.remain_time:
		# 	self.up = False
		# sprite_sprite_collision(self, self.machine, self.go_up)
		if self.dir == 0:
			self.y -= 1 / self.t
			self.x -= self.ratio / self.t
		else:
			self.y -= 1 / self.t
			self.x += self.ratio / self.t
		return


class Dollar(Falling_Object):
	w = 50
	h = 50

	def blit(self):
		rect(self.scr, GREEN, (self.x, self.y, self.w, self.h))
		self.fall()
		return
	pass