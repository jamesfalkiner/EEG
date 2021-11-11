import pygame
from Menu.Staff.DriverMenu import DriverMenu
from Menu.Staff.CrewMenu import CrewMenu
from Menu.Staff.MechanicMenu import MechanicMenu
from Tools.FontRender import RenderFont, CreateNumber


class StaffMenu(object):
    def __init__(self, screen):
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        self.screen = screen
        self.button_list = []
        self.button_kwargs = []
        driver_butt = RenderFont("Drivers", 20, self.BLACK)
        crew_butt = RenderFont("Crew", 20, self.BLACK)
        mech_butt = RenderFont("Mechanics", 20, self.BLACK)
        self.button_label_list = [driver_butt, crew_butt, mech_butt]

    def DrawButtons(self):
        for num in range(3):
            self.button_list.append(pygame.Rect(self.screen_width/2, self.screen_height/4 * (num+1), 50, 50))
            self.button_kwargs.append([self.screen_width/1.99, self.screen_height/3.95 * (num+1)])

    def DisplayWindow(self):
        running = True
        self.DrawButtons()
        while running:

            click = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            self.screen.fill(self.LBLUE)
            mx, my = pygame.mouse.get_pos()
            for button in self.button_list:
                pygame.draw.rect(self.screen, self.RED, button)
                if button.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, self.GREEN, button)
                    if click:
                        if self.button_list.index(button) == 0:
                            DriverMenu(self.screen).DisplayWindow()
                        if self.button_list.index(button) == 1:
                            CrewMenu(self.screen).DisplayWindow()
                        if self.button_list.index(button) == 2:
                            MechanicMenu(self.screen).DisplayWindow()
            for i in range(len(self.button_label_list)):
                self.screen.blit(self.button_label_list[i], self.button_kwargs[i])





            pygame.display.update()

