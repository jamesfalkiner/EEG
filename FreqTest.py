import pygame
from Tools.FontRender import RenderFont



class FreqTest(object):
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
        #############
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.templeft = RenderFont("β", 300, self.WHITE)
        self.tempright = RenderFont("α", 300, self.WHITE)

    def DrawButtons(self):

        for num in range(2):
            self.button_list.append(pygame.Rect(((self.screen_width + 250)/2) * num+215, (self.screen_height - 100)/2, 400, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width + 250) / 3) , (self.screen_height / 2)-100, 800, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width) /2) , (self.screen_height / 2)-110, 5, 120))

    def DisplayWindow(self):
        self.DrawButtons()
        click = False
        current_time = pygame.time.get_ticks()
        # 100
        # how long to show or hide
        delay_alpha = 36   # 500ms = 0.5s
        delay_beta = 50  # 500ms = 0.5s

        # time of next change
        change_time_alpha = current_time + delay_alpha
        change_time_beta = current_time + delay_beta
        # 200
        show_alpha = True
        show_beta = True
        while self.on_race_menu:
            alpha_detected = False
            beta_detected = True
            mx, my = pygame.mouse.get_pos()
            self.screen.fill(self.BLACK)
            #pygame.draw.rect(self.screen, self.RED, self.button_list[2])
            pygame.draw.circle(self.screen, self.RED, self.button_list[0].center, 50)
            pygame.draw.circle(self.screen, self.RED, self.button_list[1].center, 50)

                # if buttons.collidepoint(mx, my):
                #     pygame.draw.rect(self.screen, self.GREEN, buttons)
                #     if click:
                #         if self.button_list.index(buttons) == 0:
                #             TierMenu(self.screen).DisplayWindow()
            click = False
            #self.screen.blit(self.templeft, [self.button_list[0].center[0]-75,self.button_list[0].center[1]-150])
            #self.screen.blit(self.tempright, [self.button_list[1].center[0]-80,self.button_list[2].center[1]-150])

            # --- updates ---

            current_time = pygame.time.get_ticks()

            # is time to change ?
            if show_alpha:
                pygame.draw.circle(self.screen, self.BLACK, self.button_list[1].center, 50)

            if show_beta:
                pygame.draw.circle(self.screen, self.BLACK, self.button_list[0].center, 50)

            if current_time >= change_time_alpha:
                # time of next change
                change_time_alpha = current_time + delay_alpha
                show_alpha = not show_alpha

            if current_time >= change_time_beta:
                # time of next change
                change_time_beta = current_time + delay_beta
                show_beta = not show_beta



            # --- draws centre line ---

            #pygame.draw.rect(self.screen, self.GREEN, self.button_list[3], 15)



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False

#  0                  if event.key == pygame.K_RIGHT:
#                        print("right")
#                        alpha_detected = 1
#                        self.button_list[3].move_ip(20,0)
#                    if event.key == pygame.K_LEFT:
#                        beta_detected = 1
#                        print("left")
#                        self.button_list[3].move_ip(-20, 0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        pressed = True
                        while pressed:
                            self.screen.fill(self.BLACK)
                            pygame.display.update()
                            for event1 in pygame.event.get():
                                if event1.type == pygame.KEYUP:
                                    pressed = False
            pygame.display.update()

