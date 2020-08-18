from objects import Rect, Rect_Button, Rect_Text
from colors import *



class Machine:
	def __init__(self, scr):
		self.scr = scr
		self.box = Rect(scr, BLACK, 400, 420, 300, 300)
		self.x, self.y, self.w, self.h = self.box.rect
		self.handle_ext = Rect(scr, BLACK, 700, 500, 200, 50)
		self.non_active_handle = Rect_Button(scr, BLACK, 900, 350, 50, 200, resp = self.click)
		self.active_handle = Rect_Button(scr, BLACK, 900, 500, 50, 200, resp = self.click)
		self.active = False
		return

	def click(self):
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


class HUD:
	def __init__(self, scr):
		self.money = Rect_Text(scr, "0", 100, 50, 50, BLACK, WHITE)
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
		self.money.update_text(self.format(str(kwargs["money"])))
		self.money.blit()
		return
	pass
