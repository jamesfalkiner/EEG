import pygame
from Tools.FontRender import RenderFont
from Menu.Shops.ShopTemplate import ShopTemplate
from Menu.Shops.Inventory import Inventory

class PartsMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.parts_tier_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.parts_tier_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.on_parts_menu = True
        self.upgrade_names = ["aerodynamics", "engine", "supercharger", "gearbox", "suspension",
                              "chassis", "tyres", "fuel", "exhaust", "clutch"]
        self.upgrade_names_fonts = []
        self.button_list = []
        self.inventory_font = RenderFont("Inventory",  50, (0, 0, 0))

    def RenderFonts(self):
        [self.upgrade_names_fonts.append(RenderFont(names, 25, (0, 0, 0))) for names in self.upgrade_names]

    def DisplayFonts(self):
        for font in self.upgrade_names_fonts:
            self.screen.blit(font, [400, ((self.upgrade_names_fonts.index(font) * 100) + 100)])

    def DrawButtons(self):
        [self.button_list.append(pygame.Rect(self.screen_width/2, (self.screen_height-50)/10 * num, 50, 50)) for num in range(10)]
        self.button_list.append(pygame.Rect(1500, 50, 300, 200))

    def ReadCarStats(self):
        pass

    def ShowWindow(self):
        self.RenderFonts()
        self.ReadCarStats()
        self.DrawButtons()
        click = False
        while self.on_parts_menu:
            self.screen.fill((0, 204, 204))
            mx, my = pygame.mouse.get_pos()
            for buttons in self.button_list:
                pygame.draw.rect(self.screen, self.RED, buttons)
                if buttons.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREEN, buttons)
                    if click:
                        if self.button_list.index(buttons) == 0:
                            ShopTemplate(self.screen, 2, self.parts_tier_2).DisplayWindow()
                        if self.button_list.index(buttons) == 10:
                            Inventory(self.screen).DisplayWindow()
                        click = False

            self.screen.blit(self.inventory_font, [1500, 50])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_parts_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()



