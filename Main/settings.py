import pygame.image

class Settings:
    def __init__(self):
        """Ініціалізація налаштувань"""
        #Налаштування дисплею
        self.display_width = 1200
        self.display_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("../images/background_grass.bmp")
        self.screen_rect = self.bg_image.get_rect()

        #Налаштування гравця
        self.player_speed = 1

        #Налаштування кулі
        self.bullet_speed =2
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)

        #Налаштування деяких текстів
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (0, 0, 0)


