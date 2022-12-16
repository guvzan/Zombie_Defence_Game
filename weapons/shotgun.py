class Shotgun:
    """Дробовик"""
    def __init__(self):
        """Ініціалізація параметрів дробовика"""
        self.name = "shotgun"
        self.bullet_speed = 4
        self.bullet_dispersion = [-0.1, 0, 0.1]
        self.bullets_left = 12
        self.max_capacity = 20
        self.damage = 15
        self.slot_number = 1

    def shoot(self, shoot_direction, x, y, bullets_amount):
        """Керувати траекторіями пістолетних куль"""
        if shoot_direction == "up":
            x += self.bullet_speed * self.bullet_dispersion[bullets_amount]
            y -= self.bullet_speed
        elif shoot_direction == "left":
            x -= self.bullet_speed
            y += self.bullet_speed * self.bullet_dispersion[bullets_amount]
        elif shoot_direction == "right":
            x += self.bullet_speed
            y += self.bullet_speed * self.bullet_dispersion[bullets_amount]
        elif shoot_direction == "down":
            x += self.bullet_speed * self.bullet_dispersion[bullets_amount]
            y += self.bullet_speed
        return x, y