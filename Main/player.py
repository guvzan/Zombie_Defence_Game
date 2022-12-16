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

        #Індикатори руху
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



        # Те, що ресетиться при рестарті
        self.reset()





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
        self.draw_health_bar()

    def get_weapon(self, weapon_name):
        """Взяти пушку в інвентар"""
        if weapon_name == "pistol_pickup":
            if self.inventory[0]:
                self.inventory[0].bullets_left += 5
                current_ammo = self.inventory[0].bullets_left
                max_ammo = self.inventory[0].max_capacity
                if current_ammo > max_ammo:
                    self.inventory[0].bullets_left = max_ammo
            else:
                self.weapon = Pistol()
                self.inventory[0] = self.weapon
                self.weapon_index = 0
        elif weapon_name == "shotgun_pickup":
            if self.inventory[1]:
                self.inventory[1].bullets_left += 3
                current_ammo = self.inventory[1].bullets_left
                max_ammo = self.inventory[1].max_capacity
                if current_ammo > max_ammo:
                    self.inventory[1].bullets_left = max_ammo
            else:
                self.weapon = Shotgun()
                self.inventory[1] = self.weapon
                self.weapon_index = 1

    def draw_health_bar(self):
        """Намалювати полоску здоров'я гравця"""
        self.health_bar = pygame.Rect(
            0, 0, self.current_health * self.health_bar_multiply_index, 10)
        self.health_bar.x = self.rect.x
        self.health_bar.y = self.rect.y - 20
        pygame.draw.rect(self.screen, self.health_bar_color, self.health_bar)

    def reset(self):
        """Скинути налаштування до початкових"""

        # Технічні параметри гравця
        self.alive = True

        # Спавнити гравця по центру екрана
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Індикатори повороту
        self.look_direction = "up"

        # Інвентар
        self.inventory = [None, None, None, None]
        self.weapon_index = 0
        self.weapon = self.inventory[self.weapon_index]

        # Параметри гравця
        self.max_health = 100
        self.current_health = self.max_health
        self.health_bar_multiply_index = float(70 / self.max_health)
        self.health_bar_color = (0, 155, 0)
        self.invinsible_time = 0
