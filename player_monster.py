# this is the player file - but you're a moster...

import pygame
import global_vars

class PlayerMonster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface(global_vars.player_size)
        self.image.fill(global_vars.player_color)

        self.rect = self.image.get_rect()
        print('here?')

        self.health = 100
        self.strength = 100
        self.speed = 10

        # set speed vector
        self.change_x = 0
        self.change_y = 0

    def change_speed(self, x, y):
        # change the speed of the player
        print('in change speed: ', x, ' ', y)
        self.change_x += x
        self.change_y += y

    def update(self):
        # update the players positon
        self.rect.x = self.change_x
        self.rect.y = self.change_y
