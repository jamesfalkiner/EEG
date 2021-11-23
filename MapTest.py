import pygame
from Tools.FontRender import RenderFont
from Tools.PictureUploads import Loadify, TransformImage
import Initialise



class MapTest(object):
    def __init__(self, screen):
        #############
        # Colours
        #############
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.RED = (180, 30, 30)
        self.GREEN = (30, 180, 30)
        self.GREY = (150, 150, 150)
        self.LGREY = (200, 200, 200)
        self.WHITE = (252, 252, 252)
        self.background_image = Loadify("Images/Backgrounds/map.jpg")
        self.background_image = TransformImage(self.background_image, Initialise.width, Initialise.height)
        self.tank1=Loadify("Images/models/tank1.png")
        self.tank1 = TransformImage(self.tank1, 325, 325)
        self.tank2=Loadify("Images/models/tank2.png")
        self.tank2 = TransformImage(self.tank2, 325, 325)
        self.tank3=Loadify("Images/models/tank3.png")
        self.tank3 = TransformImage(self.tank3, 400, 400)
        self.tank4=Loadify("Images/models/tank4.png")
        self.tank4 = TransformImage(self.tank4, 400, 400)
        #############
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.templeft = RenderFont("β", 300, self.WHITE)
        self.tempright = RenderFont("α", 300, self.WHITE)


    def DisplayWindow(self):
        self.screen.blit(self.background_image, [0, 0])

        click = False
        current_time = pygame.time.get_ticks()
        # 100
        # how long to show or hide
        delay_alpha = 95  # 500ms = 0.5s
        delay_beta = 150  # 500ms = 0.5s

        # time of next change
        change_time_alpha = current_time + delay_alpha
        change_time_beta = current_time + delay_beta
        # 200
        show_alpha = True
        show_beta = True
        while self.on_race_menu:
            self.screen.blit(self.tank1, [350, 200])
            self.screen.blit(self.tank3, [1300, 500])
            alpha_detected = False
            beta_detected = True
            mx, my = pygame.mouse.get_pos()


                # if buttons.collidepoint(mx, my):
                #     pygame.draw.rect(self.screen, self.GREEN, buttons)
                #     if click:
                #         if self.button_list.index(buttons) == 0:
                #             TierMenu(self.screen).DisplayWindow()
            click = False
            # --- updates ---

            current_time = pygame.time.get_ticks()

            # is time to change ?
            if show_alpha:
                self.screen.blit(self.tank2, [350, 200])

            if show_beta:
                self.screen.blit(self.tank4, [1300, 500])

            if current_time >= change_time_alpha:
                # time of next change
                change_time_alpha = current_time + delay_alpha
                show_alpha = not show_alpha

            if current_time >= change_time_beta:
                # time of next change
                change_time_beta = current_time + delay_beta
                show_beta = not show_beta




            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False
                    if event.key == pygame.K_RIGHT:
                        print("right")
                        alpha_detected = 1
                        self.button_list[3].move_ip(20,0)
                    if event.key == pygame.K_LEFT:
                        beta_detected = 1
                        print("left")
                        self.button_list[3].move_ip(-20, 0)


            pygame.display.update()

