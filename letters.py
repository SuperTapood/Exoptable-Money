from objects import Text_Button, Text, Rect, Image_Button, Rect_Button, Image
from colors import *
import pygame
from time import sleep as wait
from time import time

class Letter_Placeholder:
	def blit(self):
		pass


class Letter:
	def __init__(self, game, scr, key, letter_smol):
		self.game = game
		self.key = key
		self.scr = scr
		self.small = True
		self.x = 1150
		self.y = 650
		_, _, w, h = Image(scr, letter_smol, self.x, self.y).get_rekt()
		self.small_button = Rect_Button(scr, BLACK, 1150, 650, w, h)
		self.smol = letter_smol
		self.angle = 0
		self.t = 0.5
		self.angle_max = 20
		self.base_factor = self.angle_max / self.t
		self.factor = self.base_factor
		return

	def click(self):
		self.small = False
		return

	def letter_blit(self):
		## TODO: add a little climb animation ##
		self.letter_rect.blit()
		self.text1.blit()
		return

	def reset(self):
		self.last = time()
		return self

	def blit(self):
		if self.small:
			img_copy = pygame.transform.rotate(self.smol, self.angle)
			self.scr.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
			self.angle += self.factor * (time() - self.last)
			self.last = time()
			if self.angle > self.angle_max:
				self.factor = self.base_factor * -1
			elif self.angle < -self.angle_max:
				self.factor = self.base_factor
			if self.small_button.is_clicked():
				self.click()
		else:
			self.game.active_letter = Letter_Placeholder()
		return


class Letters:
	def __init__(self, game, scr, dic, sprites):
		letter_smol = sprites["letter"]
		# will add those later when I'll have them in my sprites
		letter_sprites = []
		self.letter_dict = {}
		for key in dic:
			self.letter_dict[key] = Letter(game, scr, key, letter_smol)
		return

	def __getitem__(self, key):
		return self.letter_dict[key]