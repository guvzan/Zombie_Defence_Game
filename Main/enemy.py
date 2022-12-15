import random
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Стандартний противник"""
    def __init__(self, zd_game, x, y):
        """Ініціалізація параметрів противника"""
        super().__init__()
        self.zd_game = zd_game
        self.screen = zd_game.screen
        self.health = 50
        self.image = pygame.image.load("../images/enemy_icon.bmp")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.active = True
        self.speed = 0.5


    def place_ememy(self):
        """Поставити противника на карту"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Рух противника"""
        if self.rect.x > self.zd_game.player.rect.x:
            self.x -= self.speed
        elif self.rect.x < self.zd_game.player.rect.x:
            self.x += self.speed

        if self.rect.y > self.zd_game.player.rect.y:
            self.y -= self.speed
        elif self.rect.y < self.zd_game.player.rect.y:
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y
        self.place_ememy()



