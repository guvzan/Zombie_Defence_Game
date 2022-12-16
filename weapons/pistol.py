class Pistol:
    """Пістолет"""
    def __init__(self):
        """Ініціалізація параметрів пістолета"""
        self.name = "pistol"
        self.bullet_speed = 1.5
        self.bullets_left = 15
        self.max_capacity = 50
        self.damage = 23
        self.slot_number = 0

    def shoot(self, shoot_direction, x, y, bullets_amount):
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
