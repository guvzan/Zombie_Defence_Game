import pygame

from settings import Settings
from player import Player

class ZombieDefence:
    """Основний клас, що представляє собою всю гру"""
    def __init__(self):
        """Ініціалізація гри"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.display_width = self.screen.get_width()
        self.settings.display_height = self.screen.get_height()
        self.player = Player(self)
        pygame.display.set_caption("Zombie Defence")

    def run_game(self):
        """Основний цикл гри"""
        while True:
            self._check_events()
            self.player.update_position()
            self._update_screen()


    def _check_events(self):
        """Перевіряти на натискання клавіш і мишки"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагувати на натискання клавіші"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Реагувати на відпускання клавіші"""
        if event.key == pygame.K_q:
            exit()
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
            self.player.look_right = False
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def _update_screen(self):
        """Оновилювати зображення на екрані"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    zd = ZombieDefence()
    zd.run_game()