import pygame
from Tools.FontRender import RenderFont


class Inventory(object):
    def __init__(self, screen):
        # colours #
        self.LBLUE = (0, 204, 204)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        #############
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.screen = screen
        self.button_list = []
        self.on_inventory = True
        self.title = RenderFont("Inventory", 30, self.BLACK)
        self.upgrade_names = ["engine", "supercharger", "gearbox", "suspension", "aerodynamics",
                              "chassis", "tyres", "fuel", "exhaust", "clutch"]
        self.upgrade_names_fonts = [RenderFont(n, 30, self.BLACK) for n in self.upgrade_names]
        self.tier_1_parts = []
        self.tier_2_parts = []

    def DrawButtons(self):
        for num in range(10):
            self.button_list.append(pygame.Rect((self.screen_width/10 * num), self.screen_height/2, 50, 50))

    def RenderFontList(self, part_name):
        """Creates a font list that changes depending on what upgrades the user has"""
        font_list = []
        for number in range(10):
            font_list.append(RenderFont(part_name + " tier " + str(number + 1) + " LOCKED", 30, self.BLACK))
        font_list[0] = (RenderFont(part_name + " tier 1 UNLOCKED", 30, self.BLACK))
        if self.tier_2_parts[self.upgrade_names.index(part_name)] == 1:
            font_list[1] = (RenderFont(part_name + " tier 2 UNLOCKED", 30, self.BLACK))
        return font_list

    def PartDisplayTemplate(self, part_name):
        """Template for each part in the inventory"""
        running = True
        font_list = self.RenderFontList(part_name)
        while running:
            self.RenderFontList(part_name)
            self.screen.fill(self.LBLUE)
            for fonts in font_list:
                self.screen.blit(fonts, [self.screen_width / 5, self.screen_height / 10 * font_list.index(fonts)])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

    def DisplayWindow(self):
        self.DrawButtons()
        click = False
        while self.on_inventory:
            self.screen.fill(self.LBLUE)
            self.screen.blit(self.title, [self.screen_width/2, 50])
            mx, my = pygame.mouse.get_pos()
            for button in self.button_list:
                pygame.draw.rect(self.screen, self.RED, button)
                if button.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREEN, button)
                    if click:
                        if self.button_list.index(button) == 0:
                            self.PartDisplayTemplate("engine")
                        if self.button_list.index(button) == 1:
                            self.PartDisplayTemplate("supercharger")
                        if self.button_list.index(button) == 2:
                            self.PartDisplayTemplate("gearbox")
                        if self.button_list.index(button) == 3:
                            self.PartDisplayTemplate("suspension")
                        click = False
            for font in self.upgrade_names_fonts:
                self.screen.blit(font, [self.screen_width/10 * self.upgrade_names_fonts.index(font), self.screen_height/2])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_inventory = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
