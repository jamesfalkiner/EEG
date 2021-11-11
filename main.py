from Menu.SettingsMenu import SettingsMenu
from Tools.FontRender import RenderFont, RenderFontBold
from Tools.PictureUploads import Loadify, TransformImage
from Menu.UpgradesMenu import UpgradesMenu
from Menu.PartsMenu import PartsMenu
from Music.Music import *
from TestOne import TestOneMenu
from TestTwo import TestTwoMenu
from Menu.Staff.Staff import StaffMenu



"""Main Menu"""
def MainMenu(screen):
    background_image = Loadify("Images/Backgrounds/nebula.png")
    background_image = TransformImage(background_image, Initialise.width, Initialise.height)

    MainMenuMusic()
    LBLUE = (0, 204, 204)
    WHITE = (255,255,255)

    font1 = RenderFontBold("Test One", 100, WHITE)
    font2 = RenderFontBold("Test Two", 100, WHITE)
    #font3 = RenderFont("Upgrades [3]", 20, BLACK)
    #font4 = RenderFont("Shop [4]", 20, BLACK)
    #font5 = RenderFont("Staff [5]", 20, BLACK)

    button_list = []
    button_list.append(pygame.Rect(700, 250, 500, 250))
    button_list.append(pygame.Rect(700, 550, 500, 250))


    on_main_menu = True
    click = False
    while on_main_menu:

        screen.blit(background_image, [0, 0])

        mx, my = pygame.mouse.get_pos()
        for button in button_list:
            pygame.draw.rect(screen, (180, 180, 180), button,10)
            if button.collidepoint(mx, my):
                pygame.draw.rect(screen, (50, 200, 100), button,6)
                if click:
                    show =True
                    if button_list.index(button) == 0:
                        TestOneMenu(screen).DisplayWindow()

                    if button_list.index(button) == 1:
                        TestTwoMenu(screen).DisplayWindow()


        screen.blit(font1, [740, 330])
        screen.blit(font2, [740, 630])
        #screen.blit(font3, [950, 450])
        #screen.blit(font4, [950, 600])
        #screen.blit(font5, [950, 750])

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Game quits if user presses escape on the main screen
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


MainMenu(Initialise.screen)
