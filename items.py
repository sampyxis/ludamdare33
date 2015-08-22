# holds all the items for the game
# includes blocks for the dungeon, loot, anything that ends up in the dungeon

import pygame
# Block is a sprite - generated - and represents the walls
class Block(pygame.sprite.Sprite):
    def __init__(self, color, size = []): # a block can be various colors
        super().__init__() # call the pygame sprite class

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_image()
