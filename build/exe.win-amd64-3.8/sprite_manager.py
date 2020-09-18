import pygame
import os
from colors import WHITE

def get_sprites():
	out = {}
	files = os.listdir("sprites")
	names = [file.split(".")[0] for file in files]
	files = [f"sprites\\{file}" for file in files]
	ratio_dividers = {"coins": 24, "dm_ex": 4, 'dm_paper': 3,
	'dollars': 20,'handle_active': 3,'handle_idle': 3,
	'letter': 12,'machine_base': 2,'ms_ex': 4,'ms_paper': 3,
	'buy_placeholder': 5}
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
# s = get_sprites()
# scr = pygame.display.set_mode((700, 700))
# scr.fill(WHITE)
# scr.blit(s["buy_placeholder"], (350, 350))
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			exit()
# 	pygame.display.update()