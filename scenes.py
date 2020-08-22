from objects import *
from complex import *
from group import Group
import pygame
from colors import *

class Scenes:
	def get_main_menu(scr, resp):
		fonts = pygame.font.get_fonts()
		objs = Group()
		objs.append(Text(scr, "Exoptable Money", 350, 75, 70, WHITE))
		objs.append(Rect(scr, BLACK, 400, 420, 300, 300))
		objs.append(Rect(scr, BLACK, 700, 500, 200, 50))
		objs.append(Rect(scr, BLACK, 900, 500, 50, 200))
		objs.append(Text_Button(scr, "Begin Thy Journey", 350, 250, 50, WHITE, BLACK, resp=resp))
		return objs