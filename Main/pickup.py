import pygame

class Pickup:
    """Що тільки на дорозі не валяється..."""
    def __init__(self, zd_game, name, x, y):
        """Ініціалізація підбирачки"""
        self.screen = zd_game.screen
        self.active = True
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"../images/{name}.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def place_pickup(self):
        """Поставити підбирачку на карту"""
        self.screen.blit(self.image, self.rect)