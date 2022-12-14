import pygame

class Inventory:
    """Інвентар гравця"""
    def __init__(self, zd_game):
        """Ініціалізація параметрів інвентаря"""
        self.screen = zd_game.screen
        self.screen_rect = zd_game.screen.get_rect()
        self.player = zd_game.player

        #Розміри інвентарю
        self.border_color = (0, 255, 0)
        self.bg_color = (30, 30, 30)
        self.inventory_slots = len(zd_game.player.inventory)
        self.slot_width = 70
        self.slot_height = 70
        self.list_of_weapons = ["pistol.bmp", "shotgun.bmp"]

        #Створити об'єкт інвентаря і поставити де треба
        self.slots = [pygame.Rect(
            1.1 * x * self.slot_width + 7, 0, self.slot_width, self.slot_height) for x in range(self.inventory_slots)]

    def draw_inventory(self):
        """Намалювати полоску інвентаря"""
        for slot_number in range(len(self.slots)):
            self.screen.fill(self.bg_color, self.slots[slot_number])
            if self.player.inventory[slot_number]:
                slot_image = pygame.image.load(f"../images/{self.list_of_weapons[slot_number]}")
                slot_rect = slot_image.get_rect()
                slot_rect.x += (7 + 70) * slot_number + 7
                self.screen.blit(slot_image, slot_rect)





