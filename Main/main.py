import pygame

from settings import Settings
from player import Player
from bullet import Bullet
from inventory import Inventory
from pickup import Pickup
from enemy import Enemy

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
        self.bullets = pygame.sprite.Group()
        self.inventory = Inventory(self)
        self.pickups = pygame.sprite.Group()
        self.standart_enemies = pygame.sprite.Group()
        pygame.display.set_caption("Zombie Defence")

        #Розставити початкові підбирачки
        self._place_pickup("pistol_pickup", 100, 100)
        self._place_pickup("shotgun_pickup", 300, 400)

        #Розставити початкових противників
        self._make_enemy(250, 250)

    def run_game(self):
        """Основний цикл гри"""
        while True:
            self._check_events()
            self.player.update_position()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        """Перевіряти на натискання клавіш і ми шки"""
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
            self.player.look_direction = "right"
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.player.look_direction = "left"
        if event.key == pygame.K_UP:
            self.player.moving_up = True
            self.player.look_direction = "up"
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True
            self.player.look_direction = "down"
        if self.player.weapon != None:
            if event.key == pygame.K_SPACE and self.player.weapon.bullets_left > 0:
                self._fire_bullet()
        if event.key == pygame.K_1:
            self.player.weapon = self.player.inventory[0]
            self.player.weapon_index = 0
        if event.key == pygame.K_2:
            self.player.weapon = self.player.inventory[1]
            self.player.weapon_index = 1

    def _check_keyup_events(self, event):
        """Реагувати на відпускання клавіші"""
        if event.key == pygame.K_q:
            exit()
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
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
        self.inventory.draw_inventory()
        self._update_pickups()
        self._update_enemies()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        """Створити нову кулю та додати її до групи куль"""
        if self.player.weapon == None:
            pass
        elif self.player.weapon.name == "pistol":
            new_bullet = Bullet(self, self.player, 1)
            self.bullets.add(new_bullet)
            self.player.weapon.bullets_left -= 1
        elif self.player.weapon.name == "shotgun":
            for i in range(0, 3):
                new_bullet = Bullet(self, self.player, i)
                self.bullets.add(new_bullet)
            self.player.weapon.bullets_left -= 1

    def _update_bullets(self):
        """Оновлює позицію куль та видаляє старі кулі"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <=0 or bullet.rect.top >= self.settings.display_height
            or bullet.rect.right <= 0 or bullet.rect.left >=self.settings.display_width):
                self.bullets.remove(bullet)
        if self.player.weapon != None:
            self._check_bullets()

    def _place_pickup(self, name, x, y):
        """Ставить підбирачки на карту"""
        new_pickup = Pickup(self, name, x, y)
        self.pickups.add(new_pickup)

    def _update_pickups(self):
        """Оновлює стан підбирачок"""
        weapon_name = None
        for pickup in self.pickups.sprites():
            if pickup.active == True:
                pickup.place_pickup()

        for pickup in self.pickups.copy():
            if self.player.rect.colliderect(pickup.rect):
                weapon_name = pickup.name
                self.pickups.remove(pickup)
            self.player.get_weapon(weapon_name)

    def _check_bullets(self):
        """Забрати пушку з інвентарю, якщо там нема патронів"""
        if self.player.weapon.bullets_left == 0:
            self.player.inventory[self.player.weapon_index] = None

    def _make_enemy(self, x, y):
        """Поставити противника на карту"""
        new_enemy = Enemy(self, x, y)
        self.standart_enemies.add(new_enemy)

    def _update_enemies(self):
        """Оновити позиції противників"""
        for enemy in self.standart_enemies:
            enemy.update()







if __name__ == "__main__":
    zd = ZombieDefence()
    zd.run_game()