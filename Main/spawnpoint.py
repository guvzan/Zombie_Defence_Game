import pygame
import random

from enemy import Enemy
from pygame.sprite import Sprite

class Spawnpoint(Sprite):
    """Точка спауна противників"""
    def __init__(self, zd_game, enemy_name, x, y):
        """Ініціалізація точки спауна"""
        super().__init__()
        self.zd_game = zd_game
        self.screen = zd_game.screen
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.color = (0, 0, 155)
        self.rect.x = x
        self.rect.y = y
        self.enemy_name = enemy_name

    def spawn_enemy(self):
        """Заспавнити противника"""
        number = random.randint(0, 10000)
        if number <= 3:
            if self.enemy_name == "red_cube":
                new_enemy = Enemy(self.zd_game, self.rect.x, self.rect.y)
                self.zd_game.standart_enemies.add(new_enemy)


    def update(self):
        """Намалювати точку спауна"""
        pygame.draw.rect(self.screen, self.color, self.rect)