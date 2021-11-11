import pygame


class DriverMenu(object):
    def __init__(self, screen):
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        self.screen = screen
        self.button_list = []
    def DrawButtons(self):
        for num in range(2):
            self.button_list.append(pygame.Rect(self.screen_width / 2, self.screen_height / 4 * (num + 1), 50, 50))

    def DisplayWindow(self):
        running = True
        self.DrawButtons()
        while running:
            self.screen.fill(self.LBLUE)
            mx, my = pygame.mouse.get_pos()
            for button in self.button_list:
                pygame.draw.rect(self.screen, self.RED, button)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
