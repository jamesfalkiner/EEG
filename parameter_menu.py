import pygame
from Tools.FontRender import RenderFont, RenderFontBold

#Input parameters which are saved in an external file.
class ParameterMenu(object):
    def __init__(self, screen):
        self.OnParameterMenu = True
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.LBLUE = (0, 255, 0)
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        self.bar_list = []
        self.slider_list = []
        self.boatNumber = 2

        self.icebergNumber = 50
        self.height_divider = 8
        self.slider_width = self.width / 2
        self.slider_height = 10
        self.slider_radius = 10
        self.bar_limit = []
        self.slider_left_coord = (self.width / 2) - (self.slider_width / 2)
        self.slider_right_coord = (self.width / 2) + (self.slider_width / 2)
        self.ships_font = RenderFont("No. of Ships", 25, self.BLACK)
        self.iceberg_font = RenderFont( "No. of Icebergs", 25, self.BLACK)

    def SliderMove(self, new_x, slider_number):

        if slider_number == 0:
            self.slider_list[0] = pygame.Rect(int(new_x) - 10, int(((self.height / self.height_divider) * 2)), 20, 20)
        if slider_number == 1:
            self.slider_list[1] = pygame.Rect(int(new_x) - 10, int(((self.height / self.height_divider) * 4)), 20, 20)

    def Slider_Calc(self):

        centre = (self.width / 2)

        return centre

    def saveValues(self, numBoat, numBerg):
        parameter_file = open("Menu/parameter_menu.txt", "w")
        parameter_file.write(str(numBoat) + "\n" + str(numBerg))
        parameter_file.close()
        print("called")


    def changeBoatNum(self, num):
        rendered_font = RenderFont(self.font1, str(num), self.BLACK)
        self.screen.blit(rendered_font, [1500,250])
        pygame.display.update()

    def changeIcebergNum(self, num):
        rendered_font = RenderFont(self.font1, str(num), self.BLACK)
        self.screen.blit(rendered_font, [1500, 550])
        pygame.display.update()

    def NewValue(self, new_x, slider):
        percentage = ((new_x - self.slider_left_coord) / (self.slider_right_coord - self.slider_left_coord))
        if slider == 0:
            self.boatNumber = int(4*percentage)
            if self.boatNumber == 0:
               self.boatNumber = 1
            self.changeNum(self.boatNumber,self.coords1)
            self.changeNum(self.icebergNumber,self.coords2)
            self.saveValues(self.boatNumber, self.icebergNumber)
        if slider == 1:
            self.icebergNumber = int(percentage * 100)
            self.changeNum(self.boatNumber,self.coords1)
            self.changeNum(self.icebergNumber,self.coords2)
            self.saveValues(self.boatNumber, self.icebergNumber)

    def Control(self, click):
        """Function that lets user adjust volume levels"""
        mx, my = pygame.mouse.get_pos()

        for bars in self.bar_list:
            pygame.draw.rect(self.screen, self.BLACK, bars)

        for sliders in self.slider_list:
            """Goes through the list of sliders"""
            pygame.draw.rect(self.screen, self.RED, sliders)
            if sliders.collidepoint(mx, my):
                if click:
                    if self.slider_list.index(sliders) == 0:
                        while click:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if self.bar_limit[0] > mouse_x:
                                mouse_x = self.bar_limit[0]
                            if self.bar_limit[1] < mouse_x:
                                mouse_x = self.bar_limit[1]
                            self.SliderMove(mouse_x, 0)
                            self.screen.fill(self.LBLUE)
                            for bars in self.bar_list:
                                pygame.draw.rect(self.screen, self.BLACK, bars)
                            for sliders in self.slider_list:
                                pygame.draw.rect(self.screen, self.RED, sliders)

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.NewValue(mouse_x, 0)
                                    click = False
                            pygame.display.update()

                    if self.slider_list.index(sliders) == 1:
                        while click:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if self.bar_limit[0] > mouse_x:
                                mouse_x = self.bar_limit[0]
                            if self.bar_limit[1] < mouse_x:
                                mouse_x = self.bar_limit[1]
                            self.SliderMove(mouse_x, 1)
                            self.screen.fill(self.LBLUE)
                            for bars in self.bar_list:
                                pygame.draw.rect(self.screen, self.BLACK, bars)
                            for sliders in self.slider_list:
                                pygame.draw.rect(self.screen, self.RED, sliders)

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.NewValue(mouse_x, 1)
                                    click = False
                            pygame.display.update()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.OnParameterMenu = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        return click

    def Bars(self):
        slider_height = self.slider_height
        slider_width = self.slider_width
        y_offset = slider_height / 2
        height_divider = self.height_divider
        self.bar_limit = [self.slider_left_coord, self.slider_right_coord]

        self.bar_list = [
            pygame.Rect(int(self.slider_left_coord), int(((self.height / height_divider) * 2) + y_offset), slider_width,
                        slider_height),
            pygame.Rect(int(self.slider_left_coord), int(((self.height / height_divider) * 4) + y_offset), slider_width,
                        slider_height)]


    def SlidersInit(self):
        """"Initiliases slider list"""
        self.slider_list = [
            pygame.Rect(int(self.Slider_Calc()), int(((self.height / self.height_divider) * 2)), 20, 20),
            pygame.Rect(int(self.Slider_Calc()), int(((self.height / self.height_divider) * 4)), 20, 20)]


    def DisplayWindow(self):
        """Function that displays all parts for the slider screen"""
        self.Bars()
        self.SlidersInit()
        click = False
        self.screen.fill(self.LBLUE)
        self.changeNum(self.icebergNumber)
        self.changeNum(self.boatNumber)
        while self.OnParameterMenu:
            click = self.Control(click)
            self.screen.blit(self.ships_font, [880, 200])
            self.screen.blit(self.iceberg_font, [850, 480])
            pygame.display.update()
            pygame.display.flip()
