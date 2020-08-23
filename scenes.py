from objects import *
from complex import *
from group import Group
import pygame
from colors import *
from buy import Buy_Button, img_arr

class Scenes:
	def get_main_menu(scr, resp):
		fonts = pygame.font.get_fonts()
		objs = Group()
		objs.append(Text(scr, "Exoptable Money", 350, 75, 70, WHITE))
		objs.append(Rect(scr, BLACK, 400, 420, 300, 300))
		objs.append(Rect(scr, BLACK, 700, 500, 200, 50))
		objs.append(Rect(scr, BLACK, 900, 500, 50, 200))
		objs.append(Text_Button(scr, "Begin Thy Journey", 350, 250, 50, WHITE, BLACK, resp=resp))
		return objs

	def get_shop_menu(game):
		objs = Group()
		# for value, name, img in zip(game, img_arr):
		# 	objs.append(const(game, value, name, img))
		values = [game.values[item] for item in game.values]
		names = [item for item in game.values]
		for value, name, i in zip(values, names, range(len(names))):
			objs.append(Buy_Button(game, value, name, i))
		return objs
