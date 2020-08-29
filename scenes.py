from objects import *
from complex import *
from group import Group
import pygame
from colors import *
from buy import Generate_Buttons


# class that returns builds and returns Groups
class Scenes:
	def get_main_menu(scr, resp, resp2, resp3):
		objs = Group()
		objs.append(Text(scr, "Exoptable Money", 200, 20, 100, WHITE))
		objs.append(Text(scr, "Pre-Alpha Build - Ver 0.3", 1040, 700, 20, WHITE))
		# the money machine:
		# objs.append(Rect(scr, BLACK, 400, 420, 300, 300))
		# objs.append(Rect(scr, BLACK, 700, 500, 200, 50))
		# objs.append(Rect(scr, BLACK, 900, 500, 50, 200))
		objs.append(Text_Button(scr, "Resume Thy Journey", 50, 250, 50, WHITE, DARK_GREEN, resp=resp))
		objs.append(Text_Button(scr, "Start Thy Journey Anew", 50, 350, 50, WHITE, DARK_GREEN, resp=resp2))
		objs.append(Text_Button(scr, "Delete All Thy Data", 50, 450, 50, WHITE, DARK_GREEN, resp=resp3))
		return objs

	def get_shop_menu(game):
		# this is basically what this function does
		# objs = Group()
		# buttons = Generate_Buttons()
		# for button in buttons:
		# 	objs.append(button)
		# return objs
		# Group.create creates a Group object and auto appends a list into it
		return Group.create(Generate_Buttons(game))
