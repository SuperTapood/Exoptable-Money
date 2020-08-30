from objects import Text_Button, Rect, Text
from colors import *



def Generate_Buttons(game):
	# dynamically generate all the buy button you can ever think of, BABEE
	# a bit of a headache but it runs once per initiation and saves me from writing
	# a butt load of code
	scr = game.scr
	prices = game.prices
	values = game.values
	levels = game.levels
	names = game.names
	out = []
	for i, name in enumerate(names):
		current_prices = prices[name]
		current_level = levels[name]
		current_values = values[name]
		price = current_prices[current_level + 1]
		value = current_values[current_level + 1]
		out.append(Buy_Button(game, name, price, value, i, current_level + 1))
	return out


class Buy_Button:
	def __init__(self, *args):
		# unpack the args values because I can't be bothered to write all those parameters
		self.game, self.name, self.price, self.value, index, self.level = args
		self.button = Text_Button(self.game.scr, str(self.price), 150 + index * 150, 510 if index < 8 else 710, 50, WHITE, DARK_GREEN, resp=self.buy)
		self.level_button = Text(self.game.scr, f"Level {self.level}", 150 + index * 150, 560 if index < 8 else 760, 30, WHITE)
		self.__lock = False
		return

	def blit(self):
		self.button.blit()
		self.level_button.blit()
		return

	def __update(self):
		# update the text
		self.button.update_text(str(self.price))
		self.level_button.update_text(f"Level {self.level + 1}")
		return

	def lock(self):
		# locking the button prevents IndexOutOfRange Error
		self.__lock = True
		self.price = "MAX"
		return

	def buy(self):
		# prbbly there is a better way but this is fine
		if not self.__lock:
			self.game.buy(self)
		return

	def update(self, game):
		# update the button upon upgrade
		self.level += 1
		if self.level == len(game.values[self.name]):
			self.lock()
		else:
			self.value = game.values[self.name][self.level]
			self.price = game.prices[self.name][self.level]
			self.button.update_text(str(self.price))
		self.__update()
		return
	pass