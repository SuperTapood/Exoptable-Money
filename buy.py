from objects import Text_Button, Rect
from colors import *

def Buy_Button(game, value, name, i):
	level = value_dict[name].index(value)
	price = price_dict[name][level]
	reward = value_dict[name][value + 1]
	if price == "max":
		return Null_Button(game, name, i)
	else:
		return Buy_Button_Obj(game, price, name, reward, i)
	return None


class Buy_Button_Obj:
	def __init__(self, game, price, name, reward, i):
		self.price = price
		self.game = game
		self.name = name
		# self.pic = img_dict[name]
		buy_pos = (75 + 200 * i, 200 if i < 8 else 500)
		x, y = buy_pos
		self.buy = Text_Button(self.game.scr, str(price), x, y, 50, BLACK, WHITE, resp=self.buy)
		rect_pos = (x / 3, y - 50)
		x, y = rect_pos
		self.rect = Rect(self.game.scr, BLUE, x, y, 150, 150)
		self.blit_buy_button = self.buy.blit
		self.blit_big_rect = self.rect.blit
		self.reward = reward
		return

	def buy(self):
		self.game.buy(self)
		return

	def blit_img(self):
		## TODO ##
		pass

	def blit(self):
		self.blit_big_rect()
		self.blit_buy_button()
		self.blit_img()
		return
	pass


img_arr = []
value_dict = {"dollars": [1, 5, 10]}
price_dict = {"dollars": [10, 50, "max"]}