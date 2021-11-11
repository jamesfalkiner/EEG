import pygame
from Tools.FontRender import RenderFont
from Music.Music import ChangeMasterLevel, ChangeMusicLevel, ChangeSoundLevel
from Menu.SettingSaves import SaveAud, SaveRes, GetAud, GetRes


def SettingsMenu(screen):
    """The General Settings Menu"""
    on_settings_menu = True
    LBLUE = (0, 204, 204)
    BLACK = (0, 0, 0)
    video_font = RenderFont("Video Settings[1]", 20, BLACK)  # Render the fonts
    audio_font = RenderFont("Audio Settings[2]", 20, BLACK)

    click = False
    while on_settings_menu:

        screen.fill(LBLUE)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(1920 / 2, 540, 200, 50)
        button_2 = pygame.Rect(1920 / 2, 800, 200, 50)

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        screen.blit(video_font, [1920 / 2, 540])
        screen.blit(audio_font, [1920 / 2, 800])

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 255, 0), button_1)
            screen.blit(video_font, [1920 / 2, 540])
            if click:
                ResolutionMenu(screen, LBLUE).DisplayWindow() # Displays the resolution menu

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 255, 0), button_2)
            screen.blit(audio_font, [1920 / 2, 800])
            if click:
                AudioMenu(screen, LBLUE).DisplayWindow() # Displays the resolution menu

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_settings_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


class ResolutionMenu(object):
    """The Settings Menu for resolution"""
    def __init__(self, screen, LBLUE):
        self.OnResolutionMenu = True
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.screen = screen
        self.LBLUE = LBLUE
        self.width, self.height = pygame.display.get_surface().get_size()
        self.fullscreen_font = RenderFont("Fullscreen[1]", 20, self.BLACK)
        self.windowed_font = RenderFont("Windowed[2]", 20, self.BLACK)
        self.resolutions = ["1920x1080[3]", "1600x900[4]", "1366X768[5]", "1280x720[6]", "1152X648[7]", "1024x576[8]"]
        self.windowed = False
        self.rendered_resolution_fonts = []
        self.button_list = []

    def RenderFont(self):
        for Resolution in self.resolutions:
            self.rendered_resolution_fonts.append(RenderFont(Resolution, 20, self.BLACK))

    def DisplayFonts(self):
        counter = 0
        for x, y, width, height in self.button_list:
            if counter <= 5:
                self.screen.blit(self.rendered_resolution_fonts[counter], [x, y])
                counter += 1
        self.screen.blit(self.fullscreen_font, [900, 350])
        self.screen.blit(self.windowed_font, [900, 650])

    def Control(self, click):
        """Function that lets user choose different resolutions and modes"""
        mx, my = pygame.mouse.get_pos()

        for buttons in self.button_list:
            pygame.draw.rect(self.screen, self.RED, buttons)
            if buttons.collidepoint(mx, my):
                pygame.draw.rect(self.screen, self.GREEN, buttons)
                if click:
                    if self.button_list.index(buttons) == 0:
                        self.ChangeResolution(1920, 1080)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 1:
                        self.ChangeResolution(1600, 900)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 2:
                        self.ChangeResolution(1366, 768)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 3:
                        self.ChangeResolution(1280, 720)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 4:
                        self.ChangeResolution(1152, 648)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 5:
                        self.ChangeResolution(1024, 576)
                        self.Buttons()
                    elif self.button_list.index(buttons) == 6:
                        pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
                        self.windowed = False
                        SaveRes(self.width, self.height, "fullscreen")
                    elif self.button_list.index(buttons) == 7:
                        pygame.display.set_mode([self.width, self.height])
                        self.windowed = True
                        SaveRes(self.width, self.height, "windowed")

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.OnResolutionMenu = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        return click

    def ChangeResolution(self, width, height):
        self.width = width
        self.height = height
        if self.windowed:
            pygame.display.set_mode([width, height])
            SaveRes(width, height, "windowed")
        else:
            pygame.display.set_mode([width, height], pygame.FULLSCREEN)
            SaveRes(width, height, "fullscreen")

    def DisplayWindow(self):
        self.RenderFont()
        print(self.rendered_resolution_fonts)
        self.Buttons()

        click = False
        while self.OnResolutionMenu:
            self.screen.fill(self.LBLUE)
            click = self.Control(click)
            self.DisplayFonts()
            pygame.display.update()

    def Buttons(self):
        width_divider = 6
        height_divider = 6
        x_offset = 100
        y_offset = 25

        self.button_list = [pygame.Rect(((self.width/width_divider)*2) - x_offset, ((self.height/height_divider)*2) - y_offset, 200, 50), pygame.Rect(((self.width/width_divider)*3) - x_offset, ((self.height/height_divider)*2) - y_offset, 200, 50),
                        pygame.Rect(((self.width/width_divider)*4) - x_offset, ((self.height/height_divider)*2) - y_offset, 200, 50), pygame.Rect(((self.width/width_divider)*2) - x_offset, ((self.height/height_divider)*3) - y_offset, 200, 50),
                        pygame.Rect(((self.width/width_divider)*3) - x_offset, ((self.height/height_divider)*3) - y_offset, 200, 50), pygame.Rect(((self.width/width_divider)*4) - x_offset, ((self.height/height_divider)*3) - y_offset, 200, 50),
                        pygame.Rect((self.width/2)-x_offset, ((self.height/height_divider)*4)-y_offset, 200, 50), pygame.Rect((self.width/2) - x_offset, ((self.height/height_divider)*5) - y_offset, 200, 50)]


class AudioMenu(object):
    def __init__(self, screen, LBLUE):
        self.OnAudioMenu = True
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.screen = screen
        self.LBLUE = LBLUE
        self.width, self.height = pygame.display.get_surface().get_size()
        self.bar_list = []
        self.slider_list = []
        self.master_level = float(GetAud()[0])
        self.music_level = float(GetAud()[1])
        self.sound_level = float(GetAud()[2])
        self.height_divider = 8
        self.slider_width = self.width/2
        self.slider_height = 10
        self.slider_radius = 10
        self.bar_limit = []
        self.slider_left_coord = (self.width / 2) - (self.slider_width / 2)
        self.slider_right_coord = (self.width/2) + (self.slider_width / 2)

    def Control(self, click):
        """Function that lets user adjust volume levels"""
        mx, my = pygame.mouse.get_pos()

        for bars in self.bar_list:
            pygame.draw.rect(self.screen, self.BLACK, bars)

        for sliders in self.slider_list:
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
                                    self.NewVolume(mouse_x, 0)
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
                                    self.NewVolume(mouse_x, 1)
                                    click = False
                            pygame.display.update()

                    if self.slider_list.index(sliders) == 2:
                        while click:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if self.bar_limit[0] > mouse_x:
                                mouse_x = self.bar_limit[0]
                            if self.bar_limit[1] < mouse_x:
                                mouse_x = self.bar_limit[1]
                            self.SliderMove(mouse_x, 2)
                            self.screen.fill(self.LBLUE)
                            for bars in self.bar_list:
                                pygame.draw.rect(self.screen, self.BLACK, bars)
                            for sliders in self.slider_list:
                                pygame.draw.rect(self.screen, self.RED, sliders)

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.NewVolume(mouse_x, 2)
                                    click = False
                            pygame.display.update()


        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.OnAudioMenu = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        return click

    def DisplayWindow(self):
        self.Bars()
        self.SlidersInit()
        click = False
        while self.OnAudioMenu:
            self.screen.fill(self.LBLUE)
            click = self.Control(click)
            pygame.display.update()

    def Bars(self):
        slider_height = self.slider_height
        slider_width = self.slider_width
        y_offset = slider_height/2
        height_divider = self.height_divider
        self.bar_limit = [self.slider_left_coord, self.slider_right_coord]



        self.bar_list = [pygame.Rect(int(self.slider_left_coord), int(((self.height/height_divider)*2)+y_offset), slider_width, slider_height),
                         pygame.Rect(int(self.slider_left_coord), int(((self.height/height_divider)*4)+y_offset), slider_width, slider_height),
                         pygame.Rect(int(self.slider_left_coord), int(((self.height/height_divider)*6)+y_offset), slider_width, slider_height)]

    def SlidersInit(self):

        self.slider_list = [pygame.Rect(int(self.Slider_Calc()[0]), int(((self.height/self.height_divider)*2)), 20, 20),
                            pygame.Rect(int(self.Slider_Calc()[1]), int(((self.height/self.height_divider)*4)), 20, 20),
                            pygame.Rect(int(self.Slider_Calc()[2]), int(((self.height/self.height_divider)*6)), 20, 20)]

    def SliderMove(self, new_x, slider_number):

        if slider_number == 0:
            self.slider_list[0] = pygame.Rect(int(new_x)-10, int(((self.height/self.height_divider)*2)), 20, 20)
        if slider_number == 1:
            self.slider_list[1] = pygame.Rect(int(new_x)-10, int(((self.height/self.height_divider)*4)), 20, 20)
        if slider_number == 2:
            self.slider_list[2] = pygame.Rect(int(new_x)-10, int(((self.height/self.height_divider)*6)), 20, 20)

    def Slider_Calc(self):
        master_inc = self.master_level*self.slider_width
        music_inc = self.music_level*self.slider_width
        sound_inc = self.sound_level*self.slider_width

        master_pos = ((self.width/2)-(self.slider_width/2)) + master_inc
        music_pos = ((self.width/2)-(self.slider_width/2)) + music_inc
        sound_pos = ((self.width / 2) - (self.slider_width/2)) + sound_inc

        return master_pos, music_pos, sound_pos

    def NewVolume(self, new_x, slider):
        percentage_bar = (new_x-self.slider_left_coord)/(self.slider_right_coord-self.slider_left_coord)
        if slider == 0:
            self.master_level = percentage_bar
            ChangeMasterLevel(self.master_level, self.music_level, self.sound_level)
        if slider == 1:
            self.music_level = percentage_bar
            ChangeMusicLevel(self.music_level)
        if slider == 2:
            self.sound_level = percentage_bar
            ChangeSoundLevel(self.sound_level)
        SaveAud(self.master_level, self.music_level, self.sound_level)