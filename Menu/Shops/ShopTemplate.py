import pygame
from Tools.FontRender import RenderFont

class ShopTemplate(object):
    def __init__(self, screen, tier, parts_tiers):
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.tier = tier
        self.button_list = []
        self.parts_tier = parts_tiers
        self.part_names =  ["engine", "supercharger", "gearbox", "suspension", "aerodynamics",
                              "chassis", "tyres", "fuel", "exhaust", "clutch"]
        self.part_names_fonts = []

    def DrawButtons(self):
        for num in range(10):
            self.button_list.append(pygame.Rect((self.screen_width/2 - 75), self.screen_height/10 * num, 150, 100))

    def RenderFonts(self):
        for parts in self.part_names:
            self.part_names_fonts.append(RenderFont(parts, 30, self.BLACK))


    def DisplayWindow(self):
        """Undergoes any initialisations then displays the window"""
        on_shop = True
        self.DrawButtons()
        self.RenderFonts()
        while on_shop:
            self.screen.fill(self.LBLUE)

            mx, my = pygame.mouse.get_pos()
            for buttons in self.button_list:
                pygame.draw.rect(self.screen, self.RED, buttons)
                if self.parts_tier[self.button_list.index(buttons)] == 1:
                    pygame.draw.rect(self.screen, self.BLUE, buttons)
                if buttons.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREEN, buttons)

            for font in self.part_names_fonts:
                self.screen.blit(font, [self.screen_width/2 - 75, self.part_names_fonts.index(font) * self.screen_height/10])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        on_shop = False
            pygame.display.update()







