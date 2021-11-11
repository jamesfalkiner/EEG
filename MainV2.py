import pygame
import time
import shelve
from CompareCars import PreStartCompareCars, AfterStartCompareCars
from Animation import CarAnimation


class RunLevel(object):
    def __init__(self, screen, tier, level):
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        self.user_car_stats = []
        self.level = level
        self.tier = tier
        self.opp_value = self.ReadOppCar()
        self.initial_user_value, self.maintenance_costs = PreStartCompareCars(self.tier)
        self.car_animation = CarAnimation(1, tier, self.width, self.height, self.screen)

    def ReadOppCar(self):
        file = shelve.open("Data/OpponentValues/opponent_values")
        value = file["tier" + str(self.tier)][self.level - 1]
        file.close()
        return value

    def RunLevel(self):
        running = True
        if self.level == 1:
            self.car_animation.Win0()
        if self.level == 2:
            self.car_animation.Win1()




