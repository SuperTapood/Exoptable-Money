from objects import *
from group import Group
from colors import BLACK, WHITE, DARK_GREEN, RED, GREEN
from buy import Generate_Buttons
from setting import Setting


# class that returns builds and returns Groups
class Scenes:
	def get_money_main(scr, resp, resp2, resp3):
		objs = Group()
		objs.append(Text(scr, "Exoptable Money", 200, 20, 100, WHITE))
		objs.append(Text_Button(scr, "Resume Thy Journey", 50, 250, 50, WHITE, DARK_GREEN, resp=resp))
		objs.append(Text_Button(scr, "Start Thy Journey Anew", 50, 350, 50, WHITE, DARK_GREEN, resp=resp2))
		objs.append(Text_Button(scr, "Delete All Thy Data", 50, 450, 50, WHITE, DARK_GREEN, resp=resp3))
		return objs

	def get_money_shop(game):
		# this is basically what this function does
		# objs = Group()
		# buttons = Generate_Buttons()
		# for button in buttons:
		# 	objs.append(button)
		# return objs
		# Group.create creates a Group object and auto appends a list into it
		return Group.create(Generate_Buttons(game))

	def get_games_menu(game):
		scr = game.scr
		menu = Group()
		menu.append(Text(scr, "THE MENAGERIE COLLECTION REMAKE", 50, 50, 50, WHITE))
		menu.append(Text_Button(scr, "Exoptable Money", 100, 200, 50, DARK_GREEN, BLACK, resp=game.blit_money))
		menu.append(Text_Button(scr, "Presentable Liberty", 100, 300, 50, RED, BLACK, resp=lambda:None))
		menu.append(Text_Button(scr, "Substantial Archives", 90, 400, 50, RED, BLACK, resp=lambda:None))
		menu.append(Text_Button(scr, "Inexorable Fate", 100, 500, 50, RED, BLACK, resp=lambda:None))
		menu.append(Text_Button(scr, "Settings", 110, 600, 50, GREEN, BLACK, resp=game.blit_settings))
		menu.append(Text(scr, "Alpha Build - Version 0.7", 900, 670, 30, RED))
		return menu


	def get_settings(game):
		settings = Group()
		scr = game.scr
		dic = game.current_settings
		settings.append(Setting(scr, "Show FPS Counter", [True, False], dic['Show FPS Counter'], 0, 150))
		settings.append(Setting(scr, "Cap FPS To 60", [True, False], dic['Cap FPS To 60'], 0, 250))
		return settings

	def get_settings_else(game):
		out = Group()
		scr = game.scr
		out.append(Text(scr, "Settings", 500, 0, 70, WHITE))
		out.append(Text_Button(scr, "Go Back", 500, 650, 50, BLACK, WHITE, resp=game.start, scale=1.3))
		out.append(Text_Button(scr, "Credits", 1050, 650, 50, BLACK, WHITE, resp=game.blit_credits, scale=1.3))
		return out

	def get_credits(game):
		out = Group()
		scr = game.scr
		out.append(Text(scr, "Credits", 500, 20, 70, WHITE))
		out.append(Text(scr, "Wertpol - The OC", 50, 100, 40, WHITE))
		out.append(Text(scr, "master1203 - Cat Stock Image", 50, 150, 40, WHITE))
		out.append(Text_Button(scr, "Go Back", 500, 650, 50, BLACK, WHITE, resp=game.start, scale=1.3))
		return out

	def get_HUD(scr, sprites, pull, buy_bg, save, load):
		money_bg = Image(scr, sprites["money_bg"], 5, -60)
		pulldown = Image_Button(scr, sprites["hud_pulldown"], 1150, 0, resp=pull)
		buy_bg = Image(scr, buy_bg, 0, -500)
		buy_buttons = Group()
		buy_buttons.append(Image_Button(scr, sprites["full_screen"], 1100, -450, resp=lambda: None))
		buy_buttons.append(Image_Button(scr, sprites["save"], 1100, -300, resp=save))
		buy_buttons.append(Image_Button(scr, sprites["load"], 1100, -150, resp=load))
		return money_bg, pulldown, buy_bg, buy_buttons

	def get_money(scr):
		return Text(scr, "0", 25, 50, 50, WHITE)

