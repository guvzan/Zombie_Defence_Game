class Settings:
    def __init__(self):
        """Ініціалізація налаштувань"""
        #Налаштування дисплею
        self.display_width = 1200
        self.display_height = 800
        self.bg_color = (230, 230, 230)

        #Налаштування гравця
        self.player_speed = 1

        #Налаштування кулі
        self.bullet_speed =2
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
