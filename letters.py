from objects import Text_Button, Text, Rect, Image_Button, Rect_Button, Image
from colors import *
import pygame
from time import sleep as wait
from time import time
from pygame.mouse import get_pos, get_pressed
from sprite_manager import get_sprites
from group import Group


def get_ms(index, scr):
	out = []
	# content = get_sprites()[f"ms_{index}"]
	content = get_sprites()["ms_ex"]
	paper = get_sprites()["ms_paper"]
	paper = Image(scr, paper, 50, 50 + 500)
	out.append(paper)
	out.append(Image(scr, content, 200, 100 + 500))
	x, y, w, h = paper.get_rekt()
	out.append(Rect_Button(scr, BLACK,x, y, w, h, delay_time=0))
	return out


def get_dm(index):
	## TODO LATER ##
	pass


def get_big(index, scr):
	# the indexes at which the letters show up, currently, I want to keep ms' 
	# letters the only ones appearing until I have them all but its best to have
	# the entire framework already
	MS = [index]
	DM = []
	out = Group()
	if index in MS:
		out.append(get_ms(MS.index(index), scr))
	elif index in DM:
		out.append(get_dm(DM.index(index), scr))
	return out


class Letter_Placeholder:
	def blit(self):
		pass


class Letter:
	def __init__(self, game, scr, key, letter_smol, letter_big, unlocks):
		self.unlock = unlocks
		self.game = game
		self.key = key
		self.scr = scr
		self.small = True
		self.big = False
		self.x = 1150
		self.y = 650
		_, _, w, h = Image(scr, letter_smol, self.x, self.y).get_rekt()
		self.small_button = Rect_Button(scr, BLACK, 1150 - w / 2, 650 - h / 2, w, h, resp=self.click)
		self.smol = letter_smol
		self.big_letter = letter_big
		self.big_button = Rect_Button(scr, BLACK, 200, 100, 1156, 561)
		self.angle = 0
		self.t = 0.5
		self.angle_max = 20
		self.base_factor = self.angle_max / self.t
		self.factor = self.base_factor
		self.active_letter = self.smol
		self.done = 1500
		self.yps = 0.05
		return

	def click(self):
		if self.small:
			self.small = False
			self.big = True
			self.last_move = time()
		return

	def letter_blit(self):
		## TODO: add a little climb animation ##
		self.letter_rect.blit()
		self.text1.blit()
		return

	def reset(self):
		self.last = time()
		return self

	def deactivate(self):
		self.game.done(self.key)
		self.game.unlock(self.unlock)
		return

	def blit(self):
		if self.small:
			if self.small_button.is_clicked():
				self.click()
			img_copy = pygame.transform.rotate(self.smol, self.angle)
			self.scr.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
			self.angle += self.factor * (time() - self.last)
			self.last = time()
			if self.angle > self.angle_max:
				self.factor = self.base_factor * -1
			elif self.angle < -self.angle_max:
				self.factor = self.base_factor
		elif self.big:
			for i in range(0, len(self.big_letter) - 1, 1):
				self.big_letter[i].blit()
			move = self.get_move()
			for obj in self.big_letter:
				if self.done > 0:
					obj.move_y(move) 
					self.done -= -move
			mouse = get_pos()
			click = get_pressed()
			x, y, w, h = self.big_letter[-1].rect
			if self.big_button.is_clicked() and self.done <= 0:
				self.deactivate()
		else:
			self.game.active_letter = Letter_Placeholder()
		return

	def get_move(self):
		y = 1 / (time() - self.last_move)
		self.last_move = time()
		return y * self.yps * -1


class Letters:
	def __init__(self, game, scr, dic, sprites):
		letter_smol = sprites["letter"]
		# will add those later when I'll have them in my sprites
		letter_sprites = []
		self.letter_dict = {}
		unlocks = {}
		unlock_index = {0: ["Machine", "dollars", "coins"]}
		scr = game.scr
		for i, key in enumerate(dic):
			big = get_big(i, scr)
			if i in unlock_index:
				new = unlock_index[i]
				for n in new:
					unlocks[n] = True
			self.letter_dict[key] = Letter(game, scr, key, letter_smol, big, unlocks)
		return

	def __getitem__(self, key):
		return self.letter_dict[key]
	pass
