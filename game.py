import pygame
from scenes import Scenes
from colors import *
from complex import Machine, HUD, FPS_Counter, Dis
from time import time
from group import Group
from fallables import Dollar, Coin
from pygame.mouse import get_pos
import json
from os import remove as delete
import os
from time import sleep as wait
import inspect
from letters import Letter_Placeholder, Letters
from sprite_manager import get_sprites
from location import Director


# *slaps class*
# these bad boys can fit so many goddamn attributes in them
# __slots__ will be such a nightmare to implement lmao

class Game_Type:
	def __init__(self):
		pygame.init()
		self.X = 1280
		self.Y = 720
		self.scr = pygame.display.set_mode((self.X, self.Y))
		pygame.display.set_caption("EXOPTABLE MONEY")
		self.fill = self.scr.fill
		self.fps_counter = FPS_Counter(self.scr)
		self.update = pygame.display.update
		self.default_settings = {"Show FPS Counter": True, "Cap FPS To 60": False}
		self.create_config()
		self.current_settings = self.get_settings()
		self.clock = pygame.time.Clock()
		return

	def create_config(self):
		files = os.listdir(os.path.dirname(__file__))
		if "config.json" in files:
			pass
		else:
			self.reset_config()
		return

	def reset_config(self):
		with open("config.json", "w") as file:
			json.dump(self.default_settings, file)
		return

	def get_settings(self):
		try:
			current_settings = {}
			with open("config.json", "r") as file:
				data = json.load(file)
				for key in data:
					current_settings[key] = data[key]
				return current_settings
		except Exception as e:
			print(e)
			self.reset_config()
			return self.get_settings()
		return


	def check_exit(self):
		if self.get_settings()["Cap FPS To 60"]:
			self.clock.tick(60)
		if self.get_settings()["Show FPS Counter"]:
			self.fps_counter.blit()
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
		return

	def save_config(self):
		with open("config.json", "w") as file:
			json.dump(self.current_settings, file)
		return

class Game(Game_Type):
	def __init__(self):
		super().__init__()
		self.money = Money()
		self.blit_money = self.money.start
		self.menu = Scenes.get_games_menu(self)
		self.settings = Scenes.get_settings(self)
		self.credits = Scenes.get_credits(self)
		self.settings_else = Scenes.get_settings_else(self)
		return

	def start(self):
		while True:
			self.fill(BLACK)
			self.check_exit()
			self.menu.blit()
			self.update()
		return

	def update_config(self, setting_value):
		setting, value = setting_value
		if self.current_settings[setting] != value:
			self.current_settings[setting] = value
			self.save_config()
		return

	def blit_settings(self):
		while True:
			self.fill(BLACK)
			self.check_exit()
			self.settings_else.blit()
			self.settings.blit()
			for setting in self.settings:
				self.update_config(setting.get_status())
			self.update()
		return

	def blit_credits(self):
		while True:
			self.fill(BLACK)
			self.check_exit()
			self.credits.blit()
			self.update()
		return
	pass

class Money(Game_Type):
	def __init__(self):
		super().__init__()
		self.sprites = get_sprites()
		self.director = Director(self)
		self.machine = Machine(self.scr, self.sprites)
		self.HUD = HUD(self.scr, self)
		self.dis = Dis(self.scr)
		self.moneys = 8654105
		self.constructors = {"dollars": Dollar, "coins": Coin}
		self.maxes = {"Machine": 0, "dollars":5, "coins": 5}
		self.current_values = {"Machine": 0, "dollars": 1, "coins": 0}
		self.prices = {"Machine": [100, 250, 500], "dollars": [50, 100, 200], "coins": [200, 500, 1000]}
		self.values = {"Machine": [None, None, None], "dollars": [2, 5, 10], "coins": [5, 10, 20]}
		self.levels = {"Machine": -1, "dollars": -1, "coins": -1}
		self.names = ["Machine", "dollars", "coins"]
		self.unlocked = {"Machine": True, "dollars": True, "coins": False}
		dollars = Group(name="dollars")
		coins = Group(name="coins")
		machine = Group(name="Machine")
		self.groups = [machine, dollars, coins]
		self.thresholds = {100: False}
		self.main_menu = Scenes.get_money_main(self.scr, self.__game_n_load, self.game, self.del_data)
		self.shop_menu = Scenes.get_money_shop(self)
		self.letters = Letters(self, self.scr, self.thresholds, self.sprites)
		self.active_letter = Letter_Placeholder()
		return

	def __game_n_load(self):
		self.load()
		self.game()
		return

	def done(self, key):
		self.thresholds[key] = True
		self.active_letter = Letter_Placeholder()
		return

	def show_dis(self):
		while True:
			self.fill(BLACK)
			self.check_exit()
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

	def update_HUD(self):
		self.HUD.update(money = self.moneys)
		return

	def get_const(self, name):
		# this is stupid, could use __getitem__ instead but this is more intuitive(?)
		return self.constructors[name]

	def check_inbox(self):
		for key in self.thresholds:
			if not self.thresholds[key]:
				if self.moneys >= key:
					self.active_letter = self.letters[key].reset()
		return

	def refill_director(self):
		for key in self.maxes:
			if key == "Machine":
				continue
			left = self.maxes[key] - self.director.count(key)
			if left > 0:
				self.director.add(key, left)
		return

	def clean_director(self):
		for key in self.director:
			for loc in self.director.blit_dict[key]:
				if loc.y > 800 or loc.y < 0:
					self.moneys += self.current_values[loc.type]
					self.director.blit_dict[key].remove(loc)
		return

	def game(self):
		while True:
			self.fill(DARK_GREEN)
			self.machine.blit()
			self.update_HUD()
			if self.machine.active:
				self.refill_director()
			self.director.blit()
			self.clean_director()
			if type(self.active_letter) == Letter_Placeholder:
				self.check_inbox()
			self.active_letter.blit()
			self.check_exit()
			self.update()
		return

	def start(self):
		while True:
			self.fill(DARK_GREEN)
			self.main_menu.blit()
			self.check_exit()
			self.update()
		return

	def shop(self):
		while True:
			self.fill(DARK_GREEN)
			self.check_exit()
			if self.machine.active:
				self.refill_director()
			self.clean_director()
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
			for key, _, _ in zip(maxes := data[1], values := data[2], levels := data[3]):
				self.maxes[key] = maxes[key]
				self.current_values[key] = values[key]
				self.levels[key] = levels[key]
			self.shop_menu = Scenes.get_money_shop(self)
		except Exception as e:
			# print(e)
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

	def unlock(self, unlocks):
		for un in unlocks:
			self.unlocked[un] = unlocks[un]
		self.shop_menu = Scenes.get_money_shop(self)
		return
	pass
