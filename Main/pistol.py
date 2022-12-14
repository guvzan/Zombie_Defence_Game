class Pistol:
    """Пістолет"""
    def __init__(self):
        """Ініціалізація параметрів пістолета"""
        self.bullet_speed = 1.5

    def shoot(self, shoot_direction, x, y):
        """Керувати траекторіями пістолетних куль"""
        if shoot_direction == "up":
            y -= self.bullet_speed
        elif shoot_direction == "left":
            x -= self.bullet_speed
        elif shoot_direction == "right":
            x += self.bullet_speed
        elif shoot_direction == "down":
            y += self.bullet_speed
        return x, y
