from objects import Text, Text_Button
from colors import *


class Setting:
	def __init__(self, scr, setting, value_range, value, x, y):
		self.current_value = value
		self.setting = setting
		self.setting_value = Text_Button(scr, f"{self.setting}: {self.current_value}", x, y, 50, WHITE, BLACK, resp=self.update_text)
		self.range = value_range
		self.current_index = value_range.index(value)
		return

	def update_text(self):
		self.current_index = (self.current_index + 1) % len(self.range)
		self.current_value = self.range[self.current_index]
		self.setting_value.update_text(f"{self.setting}: {self.current_value}")
		return

	def blit(self):
		self.setting_value.blit()
		return

	def get_status(self):
		return self.setting, self.current_value
	pass