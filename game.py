import pygame
from scenes import Scenes
from colors import *
from complex import Machine, HUD
from time import time
from group import Group
from fallables import Dollar


class Game:
	def __init__(self):
		pygame.init()
		self.X = 1280
		self.Y = 720
		self.scr = pygame.display.set_mode((self.X, self.Y))
		pygame.display.set_caption("EXOPTABLE MONEY")
		self.fill = self.scr.fill
		self.machine = Machine(self.scr)
		self.HUD = HUD(self.scr)
		self.moneys = 0
		self.values = {"dollars": 1}
		self.constructors = {"dollars": Dollar}
		self.maxes = {"dollars": 1}
		dollars = Group(name="dollars")
		self.groups = [dollars]
		return

	def __check_exit(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
		return

	def update_HUD(self):
		self.HUD.update(money = self.moneys)
		return

	def get_const(self, name):
		return self.constructors[name]

	def make_money(self):
		for top, group in zip(self.maxes, self.groups):
			assert top == group.name
			if group < self.maxes[top]:
				group.append(self.get_const(top)(self.scr, self.values[top], self.machine))
		return

	def blit_groups(self):
		for group in self.groups:
			group.blit()
		return

	def clean_groups(self):
		for group, value in zip(self.groups, self.values):
			count = group.remove(lambda obj: obj.y > 800, count=True)
			self.moneys += count * self.values[value]
		return

	def start(self):
		while True:
			start = time()
			self.__check_exit()
			self.fill(DARK_GREEN)
			self.machine.blit()
			self.update_HUD()
			if self.machine.active:
				self.make_money()
			self.blit_groups()
			self.clean_groups()
			pygame.display.update()
			# print(1 / (time()- start))
		return
	pass