from objects import Text_Button, Rect
from colors import *



def Generate_Buttons(game):
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
		self.game, self.name, self.price, self.value, index, self.level = args
		self.button = Text_Button(self.game.scr, str(self.price), 150, 510, 50, WHITE, DARK_GREEN, resp=self.buy)
		self.blit = self.button.blit
		self.__lock = False
		return

	def lock(self):
		self.__lock = True
		return

	def buy(self):
		if not self.__lock:
			self.game.buy(self)
		return

	def update(self, game):
		self.level += 1
		if self.level == len(game.values[self.name]):
			self.lock()
		else:
			self.value = game.values[self.name][self.level]
			self.price = game.prices[self.name][self.level]
			self.button.update_text(str(self.price))
		return
	pass