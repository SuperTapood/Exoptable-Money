from objects import Text_Button, Text, Rect
from colors import *

class Letter_Placeholder:
	def blit(self):
		pass


class Letter:
	def __init__(self, scr, key):
		self.key = key
		self.small = True
		self.button = Text_Button(scr, "NEW LETTER", 1050, 650, 30, BLACK, WHITE, resp=self.click)
		self.text1 = Text(scr, "M.S.", 600, 600, 50, BLACK)
		self.letter_rect = Rect(scr, WHITE, 100, 100, 1000, 600)
		# will later include a little animation
		self.button_blit = self.button.blit
		return

	def click(self):
		self.small = False
		return

	def letter_blit(self):
		## TODO: add a little climb animation ##
		self.letter_rect.blit()
		self.text1.blit()
		return

	def blit(self):
		if self.small:
			self.button_blit()
		else:
			self.letter_blit()
		return


class Letters:
	def __init__(self, scr, dic):
		self.letter_dict = {}
		for key in dic:
			self.letter_dict[key] = Letter(scr, key)
		return

	def __getitem__(self, key):
		return self.letter_dict[key]