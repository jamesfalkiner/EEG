import pygame
from Tools.FontRender import RenderFont, CreateNumber
from Tools.PictureUploads import LoadUpgradeBars, LoadUpgradeButtons, LoadUpgradeLevels, Loadify, TransformImage
import time
import shelve


class UpgradesMenu(object):
    def __init__(self, screen,upgrade_bars_images,buttons_images,upgrade_levels_text_images):
        self.BLACK = (0, 0, 0)
        self.LBLUE = (0, 204, 204)
        self.on_upgrades_menu = True
        self.rerender = True
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        self.scale = self.width/1920
        self.upgrade_parts = [["engine", 0], ["supercharger", 0], ["gearbox", 0], ["suspension", 0],
                              ["aerodynamics", 0], ["chassis", 0], ["tyres", 0], ["fuel", 0], ["exhaust", 0],
                              ["clutch", 0]]
        self.money = 1000
        self.money_font = RenderFont("$" + "{:,}".format(self.money), 25, self.BLACK)
        self.upgrade_names = [names for names, values in self.upgrade_parts]
        self.upgrade_prices = [100, 30, 100, 60, 100, 60, 30, 30, 60, 60]
        self.upgrade_prices_fonts = [RenderFont("$" + "{:,}".format(n), 28, self.BLACK) for n in self.upgrade_prices]

        ###############
        # Car original values which are changed
        ###############
        self.car_speed = 1
        self.car_acceleration = 1.01
        self.car_random = 100
        ###############
        # upgrade bar assignments
        ###############
        self.upgrade_bars = upgrade_bars_images
        self.upgrade_bars_shown = []
        ###############
        # button image assignments
        ###############
        self.button_images = buttons_images
        self.button_unpressed = self.button_images[0]
        self.button_hover = self.button_images[1]
        self.button_list = self.DrawButtons()  # sets the button locations on the screen
        ###############
        # level image assignments
        ###############
        self.upgrade_level_images = upgrade_levels_text_images  # list of all the upgrade levels
        self.upgrade_levels_shown = []
        self.upgrade_background = Loadify("Images/Backgrounds/Upgrade Menu 2.png")
        self.upgrade_background = TransformImage(self.upgrade_background, self.width, self.height)



    ##########
    """Following Functons display messages for the user for certain circumstances"""
    ##########
    def NotEnoughMoney(self):
        """Gives a message if the user doesnt have enough money to afford the upgrades"""
        start_time = time.time()
        error_message = "Not Enough Money"
        error_font = RenderFont(error_message, 40, self.BLACK)
        while (time.time() - start_time) < 1:
            self.screen.blit(error_font, [500, 500])
            pygame.display.update()

    def FullyUpgraded(self):
        """Gives the user a message if the part is fully upgraded"""
        start_time = time.time()
        message = "Part Already Fully Upgraded"
        message_font = RenderFont(message, 40, self.BLACK)
        while (time.time() - start_time) < 1:
            self.screen.blit(message_font, [800, 800])
            pygame.display.update()

    #########
    """Following Function causes each part to be upgraded"""
    #########

    def UpgradePart(self, number):
        """General function for upgrading the parts"""
        if self.upgrade_parts[number][1] <= 9:
            if self.money >= self.upgrade_prices[number]:
                self.upgrade_parts[number][1] += 1
                self.money -= self.upgrade_prices[number]
                self.rerender = True
                self.WriteMoney()
                self.WriteUpgrades()
                self.UpdateUpgradePrices()
            else:
                self.NotEnoughMoney()
        else:
            """Shows a message to the user if fully upgraded"""
            self.FullyUpgraded()

    ###########
    """Read and write functions"""
    ###########
    def WriteMoney(self):
        """Writes the money stats to the save file"""
        money_file = shelve.open("Data/Money/money")
        money_file["money"] = self.money
        money_file.close()

    def ReadMoney(self):
        """Reads the money"""
        money_file = shelve.open("Data/Money/money")
        self.money = money_file["money"]
        money_file.close()

    def WriteUpgrades(self):
        """Writes the upgrade level to a file"""
        file = shelve.open("Data/Upgrades/part_upgrades")
        upgrade_values = []
        for name, value in self.upgrade_parts:
            upgrade_values.append(value)
        file["tier1"] = upgrade_values
        file.close()

    def UpdateUpgradePrices(self):
        """Creates the upgrade prices"""
        counter = 0
        while counter < 10:
            for names, values in self.upgrade_parts:
                if counter == 0 or counter == 2 or counter == 4:
                    self.upgrade_prices[counter] = 10 * (values ** 2) + 10 * values + 100
                elif counter == 3 or counter == 5 or counter == 8 or counter == 9:
                    self.upgrade_prices[counter] = 6 * (values ** 2) + 6 * values + 60
                elif counter == 1 or counter == 6 or counter == 7:
                    self.upgrade_prices[counter] = 3 * (values ** 2) + 3 * values + 30
                counter += 1

    def ReadDictionary(self):
        """Reads the save file to create an up-to-date upgrade list"""
        keys = [names for names, value in self.upgrade_parts]
        value_file = shelve.open("Data/Upgrades/part_upgrades")
        values = value_file["tier1"]
        value_file.close()
        self.upgrade_parts = []
        for n in range(10):
            self.upgrade_parts.append([keys[n], values[n]])

    ##########
    """Window Update Functions"""
    ##########
    def ScreenBlit(self):
        """Blits the screen with the corresponding fonts
        Will rerender the fonts if there has been a change in upgrades"""
        if self.rerender:
            self.money_font = RenderFont("$" + "{:,}".format(self.money), 25, self.BLACK)
            self.upgrade_prices_fonts = [RenderFont("$" + "{:,}".format(n), 28, self.BLACK) for n in self.upgrade_prices]
            self.rerender = False
            self.FindUpgradeBars()
            self.FindLevelBars()
            font_counter = 0
            for name, value in self.upgrade_parts:
                if value == 10:
                    self.upgrade_prices_fonts[font_counter] = RenderFont("Fully Upgraded", 28, self.BLACK)
                font_counter += 1
        self.screen.fill(self.LBLUE)
        self.screen.blit(self.upgrade_background, [0, 0])
        upgrade_counter = 0
        for value in self.upgrade_prices_fonts:
            self.screen.blit(value, [1150 * self.scale, (upgrade_counter * 80 + 272) * self.scale])
            upgrade_counter += 1
        for value in range(10):
            self.screen.blit(self.button_unpressed, [500 * self.scale, (value * 80 + 275) * self.scale])
        bar_counter = 0
        for bar in self.upgrade_bars_shown:
            self.screen.blit(bar, [1510 * self.scale, (bar_counter * 80 + 267) * self.scale])
            bar_counter += 1
        level_counter = 0
        for level in self.upgrade_levels_shown:
            self.screen.blit(level, [400 * self.scale, (level_counter * 80 + 265) * self.scale])
            level_counter += 1
        self.screen.blit(self.money_font, [1500 * self.scale, 125 * self.scale])

    def DrawButtons(self):
        """Draw the buttons for the upgrades menu"""
        button_list = []
        for number in range(10):
            button_list.append(pygame.Rect(500 * self.scale, (number * 80 + 275) * self.scale, 100, 50))
        return button_list

    def FindUpgradeBars(self):
        """This function checks to see what level the upgrade is and creates the correct list"""
        self.upgrade_bars_shown = [self.upgrade_bars[value] for name, value in self.upgrade_parts]

    def FindLevelBars(self):
        """This function checks to see what level the upgrade is and creates the correct list"""
        self.upgrade_levels_shown = []
        for name, values in self.upgrade_parts:
            self.upgrade_levels_shown.append(self.upgrade_level_images[int(values)])

    def AnimateButton(self, number):
        image_counter = 0
        while image_counter < len(self.button_images):
            self.screen.blit(self.upgrade_background, [0, 0])
            upgrade_counter = 0
            for value in self.upgrade_prices_fonts:
                self.screen.blit(value, [1150 * self.scale, (upgrade_counter * 80 + 272) * self.scale])
                upgrade_counter += 1
            for value in range(10):
                if value != number:
                    self.screen.blit(self.button_unpressed, [500 * self.scale, (value * 80 + 275) * self.scale])
            bar_counter = 0
            for bar in self.upgrade_bars_shown:
                self.screen.blit(bar, [1510 * self.scale, (bar_counter * 80 + 267) * self.scale])
                bar_counter += 1
            level_counter = 0
            for level in self.upgrade_levels_shown:
                self.screen.blit(level, [400 * self.scale, (level_counter * 80 + 265) * self.scale])
                level_counter += 1
            self.screen.blit(self.money_font, [1500 * self.scale, 125 * self.scale])
            self.screen.blit(self.button_images[(round(image_counter))], [500 * self.scale, (number * 80 + 275) * self.scale])
            image_counter += 1
            pygame.display.update()


    def ShowWindow(self):
        """Shows the window for the upgrade menu"""
        self.ReadMoney()
        self.ReadDictionary()
        self.UpdateUpgradePrices()
        click = False
        while self.on_upgrades_menu:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_upgrades_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            self.ScreenBlit()  # blits all the fonts onto the screen
            mx, my = pygame.mouse.get_pos()
            for buttons in self.button_list:
                if buttons.collidepoint(mx, my):
                    self.screen.blit(self.button_hover, [500 * self.scale, (int(self.button_list.index(buttons)) * 80 +
                                                                            275) * self.scale])
                    """If user clicks on any of the buttons"""
                    if click:

                        if self.button_list.index(buttons) == 0:
                            self.AnimateButton(0)
                            self.UpgradePart(0)
                        elif self.button_list.index(buttons) == 1:
                            self.AnimateButton(1)
                            self.UpgradePart(1)
                        elif self.button_list.index(buttons) == 2:
                            self.AnimateButton(2)
                            self.UpgradePart(2)
                        elif self.button_list.index(buttons) == 3:
                            self.AnimateButton(3)
                            self.UpgradePart(3)
                        elif self.button_list.index(buttons) == 4:
                            self.AnimateButton(4)
                            self.UpgradePart(4)
                        elif self.button_list.index(buttons) == 5:
                            self.AnimateButton(5)
                            self.UpgradePart(5)
                        elif self.button_list.index(buttons) == 6:
                            self.AnimateButton(6)
                            self.UpgradePart(6)
                        elif self.button_list.index(buttons) == 7:
                            self.AnimateButton(7)
                            self.UpgradePart(7)
                        elif self.button_list.index(buttons) == 8:
                            self.AnimateButton(8)
                            self.UpgradePart(8)
                        elif self.button_list.index(buttons) == 9:
                            self.AnimateButton(9)
                            self.UpgradePart(9)
                        click = False
            pygame.display.update()



