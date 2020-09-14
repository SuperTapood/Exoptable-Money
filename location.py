from random import randint, uniform
from math import cos, sqrt
import pygame
from time import time

class Tracker:
	def __init__(self, _type, w):
		self.type = _type
		self.x = 600 - w / 2
		self.y = 400
		self.ratio = self.__get_ratio(angle=randint(35, 45))
		self.dir = randint(0, 1)
		self.t = uniform(0.1, 0.3)
		self.angle = 0
		self.rotation_speed = uniform(1, 3)
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

	def update(self):
		if self.dir == 0:
			self.y -= 1 / self.t
			self.x -= self.ratio / self.t
		else:
			self.y -= 1 / self.t
			self.x += self.ratio / self.t
		self.angle += self.rotation_speed
		return
	pass


class Director:
	def __init__(self, game):
		self.blit_dict = {'dollars': [], 'coins': []}
		self.imgs = {"coins": game.sprites["coins"], "dollars": game.sprites["dollars"]}
		self.width = {}
		for key in self.imgs:
			_, _, self.width[key], _ = self.imgs[key].get_rect()
		self.scr = game.scr
		return

	def __iter__(self):
		return iter(self.blit_dict)

	def count(self, _type):
		return len(self.blit_dict[_type])

	def add(self, _type, count=1):
		if count > 0:
			self.blit_dict[_type].append(Tracker(_type, self.width[_type]))
			self.add(_type, count=count - 1)
		return

	def blit(self):
		for key in self:
			for loc in self.blit_dict[key]:
				img = pygame.transform.rotate(self.imgs[key], loc.angle)
				self.scr.blit(img, (loc.x - int(img.get_width() / 2), loc.y - int(img.get_height() / 2)))
				loc.update()
		return
	pass