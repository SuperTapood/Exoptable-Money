from pygame.draw import circle, rect, line, polygon
from pygame.mouse import get_pressed, get_pos
from time import time
import pygame
from math import ceil
from functools import lru_cache

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

    def move_y(self, factor):
        x, y, w, h = self.rect
        y = y + factor
        self.rect = x, y, w, h
        return

    pass

class Button:
    last_click = time()

    def check_click(self):
        # check if the button is being click
        mouse = get_pos()
        x, y, w, h = self.rect
        if x + w > mouse[0] > x:
            if y + h > mouse[1] > y:
                if get_pressed()[0] == 1:
                    return True
        return False

    def blit(self):
        # implement click delay to prevent instant clicks
        if time() - self.last_click >= self.delay_time:
            if self.check_click():
                self.last_click = time()
                self.resp()
        return

    def is_clicked(self):
        if self.check_click():
            if time() - self.last_click >= self.delay_time:
                return True
        return False
    pass

class Rect_Button(Button):
    def __init__(self, scr, color, x, y, w, h, resp=lambda: None, width=0, delay_time=0.3):
        self.scr = scr
        self.butt = Rect(scr, color, x, y, w, h, width)
        self.resp = resp
        self.rect = x, y, w, h
        self.delay_time = delay_time
        return

    def move_y(self, factor):
        self.butt.move_y(factor)
        x, y, w, h = self.rect
        y = y + factor
        self.rect = x, y, w, h
        return

    def blit(self):
        self.butt.blit()
        super().blit()
        return

    def get_rekt(self):
        return self.rect

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

    pass

class Rect_Text:
    def __init__(self, scr, txt, x, y, font_size, t_color, r_color, scale=1.1):
        text = Text(scr, txt, x, y, font_size, t_color)
        x, y, w, h = text.get_rekt()
        self.text = Text(scr, txt, x + (w * (scale - 1)) / 2, y + (h * (scale - 1)) / 2, font_size, t_color)
        self.scaled_text = Text(scr, txt, x, y, ceil(font_size * scale), t_color)
        x, y, w, h = self.scaled_text.get_rekt()
        self.scr = scr
        self.r_color = r_color
        self.rect = Rect(scr, r_color, x, y, w, h)
        self.scale = scale
        return

    def blit(self):
        self.rect.blit()
        self.text.blit()
        return

    def update_text(self, new):
        self.scaled_text.update_text(new)
        x, y, w, h = self.scaled_text.get_rekt()
        self.text.update_text(new)
        self.text.x = x + (w * (self.scale - 1)) / 2
        self.text.y = y + (h * (self.scale - 0.9)) / 2
        self.rect = Rect(self.scr, self.r_color, x, y, w, h)
        return

    pass

class Text_Button:
    def __init__(self, scr, txt, x, y, font_size, t_color, r_color, font="freesansbold.ttf", resp=lambda: None, scale=1.1):
        text = Text(scr, txt, x, y, font_size, t_color, font)
        x, y, w, h = text.get_rekt()
        self.text = Text(scr, txt, x + (w * (scale - 1)) / 2, y + (h * (scale - 1)) / 2, font_size, t_color, font)
        self.scaled_text = Text(scr, txt, x, y, ceil(font_size * scale), t_color, font)
        x, y, w, h = self.scaled_text.get_rekt()
        self.resp = resp
        self.Rect = Rect_Button(scr, r_color, x, y, w, h, resp)
        self.scr = scr
        self.r_color = r_color
        self.scale = scale
        return

    def blit(self):
        self.Rect.blit()
        self.text.blit()
        return

    def update_text(self, new):
        self.scaled_text.update_text(new)
        x, y, w, h = self.scaled_text.get_rekt()
        self.text.update_text(new)
        self.text.x = x + (w * (self.scale - 1)) / 2
        self.text.y = y + (h * (self.scale - 0.9)) / 2
        self.rect = Rect(self.scr, self.r_color, x, y, w, h)
        return

    pass

class Image:
    def __init__(self, scr, img, x, y):
        self.scr = scr
        self.img = img
        self.og = img
        self.x = x
        self.y = y
        # constant
        self.angle = 90
        return

    def blit(self):
        self.scr.blit(self.img, (self.x, self.y))
        return

    def get_rekt(self):
        _, _, w, h = self.img.get_rect()
        return self.x, self.y, w, h

    def rotate(self, angle):
        self.img, self.rect = self.rot_center(self.og, self.angle)
        return

    def rotate_up(self, factor):
        self.angle += factor
        self.rotate(self.angle)
        return

    def rotate_down(self, factor):
        self.rotate_up(-factor)
        return

    def rot_center(self, image, angle):
        center = image.get_rect().center
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = center)
        return rotated_image, new_rect

    def move_y(self, factor):
        self.y += factor
        return
    pass

class Image_Button(Button):
    def __init__(self, scr, img, x, y, resp, delay_time=0.3):
        self.img = Image(scr, img, x, y)
        self.rect = self.img.get_rekt()
        self.delay_time = delay_time
        self.resp = resp
        self.rotate_up = self.img.rotate_up
        self.rotate_down = self.img.rotate_down
        return

    def blit(self):
        self.img.blit()
        super().blit()
        return
    pass

