import pygame
from Tools.PictureUploads import Loadify, TransformImage
from Menu.SettingSaves import GetRes

pygame.init()
width = int(GetRes()[0])
height = int(GetRes()[1])
mode = (GetRes()[2])
if mode == "fullscreen":
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode([width, height])
""" Run Game intro """

