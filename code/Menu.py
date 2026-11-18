#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, C_BLACK, MENU_OPTION, C_WHITE, C_ORANGE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40, "Danger Zone", C_BLACK, ((WIN_WIDTH / 2), 70))
            self.menu_text(15, "How to play", C_BLACK, ((WIN_WIDTH / 2), 200))
            self.menu_text(15, "UP Arrow - Move Up     DOWN Arrow - Move Down ", C_BLACK, ((WIN_WIDTH / 2), 230))
            self.menu_text(15, "LEFT Arrow - Move Left     RIGHT Arrow - Move Right", C_BLACK, ((WIN_WIDTH / 2), 250))
            self.menu_text(15, "CTRL - Shoot", C_BLACK, ((WIN_WIDTH / 2), 270))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 120 + 30 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
