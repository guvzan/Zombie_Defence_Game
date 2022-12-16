import time

import pygame

from settings import Settings
from player import Player
from bullet import Bullet
from inventory import Inventory
from pickup import Pickup
from enemy import Enemy
from statistic import Statistic
from spawnpoint import Spawnpoint

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
        self.statistic = Statistic(self)
        self.spawnpoints = pygame.sprite.Group()
        pygame.display.set_caption("Zombie Defence")

        self._set_primary_settables()

    def run_game(self):
        """Основний цикл гри"""
        while True:
            self._check_events()
            if self.player.alive:
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
        if event.key == pygame.K_r and not self.player.alive:
            self._restart()
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
        self.screen.fill(self.settings.bg_color, self.settings.screen_rect)
        self.player.blitme()
        self.inventory.draw_inventory()
        self.statistic.show_score()
        self._update_pickups()
        self._update_enemies()
        self._check_spawnpoints()
        self._check_ammo()
        self._check_player_enemy()
        self._check_powerup_time()
        if self.player.weapon != None:
            self._check_bullets_enemies()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.player.alive:
            self._show_gameover_text()
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

    def _check_bullets_enemies(self):
        """Перевіряти попадання куль в противників"""
        collisions = pygame.sprite.groupcollide(
            self.standart_enemies, self.bullets, False, False)
        for enemy, bullets in collisions.items():
            self.bullets.remove(bullets)
            enemy.current_health -= self.player.weapon.damage * len(bullets)
            if enemy.current_health <= 0:
                self.standart_enemies.remove(enemy)
                enemy.check_death()
                self.statistic.score += enemy.points_for_kill
                self.statistic.prep_score()

    def _set_spawnpoint(self, name, x, y):
        """Поставити точку спауна на карту"""
        new_spawnpoint = Spawnpoint(self, name, x, y)
        self.spawnpoints.add(new_spawnpoint)

    def _check_spawnpoints(self):
        """Оновлювати спавнпоінти"""
        for spawn in self.spawnpoints:
            spawn.update()
            spawn.spawn_enemy()

    def _check_ammo(self):
        """Вивести кількість патронів у кожній зброї"""
        for weapon in self.player.inventory:
            if weapon:
                ammo_str = str(weapon.bullets_left)
                ammo_image = self.settings.font.render(
                    ammo_str, True, self.settings.bg_color, self.settings.text_color)
                ammo_rect = ammo_image.get_rect()
                ammo_rect.x = (7 + 70) * weapon.slot_number + 7
                ammo_rect.y = 70
                self.screen.blit(ammo_image, ammo_rect)

    def _check_player_enemy(self):
        """Перевіряти, чи гравець не торкається противника"""
        if not self.player.invinsible_time:
            for enemy in self.standart_enemies:
                if self.player.rect.colliderect(enemy.rect):
                    self.player.current_health -= enemy.damage
                    self.player.invinsible_time = 500
                    if self.player.current_health <= 0:
                        self.player.alive = False

    def _check_powerup_time(self):
        """Відслідковувати тимчасові ефекти на гравцеві"""
        if self.player.invinsible_time > 0:
            self.player.invinsible_time -= 1

    def _show_gameover_text(self):
        """Текст про закінчення гри"""
        text_str = "Game Over"
        text_image = self.settings.font.render(
            text_str, True, self.settings.bg_color, self.settings.text_color)
        text_rect = text_image.get_rect()
        text_rect.center = self.screen.get_rect().center
        self.screen.blit(text_image, text_rect)

    def _restart(self):
        """Рестарт гри"""
        self.player.reset()
        self.standart_enemies.empty()
        self.bullets.empty()
        self._set_primary_settables()

    def _set_primary_settables(self):
        """Розставити підбирачки, противників, спавнпоінти і т.д."""
        # Розставити початкові підбирачки
        self._place_pickup("pistol_pickup", 100, 100)
        self._place_pickup("shotgun_pickup", 300, 400)

        # Розставити початкових противників
        self._make_enemy(250, 250)
        self._make_enemy(350, 350)

        # Розставити точки спауна
        self._set_spawnpoint("red_cube", 500, 100)
        self._set_spawnpoint("red_cube", 1000, 300)












if __name__ == "__main__":
    zd = ZombieDefence()
    zd.run_game()