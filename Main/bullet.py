import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас кулі вогнепальної зброї"""
    def __init__(self, zd_game, player):
        """Ініціалізація кулі"""
        super().__init__()
        self.screen = zd_game.screen
        self.settings = zd_game.settings
        self.color = self.settings.bullet_color

        #Створення rect кулі та задання позиції
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = zd_game.player.rect.center

        self.moving_direction = player.look_direction
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Рухати кулю в потрібному напрямку"""
        if self.moving_direction == "up":
            self.y -= self.settings.bullet_speed
        elif self.moving_direction == "left":
            self.x -= self.settings.bullet_speed
        elif self.moving_direction == "right":
            self.x += self.settings.bullet_speed
        elif self.moving_direction == "down":
            self.y += self.settings.bullet_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю в поточній позиції"""
        pygame.draw.rect(self.screen, self.color, self.rect)