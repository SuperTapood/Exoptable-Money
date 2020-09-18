from random import randint, uniform
from pygame.draw import *
from colors import GREEN
from time import time
from collision import sprite_sprite_collision
from math import sin, cos, sqrt
import pygame


# this has a lot of code so I will be able to add new objects more easily
class Falling_Object:
	def __init__(self, scr, value, machine, sprite):
		self.sprite = sprite
		self.value = value
		self.scr = scr
		_, _, self.w, self.h = sprite.get_rect()
		self.x = 540 - self.w / 2
		self.y = 350
		self.g = 100
		self.last = time()
		self.machine = machine
		## TODO: implement the angle thingy ##
		angle = randint(35, 45)
		self.dir = randint(0, 1)
		self.t = uniform(2, 5)
		self.ratio = self.__get_ratio(angle)
		self.up = False
		self.remain_time = 3
		self.started = time()
		self.angle = 0
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
		#
		# | this is a surprise tool that will help us later! |
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

	def rotate(self):
		img_copy = pygame.transform.rotate(self.sprite, self.angle)
		self.scr.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
		self.angle += self.rotation_speed
		return

	def blit(self):
		self.rotate()
		self.fall()
		return
	pass


class Dollar(Falling_Object):
	rotation_speed = 3
	pass

class Coin(Falling_Object):
	rotation_speed = 1
	pass