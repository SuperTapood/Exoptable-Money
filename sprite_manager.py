import pygame
import os
from colors import WHITE

def get_sprites():
	out = {}
	files = os.listdir("sprites")
	names = [file.split(".")[0] for file in files]
	files = [f"sprites\\{file}" for file in files]
	ratio_dividers = {"coin": 12, "dm_ex": 4, 'dm_paper': 3,
	'dollar': 12,'handle_active': 3,'handle_idle': 3,
	'letter': 12,'machine_base': 3,'ms_ex': 4,'ms_paper': 3}
	# single best for loop ever
	for name, file in zip(names, files):
		img = pygame.image.load(file)
		rect = img.get_rect()
		_, _, w, h = rect
		ratio = w / h
		ratio = ratio / ratio_dividers[name]
		out[name] = pygame.transform.scale(img, (int(w * ratio), int(h * ratio)))
	return out