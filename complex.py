from objects import Rect, Rect_Button, Rect_Text, Text_Button, Text, Image, Image_Button
from colors import *
from time import time
from group import Group
from scenes import Scenes
import pygame

## called those complex object because it sounded cool ##


# the money machine class
# will change to be a picture button later on
# prbbly after I draw a money machine
class Machine:
	def __init__(self, scr, sprites):
		self.scr = scr
		box = sprites["machine_base"]
		self.box = Image(scr, box, 400, 350)
		self.x, self.y, self.w, self.h = self.box.get_rekt()
		# make two different handles for the machine because I am a moron
		# that can't use transformations
		handle = sprites["handle_idle"]
		self.non_active_handle = Image_Button(scr, handle, 700, 500, self.click)
		handle = sprites["handle_active"]
		self.active_handle = Image_Button(scr, handle, 700, 370, self.click)
		self.active = False
		return

	def click(self):
		# haha money machine go brrrrr
		self.active = not self.active
		# reset both handles bc they are the same button
		self.active_handle.last_click = time()
		self.non_active_handle.last_click = time()
		return

	def blit(self):
		if self.active:
			handle = self.active_handle
		elif self.active == False:
			handle = self.non_active_handle
		handle.blit()
		self.box.blit()
		return
	pass


# the hud is used to convey info to the player and place buttons
class HUD:
	def __init__(self, scr, game):
		self.money = Rect_Text(scr, "0", 10, 10, 50, BLACK, WHITE)
		self.save = Text_Button(scr, "SAVE", 700, 10, 50, BLACK, WHITE, resp=game.save)
		self.load = Text_Button(scr, "LOAD", 900, 10, 50, BLACK, WHITE, resp=game.load)
		self.buy = Text_Button(scr, "BUY", 700, 100, 50, BLACK, WHITE, resp=game.shop)
		self.main = Text_Button(scr, "MAIN", 900, 100, 50, BLACK, WHITE, resp=game.game)
		self.moneys = 0
		return


	# format the money value to look a bit nicer
	def format(self, num):
		out = ""
		# imma need to reverse the number in order to correctly place the ","
		num = num[::-1]
		for i, digit in enumerate(num):
			if i % 3 == 0:
				if i > 0:
					out += ","
			out += digit
		# reverse the number back so it makes sense
		return out[::-1]

	def update(self, **kwargs):
		# I really wish there was a better way to do this
		# nah for loops would be worse
		if self.moneys != str(kwargs["money"]):
			self.moneys = str(kwargs["money"])
			self.money.update_text(self.format(str(kwargs["money"])))
		self.money.blit()
		self.save.blit()
		self.load.blit()
		self.buy.blit()
		self.main.blit()
		return
	pass

# FPS counter that will be disabled later on
# mere cosmetic
class FPS_Counter:
	def __init__(self, scr):
		self.counter = Text(scr, "", 1140, 10, 25, WHITE)
		self.dec_factor = 10
		self.last = time()
		return

	def __str__(self):
		# spf stands for seconds-per-frame
		# i use it because FPS can sometime not play nice
		spf = time() - self.last
		try:
			fps = 1 / spf
		except ZeroDivisionError:
			fps = 1000
		return f"{int(fps * self.dec_factor) / self.dec_factor} FPS"

	def blit(self):
		self.counter.update_text(str(self))
		self.last = time()
		self.counter.blit()
		return
	pass


# this exists
# why? idk
class Dis:
	def __init__(self, scr):
		self.scr = scr
		self.choices = {"yes": False, "no": False}
		self.txt = Group()
		self.txt.append(Text(scr, "WARNING", 50, 50, 50, WHITE))
		self.txt.append(Text(scr, "Deleted data will not be recoverable", 50, 250, 50, WHITE))
		self.txt.append(Text(scr, "Are you sure you want to delete the saved data?", 50, 450, 50, WHITE))
		self.yes = Text_Button(scr, "YES", 150, 550, 100, RED, GREEN, resp=lambda: self.change_bool("yes"))
		self.no = Text_Button(scr, "NO", 1050, 550, 100, RED, GREEN, resp=lambda: self.change_bool("no"))
		return

	def __getitem__(self, item):
		return self.choices[item]

	def change_bool(self, booly):
		self.choices[booly] = True
		return

	def blit(self):
		self.txt.blit()
		self.yes.blit()
		self.no.blit()
		return
	pass


class new_hud:
	def __init__(self, scr, sprites, save, load):
		buy_bg = pygame.transform.scale(sprites['buy_bg'], (1280, 520))
		self.money_bg, self.pulldown, self.buy_bg, self.buttons = Scenes.get_HUD(scr, sprites, self.pull_menu, buy_bg, save, load)
		self.moneys = 0
		self.money = Scenes.get_money(scr)
		self.factor = 20
		self.moving = 0
		# start down while testing
		self.moving = self.factor
		self.down = False
		self.max = 500
		self.current = 0
		return

	def pull_menu(self):
		if self.down == True:
			self.moving = -self.factor
		elif self.down == False:
			self.moving = self.factor
		return

	def format(self, num):
		out = ""
		# imma need to reverse the number in order to correctly place the ","
		num = str(num)[::-1]
		for i, digit in enumerate(num):
			if i % 3 == 0:
				if i > 0:
					out += ","
			out += digit
		# reverse the number back so it makes sense
		return out[::-1]

	def update(self, moneys):
		self.money_bg.blit()
		self.pulldown.blit()
		self.buy_bg.blit()
		self.buttons.blit()
		self.money_bg.y += self.moving
		self.pulldown.add_Y(self.moving)
		self.current += self.moving
		self.money.y += self.moving
		self.buy_bg.y += self.moving
		self.buttons.shift_y(self.moving)
		if self.current == self.max:
			self.moving = 0
			self.down = True
		if self.current == 0:
			self.moving = 0
			self.down = False
		if moneys != self.moneys:
			self.money.update_text(self.format(moneys))
			self.moneys = moneys
		self.money.blit()
	pass