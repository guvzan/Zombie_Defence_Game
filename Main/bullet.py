import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас кулі вогнепальної зброї"""
    def __init__(self, zd_game, player, bullets_amount):
        """Ініціалізація кулі"""
        super().__init__()
        self.screen = zd_game.screen
        self.settings = zd_game.settings
        self.color = self.settings.bullet_color

        #Створення rect кулі та задання позиції
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = zd_game.player.rect.center

        #Координати пострілів, так скажем
        self.moving_direction = player.look_direction
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #З якої зброї постріл
        self.weapon = player.weapon
        self.bullets_amount = bullets_amount

    def update(self):
        """Рухати кулю в потрібному напрямку"""
        self.x, self.y = self.weapon.shoot(self.moving_direction, self.x, self.y, self.bullets_amount)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю в поточній позиції"""
        pygame.draw.rect(self.screen, self.color, self.rect)