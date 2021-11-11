import pygame
import random
from Tools.PictureUploads import Loadify, LoadBackgroundImages, TransformImage
import time


class CarAnimation(object):
    def __init__(self, result, tier, width, height, screen, colour="blue"):
        self.screen = screen
        self.width = width
        self.height = height
        self.result = result
        self.dt = 1
        self.scale = self.width / 1920
        self.on_race = True
        self.last_time = time.time()
        self.clock = pygame.time.Clock()
        #########
        # Set the car sprites up for the race
        #########
        self.user_car_images = []
        self.opp_car_images = []
        for num in range(4):
            self.user_car_images.append(Loadify("Images/CarSprites/Tier" + str(tier) + "/usercarfr" + str(num + 1) + ".png"))
            self.opp_car_images.append(Loadify("Images/CarSprites/Tier" + str(tier) + "/" + colour + "carfr" + str(num + 1) + ".png"))
        self.current_user_image = self.user_car_images[0]
        self.current_opp_image = self.opp_car_images[0]
        ########
        # Set the original positions of the car
        ########
        self.user_x_position = self.width/5 * 3 - 101 * self.scale
        self.opp_x_position = self.width/5 * 3 - 101 * self.scale
        self.user_y_position = self.height/3 * 1.75
        self.opp_y_position = self.height/3 + 20 * self.scale
        #########
        self.restart_time = True
        self.start_time = time.time()
        ##########
        """Initialise the background"""
        ##########
        self.background_images = LoadBackgroundImages()
        for image in self.background_images:
            if image.get_size() != (self.width, self.height):
                TransformImage(image, self.width, self.height)
        self.image_locations = [0, self.width, self.width * 2]
        self.movement_speed = 2 * self.scale

    ##########
    # Image Movement Functions
    ##########
    def CarImageCycle(self):
        """Function that changes the picture of the car every x seconds"""
        if self.restart_time:
            """Restart the start_time"""
            self.start_time = time.time()
            self.restart_time = False
        current_image_num = self.user_car_images.index(self.current_user_image)
        if time.time() - self.start_time > 0.1:
            if current_image_num <= 2:
                self.current_user_image = self.user_car_images[current_image_num + 1]
                self.current_opp_image = self.opp_car_images[current_image_num + 1]
            elif current_image_num == 3:
                self.current_user_image = self.user_car_images[0]
                self.current_opp_image = self.opp_car_images[0]
            self.restart_time = True

    def MoveBackground(self):
        if self.image_locations[2] > 0:
            for image in self.image_locations:
                self.image_locations[self.image_locations.index(image)] = image - self.movement_speed * self.dt


    """Logic for different race results"""
    # Loss Animations
    def FalseStart(self):
        pass

    def TyreBurst(self):
        pass

    def Loss0(self):
        pass

    def Loss1(self):
        pass

    def Loss2(self):
        pass

    def Loss3(self):
        pass

    # Win animations
    def Win0(self):
        """Just win with good start"""
        race_start_time = time.time()
        random_value = 0.05 * random.randint(1, 10)
        print(random_value)
        self.movement_speed = 0.1
        while self.on_race:
            self.MoveBackground()
            if time.time() - race_start_time < 1.2:
                self.movement_speed = self.movement_speed * 1.02
                self.user_x_position -= 0.1 * self.dt * self.scale
                self.opp_x_position -= 0.1 * self.dt * self.scale
            if 1.2 <= time.time() - race_start_time < 2.5:
                self.movement_speed = self.movement_speed * 1.02
                self.user_x_position -= 0.5 * self.dt * self.scale
                self.opp_x_position -= 0.5 * self.dt * self.scale
            if 2.5 <= time.time() - race_start_time < 3.5:
                self.user_x_position -= (0.1 + random_value) * self.dt * self.scale
                self.opp_x_position -= (0.6 + random_value) * self.dt * self.scale
            if 3.5 <= time.time() - race_start_time < 4.5:
                self.user_x_position -= (0.1 + 0.5 * random_value) * self.dt * self.scale
                self.opp_x_position += 0.2 * self.dt * self.scale
            if 4.5 <= time.time() - race_start_time < 5.5:
                self.user_x_position += 0.1 * self.dt * self.scale
            if self.image_locations[2] <= 0:
                self.user_x_position += 16
                self.opp_x_position += 13
            if self.user_x_position > self.width + 30 and self.opp_x_position > self.width + 30:
                self.on_race = False
            self.RunAnimation()

    def Win1(self):
        """Comfortable win"""
        race_start_time = time.time()
        random_value = 0.05 * random.randint(1, 10)
        print(random_value)
        self.movement_speed = 0.1
        while self.on_race:
            self.MoveBackground()
            if time.time() - race_start_time < 1.2:
                self.movement_speed = self.movement_speed * 1.02
                self.user_x_position -= 0.1 * self.dt * self.scale
                self.opp_x_position -= 0.1 * self.dt * self.scale
            if 1.2 <= time.time() - race_start_time < 2.5:
                self.movement_speed = self.movement_speed * 1.02
                self.user_x_position -= 0.3 * self.dt * self.scale
                self.opp_x_position -= 0.5 * self.dt * self.scale
            if 2.5 <= time.time() - race_start_time < 3.5:
                self.user_x_position -= (0.1 + random_value) * self.dt * self.scale
                self.opp_x_position -= (1 + random_value) * self.dt * self.scale
            if 3.5 <= time.time() - race_start_time < 4.5:
                self.user_x_position -= (0.1 + 0.5 * random_value) * self.dt * self.scale
                self.opp_x_position += 0.1 * self.dt * self.scale
            if 4.5 <= time.time() - race_start_time < 5.5:
                self.user_x_position += 0.1 * self.dt * self.scale
            if self.image_locations[2] <= 0:
                self.user_x_position += 16
                self.opp_x_position += 13
            if self.user_x_position > self.width + 30 and self.opp_x_position > self.width + 30:
                self.on_race = False
            self.RunAnimation()

    def Win2(self):
        pass

    def Win3(self):
        pass

    def RunAnimation(self):
        """Runs the animation"""
        self.dt = (time.time() - self.last_time) * 100
        self.last_time = time.time()
        self.CarImageCycle()
        for image in self.image_locations:
            if image > -1920:
                self.screen.blit(self.background_images[self.image_locations.index(image)], [image, 0])
        if self.image_locations[2] <= 0:
            self.screen.blit(self.background_images[2], [0, 0])
        self.screen.blit(self.current_user_image, [self.user_x_position, self.user_y_position])
        self.screen.blit(self.current_opp_image, [self.opp_x_position, self.opp_y_position])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_race = False
        self.clock.tick(100)




