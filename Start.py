import time
import pygame

class Start(object):
    def __init__(self, screen):
        self.track_temp = 24
        self.tyre_score = int
        self.screen = screen
        self.tyre_temp = int
        self.tyre_burst = False

    def Start(self):
        """Function for figuring out how long button is pressed"""
        time_held = self.HeldTime()
        self.TempCalc(time_held)
        vlow = 0.5
        low = 0.7
        med = 0.8
        high = 0.9
        vhigh = 1
        if self.tyre_temp<=40:
            self.tyre_score = vlow
        if self.tyre_temp>40 and self.tyre_temp<=65:
            self.tyre_score = low
        if self.tyre_temp>65 and self.tyre_temp<=85:
            self.tyre_score = med
        if self.tyre_temp>85 and self.tyre_temp<=90:
            self.tyre_score = high
        if self.tyre_temp>90 and self.tyre_temp<=100:
            self.tyre_score = vhigh
        if self.tyre_temp>100 and self.tyre_temp<=110:
            self.tyre_score = med
        if self.tyre_temp>110 and self.tyre_temp<=130:
            self.tyre_score = low
        if self.tyre_temp>130 and self.tyre_temp<=150:
            self.tyre_score = vlow
        print("Tyre score =", self.tyre_score)
        print("Tyre temp was = ", self.tyre_temp, "°C")
        print("Time held", time_held)
        print("Tyre Burst?", self.tyre_burst)


    def HeldTime(self):
        calculating = True
        self.screen.fill((0, 50, 0))
        time_held = 0
        counting = False
        previous_time = 0
        """Calculates how much time you've held down W, adding 0.05 every 50ms to the time held. Calculates
        and updates tyre temperature every 0,05 seconds too, resulting in visual feedback for tyre
        temperature."""
        while calculating:
            if counting: 
                if time.time() > (previous_time+0.05):
                    previous_time = time.time()
                    time_held += 0.05
                    self.TempCalc(time_held)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        init_time = time.time()
                        counting = True
                        self.screen.fill((0, 50, 100))
                    if event.key == pygame.K_ESCAPE:
                        calculating = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        fin_time = time.time()
                        held_time = fin_time - init_time
                        print("Exact held time", held_time)
                        return time_held

            pygame.display.update()

    def TempCalc(self, time_held):

        #Tyre temperature is the time held x the rate of tyre temperature increase plus the starting temp
        temp_factor = 30

        self.tyre_temp = self.track_temp+(time_held*temp_factor)

        if self.tyre_temp < 250:
            self.screen.fill((251-self.tyre_temp, self.tyre_temp, 125))
        else:
            self.screen.fill((0,0,0))

        if self.tyre_temp>150:
            self.tyre_score = 0
            self.tyre_burst = True
            self.screen.fill((0, 0, 0))