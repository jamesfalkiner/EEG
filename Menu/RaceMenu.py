import pygame
from Tools.FontRender import RenderFont
from MainV2 import RunLevel
from Start import Start


class RaceMenu(object):
    def __init__(self, screen):
        #############
        # Colours
        #############
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.GREY = (180, 180, 180)
        #############
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.temp_font = RenderFont("Tier 1", 20, self.BLACK)

    def DrawButtons(self):
        """Creates three buttons"""
        for num in range(3):
            self.button_list.append(pygame.Rect(((self.screen_width - 200)/3) * num + 200, (self.screen_height - 200)/2, 400, 200))

    def DisplayWindow(self):
        self.DrawButtons()
        click = False
        while self.on_race_menu:
            mx, my = pygame.mouse.get_pos()
            self.screen.fill(self.GREY)
            for buttons in self.button_list:
                pygame.draw.rect(self.screen, self.GREY, buttons)
                if buttons.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREY, buttons)
                    if click:
                        if self.button_list.index(buttons) == 0:
                            TierMenu(self.screen).DisplayWindow()
            click = False
            self.screen.blit(self.temp_font, (200, (self.screen_height - 200)/2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()


class TierMenu(object):
    def __init__(self, screen):
        ###########
        # Colours
        ###########
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        ###########
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.on_tier_menu = True
        self.temp_font1 = RenderFont("Win0", 20, self.BLACK)
        self.temp_font2 = RenderFont("Win1", 20, self.BLACK)
        self.button_list = []

    def DrawButtons(self):
        for num in range(10):
            self.button_list.append(pygame.Rect(((self.screen_width - 100)/10) * num + 100, (self.screen_height - 50)/2,
                                                                                                            100, 50))

    def DisplayWindow(self):
        self.DrawButtons()
        click = False
        while self.on_tier_menu:
            mx, my = pygame.mouse.get_pos()
            self.screen.fill(self.LBLUE)
            for buttons in self.button_list:
                pygame.draw.rect(self.screen, self.RED, buttons)
                if buttons.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREEN, buttons)
                    if click:

                        if self.button_list.index(buttons) == 0:
                            RunLevel(self.screen, 1, 1).RunLevel()
                        if self.button_list.index(buttons) == 1:
                            RunLevel(self.screen, 1, 2).RunLevel()
                        if self.button_list.index(buttons) == 2:
                            Start(self.screen).Start()

            click = False
            self.screen.blit(self.temp_font1, (100, (self.screen_height - 50) / 2))
            self.screen.blit(self.temp_font2, (300, (self.screen_height - 50) / 2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_tier_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

class Tier1(TierMenu):
    pass






