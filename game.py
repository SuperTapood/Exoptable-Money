import pygame
from scenes import Scenes
from colors import *
from complex import Machine, HUD, FPS_Counter
from time import time
from group import Group
from fallables import Dollar
from pygame.mouse import get_pos
import json
from os import remove as delete
from time import sleep as wait
import inspect


class Game:
	def __init__(self):
		pygame.init()
		self.X = 1280
		self.Y = 720
		self.scr = pygame.display.set_mode((self.X, self.Y))
		pygame.display.set_caption("EXOPTABLE MONEY")
		self.fill = self.scr.fill
		self.machine = Machine(self.scr)
		self.HUD = HUD(self.scr, self)
		self.moneys = 0
		self.constructors = {"dollars": Dollar}
		self.maxes = {"dollars": 1}
		self.current_values = {"dollars": 1}
		self.prices = {"dollars": [50, 100, 200]}
		self.values = {"dollars": [2, 5, 10]}
		self.levels = {"dollars": -1}
		self.names = ["dollars"]
		dollars = Group(name="dollars")
		self.groups = [dollars]
		self.main_menu = Scenes.get_main_menu(self.scr, self.__game_n_load, self.game, self.del_data)
		self.shop_menu = Scenes.get_shop_menu(self)
		self.fps_counter = FPS_Counter(self.scr)
		return

	def __game_n_load(self):
		self.load()
		self.game()
		return

	def show_dis(self):
		## warn user from deleting data on accident ##
		## TODO ##
		pass

	def del_data(self):
		self.show_dis()
		try:
			delete("data.json")
		except Exception as e:
			pass
		self.start()
		return


	def __check_exit(self):
		# print(get_pos())
		self.fps_counter.blit()
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
				group.append(self.get_const(top)(self.scr, self.current_values[top], self.machine))
		return

	def blit_groups(self):
		for group in self.groups:
			group.blit()
		return

	def clean_groups(self):
		for group, value in zip(self.groups, self.current_values):
			count = group.remove(lambda obj: obj.y > 800 or obj.y < 0, count=True)
			self.moneys += count * self.current_values[value]
		return

	def game(self):
		while True:
			self.fill(DARK_GREEN)
			self.machine.blit()
			self.update_HUD()
			if self.machine.active:
				self.make_money()
			self.blit_groups()
			self.clean_groups()
			self.__check_exit()
			pygame.display.update()
		return

	def start(self):
		while True:
			self.fill(DARK_GREEN)
			self.main_menu.blit()
			self.__check_exit()
			pygame.display.update()
		return

	def shop(self):
		while True:
			self.blit_groups()
			self.fill(DARK_GREEN)
			self.__check_exit()
			if self.machine.active:
				self.make_money()
			self.clean_groups()
			self.shop_menu.blit()
			self.update_HUD()
			pygame.display.update()
		return

	def data_generate(self):
		dic = {}
		members = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
		exclude = ["HUD", "X", "Y", "constructors", 
		"fps_counter", "groups", "machine",  "main_menu", "names",
		"scr", "shop_menu"]
		for mem in members:
			att = mem[0]
			value = mem[1]
			if not att[:2] == att[-2:] == "__":
				if att not in exclude:
					dic[att] = value
		return dic

	def save(self):
		with open("data.json", "w") as file:
			json.dump(self.data_generate(), file)
		return

	def load(self):
		try:
			data = json.load(open("data.json", "r"))
			for entry in data:
				setattr(self, entry, data[entry])
		except Exception as e:
			pass
		return

	def buy(self, button):
		if self.moneys - button.price >= 0:
			self.moneys -= button.price
			self.current_values[button.name] = self.values[button.name][button.level]
			self.levels[button.name] += 1
			button.update(self)
		return
	pass