import pygame
from scenes import Scenes
from colors import *
from complex import Machine, HUD, FPS_Counter, Dis
from time import time
from group import Group
from fallables import Dollar
from pygame.mouse import get_pos
import json
from os import remove as delete
from time import sleep as wait
import inspect


# *slaps class*
# this bad boy can fit so many goddamn attributes in it
# lol __slots__ will be a nightmare to implement lmao

class Game:
	def __init__(self):
		pygame.init()
		# screen isn't 1080p because development is easier with 720p because it doesn't fill up my screen
		self.X = 1280
		self.Y = 720
		self.scr = pygame.display.set_mode((self.X, self.Y))
		pygame.display.set_caption("EXOPTABLE MONEY")
		self.fill = self.scr.fill
		self.machine = Machine(self.scr)
		self.HUD = HUD(self.scr, self)
		self.dis = Dis(self.scr)
		self.moneys = 8654105
		self.constructors = {"dollars": Dollar}
		self.maxes = {"dollars": 1}
		self.current_values = {"dollars": 1}
		self.prices = {"Machine": [100, 250, 500], "dollars": [50, 100, 200]}
		self.values = {"Machine": [None, None, None], "dollars": [2, 5, 10]}
		self.levels = {"Machine": -1, "dollars": -1}
		self.names = ["Machine", "dollars"]
		dollars = Group(name="dollars")
		self.groups = [dollars]
		self.main_menu = Scenes.get_main_menu(self.scr, self.__game_n_load, self.game, self.del_data)
		self.shop_menu = Scenes.get_shop_menu(self)
		self.fps_counter = FPS_Counter(self.scr)
		self.update = pygame.display.update
		return

	def __game_n_load(self):
		self.load()
		self.game()
		return

	def show_dis(self):
		while True:
			self.fill(BLACK)
			self.__check_exit()
			self.dis.blit()
			if self.dis["yes"]:
				true = True
				break
			if self.dis["no"]:
				true = False
				break
			self.update()
		return true


	def del_data(self):
		if self.show_dis():
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
		# this is stupid, could use __getitem__ instead but this is more intuitive(?)
		return self.constructors[name]

	def make_money(self):
		# fill all of the money groups
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
		# remove objects that are no longer on screen and add moneys to player
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
			self.update()
		return

	def start(self):
		while True:
			self.fill(DARK_GREEN)
			self.main_menu.blit()
			self.__check_exit()
			self.update()
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
			self.update()
		return

	def save(self):
		with open("data.json", "w") as file:
			json.dump(self.data_generate(), file)
		return


	def data_generate(self):
		# generate the save data I need
		arr = []
		arr.append(self.moneys)
		arr.append(self.maxes)
		arr.append(self.current_values)
		arr.append(self.levels)
		return arr

	def load(self):
		# my patent-pending brilliant loading function
		try:
			data = json.load(open("data.json", "r"))
			self.moneys = data[0]
			for key, _, _ in zip(data[1], data[2], data[3]):
				self.maxes[key] = maxes[key]
				self.current_values[key] = values[key]
				self.levels[key] = levels[key]
		except Exception as e:
			pass
		return

	def increase_maxes(self):
		for key in self.maxes:
			self.maxes[key] += 1
		return

	def buy(self, button):
		# a few logic rules for the buying process
		if self.moneys - button.price >= 0:
			self.moneys -= button.price
			self.levels[button.name] += 1
			if button.name == "Machine":
				self.increase_maxes()
			else:
				self.current_values[button.name] = self.values[button.name][button.level]
			button.update(self)
		return
	pass