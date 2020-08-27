from pygame.draw import circle, rect, line, polygon
from pygame.mouse import get_pressed, get_pos
from time import time
import pygame


# some mindless object templates

class Rect:
	def __init__(self, scr, color, x, y, w, h, width=0):
		self.scr = scr
		self.color = color
		self.rect = x, y, w, h
		self.width = 0
		return

	def blit(self):
		rect(self.scr, self.color, self.rect, self.width)
		return
	pass
class Button:
	last_click = time()

	def check_click(self):
		# check if the button is being click
		mouse = get_pos()
		click = get_pressed()
		x, y, w, h = self.rect
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1

	def blit(self):
		# implement click delay to prevent instant clicks
		if self.check_click() and time() - self.last_click >= self.delay_time:
			self.last_click = time()
			self.resp()
		return
class Rect_Button(Button):
	def __init__(self, scr, color, x, y, w, h, resp=lambda:None, width=0, delay_time=0.3):
		self.scr = scr
		self.butt = Rect(scr, color, x, y, w, h, width)
		self.resp = resp
		self.rect = x, y, w, h
		self.delay_time = delay_time
		return

	def blit(self):
		self.butt.blit()
		super().blit()
		return
	pass
class Text:
	def __init__(self, scr, txt, x, y, font_size, color, font="freesansbold.ttf"):
		self.scr = scr
		self.x = x
		self.y = y
		self.font_size = font_size
		self.color = color
		self.font = font
		font = pygame.font.Font(self.font, self.font_size)
		self.text = font.render(txt, True, self.color)
		self.rect = self.text.get_rect()
		self.rect.topleft = (self.x, self.y)
		return

	def blit(self):
		self.scr.blit(self.text, (self.rect.x, self.rect.y))
		return

	def get_rekt(self):
		x = self.rect.x
		y = self.rect.y
		w = self.rect.w
		h = self.rect.h
		return x, y, w, h

	def update_text(self, txt):
		font = pygame.font.Font(self.font, self.font_size)
		self.text = font.render(txt, True, self.color)
		self.rect = self.text.get_rect()
		self.rect.topleft = (self.x, self.y)
		return
class Rect_Text:
	def __init__(self, scr, txt, t_x, t_y, size, t_color, r_color):
		self.text = Text(scr, txt, t_x, t_y, size, t_color)
		self.scr = scr
		self.r_color = r_color
		x, y, w, h = self.text.get_rekt()
		self.rect = Rect(scr, r_color, x, y , w, h)
		return

	def blit(self):
		self.rect.blit()
		self.text.blit()
		return

	def update_text(self, new):
		self.text.update_text(new)
		x, y, w, h = self.text.get_rekt()
		self.rect = Rect(self.scr, self.r_color, x, y , w, h)
		return
	pass
class Text_Button:
	def __init__(self, scr, txt, x, y, font_size, t_color, r_color, font="freesansbold.ttf", resp=lambda: None):
		self.text = Text(scr, txt, x, y, font_size, t_color, font)
		x, y, w, h = self.text.get_rekt()
		self.resp = resp
		self.Rect = Rect_Button(scr, r_color, x, y, w, h, resp)
		self.scr = scr
		self.r_color = r_color
		return

	def blit(self):
		self.Rect.blit()
		self.text.blit()
		return

	def update_text(self, new_text):
		self.text.update_text(new_text)
		self.Rect.rect = self.text.get_rekt()
		return
	pass
