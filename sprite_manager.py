import pygame
import os
from colors import *
from complex import new_hud
from time import time

def get_sprites():
	out = {}
	files = os.listdir("sprites")
	names = [file.split(".")[0] for file in files]
	files = [f"sprites\\{file}" for file in files]
	ratio_dividers = {"coins": 24, "dm_ex": 4, 'dm_paper': 3,
	'dollars': 20,'handle_active': 3,'handle_idle': 3,
	'letter': 12,'machine_base': 2,'ms_ex': 4,'ms_paper': 3,
	'buy_placeholder': 5, 'money_bg': 7, 'hud_pulldown': 2, 'buy_bg': 1, 'full_screen': 4,
	'save': 4, 'load': 7}
	# single best for loop ever
	for name, file in zip(names, files):
		if name in ratio_dividers:
			img = pygame.image.load(file)
			rect = img.get_rect()
			_, _, w, h = rect
			ratio = w / h
			ratio = ratio / ratio_dividers[name]
			out[name] = pygame.transform.scale(img, (round(w * ratio), round(h * ratio)))
	return out