import pygame.font


class Statistic:
    """Клас, що відслідковує ігрову статистику"""
    def __init__(self, zd_game):
        """Ініціалізація статистики"""
        self.screen = zd_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 155, 0)
        self.bg_color = (0, 0, 155)
        self.font = pygame.font.SysFont(None, 48)
        self.score = 0
        self.prep_score()

    def prep_score(self):
        """Перевести очки в зображення"""
        score_str = str(self.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_score(self):
        """Показати очки"""
        self.screen.blit(self.score_image, self.score_rect)