import pygame
import os
from colors import *
# from complex import new_hud

def get_sprites():
	out = {}
	files = os.listdir("sprites")
	names = [file.split(".")[0] for file in files]
	files = [f"sprites\\{file}" for file in files]
	ratio_dividers = {"coins": 24, "dm_ex": 4, 'dm_paper': 3,
	'dollars': 20,'handle_active': 3,'handle_idle': 3,
	'letter': 12,'machine_base': 2,'ms_ex': 4,'ms_paper': 3,
	'buy_placeholder': 5, 'money_bg': 7, 'hud_pulldown': 2}
	# single best for loop ever
	for name, file in zip(names, files):
		if name in ratio_dividers:
			img = pygame.image.load(file)
			rect = img.get_rect()
			_, _, w, h = rect
			ratio = w / h
			ratio = ratio / ratio_dividers[name]
			out[name] = pygame.transform.scale(img, (int(w * ratio), int(h * ratio)))
	return out


# testing ground for new sprites
# pygame.init()
# s = get_sprites()
# scr = pygame.display.set_mode((1280, 720))
# hud = new_hud(scr, s)
# m = 0
# while True:
# 	scr.fill(BLACK)
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			exit()
# 	m += 754654865
# 	hud.blit(m)
# 	pygame.display.update()