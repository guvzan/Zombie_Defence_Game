import pygame

from settings import Settings
from weapons.pistol import Pistol
from weapons.shotgun import Shotgun


class Player:
    """Клас гравця"""
    def __init__(self, zd_game):
        """Ініціалізація гравця"""
        self.screen = zd_game.screen
        self.screen_rect = zd_game.screen.get_rect()
        self.settings = Settings()

        #Завантаження картинки гравця
        self.image = pygame.image.load("../images/player_icon.bmp")
        self.rect = self.image.get_rect()

        #Спавнити гравця по центру екрана
        self.rect.center = self.screen_rect.center

        #Індикатори руху
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Індикатори повороту
        self.look_direction = "up"

        #Інвентар
        self.inventory = [Pistol(), None, None]
        self.weapon = Shotgun()



    def update_position(self):
        """Метод для руху гравця"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Намалювати гравця на екрані"""
        self.screen.blit(self.image, self.rect)