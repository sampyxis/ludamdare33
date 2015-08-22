# holds all the items for the game
# includes blocks for the dungeon, loot, anything that ends up in the dungeon

import pygame
import global_vars
# Block is a sprite - generated - and represents the walls

class Items(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface(global_vars.player_size)
        self.image.fill(color)

        self.rect = self.image.get_image()

class Blocky(pygame.sprite.Sprite):
    def __init__(self, color): # a block can be various colors
        super().__init__() # call the pygame sprite class

        self.image = pygame.Surface(global_vars.player_size)
        self.image.fill(color)

        self.rect = self.image.get_image()

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([20,20])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.health = 100
        self.strength = 100
        self.speed = 10

        # set speed vector
        self.change_x = 0
        self.change_y = 0
