from objects import Rect, Rect_Button, Rect_Text, Text_Button, Text
from colors import *
from time import time
from group import Group

## called those complex object because it sounded cool ##


# the money machine class
# will change to be a picture button later on
# presumably(?) after I draw a money machine
class Machine:
	def __init__(self, scr):
		self.scr = scr
		self.box = Rect(scr, BLACK, 400, 420, 300, 300)
		self.x, self.y, self.w, self.h = self.box.rect
		self.handle_ext = Rect(scr, BLACK, 700, 500, 200, 50)
		# make two different handles for the machine because I am a moron
		# that can't use transformations
		self.non_active_handle = Rect_Button(scr, BLACK, 900, 350, 50, 200, resp = self.click)
		self.active_handle = Rect_Button(scr, BLACK, 900, 500, 50, 200, resp = self.click)
		self.active = False
		return

	def click(self):
		# haha money machine go brrrrr
		self.active = not self.active
		return

	def blit(self):
		if self.active:
			handle = self.non_active_handle
		else:
			handle = self.active_handle
		self.box.blit()
		self.handle_ext.blit()
		handle.blit()
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
		return

	def format(self, num):
		out = ""
		num = num[::-1]
		for i, digit in enumerate(num):
			if i % 3 == 0 and i > 0:
				out += ","
			out += digit
		return out[::-1]

	def update(self, **kwargs):
		# I really wish there was a better way to do this
		self.money.update_text(self.format(str(kwargs["money"])))
		self.money.blit()
		self.save.blit()
		self.load.blit()
		self.buy.blit()
		self.main.blit()
		return
	pass

# FPS counter that will be disabled later on
class FPS_Counter:
	def __init__(self, scr):
		self.counter = Text(scr, "", 1140, 10, 25, WHITE)
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
		return f"{int(fps * 10) / 10} FPS"

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
		self.txt.append(Text(scr, "Are you sure you want to delete the saved data?", 50, 250, 50, WHITE))
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