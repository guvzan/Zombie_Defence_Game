import random
import pygame

from pygame.sprite import Sprite
from pickup import Pickup

class Enemy(Sprite):
    """Стандартний противник"""
    def __init__(self, zd_game, x, y):
        """Ініціалізація параметрів противника"""
        super().__init__()
        # Стати противника
        self.max_health = 50
        self.current_health = self.max_health
        self.speed = 0.1
        self.points_for_kill = 50
        self.name = "red_cube"
        self.damage = 25

        #Технічні змінні
        self.zd_game = zd_game
        self.screen = zd_game.screen
        self.image = pygame.image.load("../images/enemy_icon.bmp")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.active = True
        self.health_bar_color = (255, 0, 0)
        self.health_bar_multiply_index = float(70 / self.max_health)




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
        if self.current_health < self.max_health:
            self.draw_health_bar()

    def draw_health_bar(self):
        """Малювати полоску здоров'я"""
        self.health_bar = pygame.Rect(
            0, 0, self.current_health * self.health_bar_multiply_index, 10)
        self.health_bar.x = self.rect.x
        self.health_bar.y = self.rect.y - 20
        pygame.draw.rect(self.screen, self.health_bar_color, self.health_bar)

    def check_death(self):
        """Дії, якщо противник вбитий"""
        action = random.randint(0, 100)
        if action <= 50:
            new_pickup = Pickup(self.zd_game, "pistol_pickup", self.rect.x, self.rect.y)
        elif action <= 100:
            new_pickup = Pickup(self.zd_game, "shotgun_pickup", self.rect.x, self.rect.y)
        self.zd_game.pickups.add(new_pickup)



