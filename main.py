# Main class to start the game

import pygame
import random
from dungeonGen import dMap
from items import Block
from player_monster import PlayerMonster
import global_vars

global_vars.init()

PLAYER_SPEED = 3

# Pygame start
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of every sprite in the game
all_sprites_list = pygame.sprite.Group()

# list of all the blocks in the game (for the dungeon)
block_list = pygame.sprite.Group()

# bullet list (don't need this yet - maybe will make it particle list)

# create the player
player = PlayerMonster()
print('player', player.health)
all_sprites_list.add(player)

done = False

# clock
clock = pygame.time.Clock()

score = 0
player.rect.y = 370 # starting position

# create dungeon

#------- main game loop --------

while not done:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print('w')

    # continous key pressed
    if pressed[pygame.K_LEFT]:
        player.change_speed(-PLAYER_SPEED,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #
        elif event.type == pygame.KEYDOWN:
            print('keydown')
            if event.key == pygame.K_LEFT:
                player.change_speed(-PLAYER_SPEED,0)
            elif event.key == pygame.K_RIGHT:
                print('key right')
                player.change_speed(PLAYER_SPEED, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, -PLAYER_SPEED)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, PLAYER_SPEED)
            elif event.key == pygame.K_ESCAPE:
                print('escape')
                done = True
                break


    # game logic
    # update all the objects (update on the sprites)
    all_sprites_list.update()

    # draw one frame
    # clear the screen
    screen.fill(global_vars.GREY)

    # draw all the sprites
    all_sprites_list.draw(screen)

    #update the screen we have drawn
    pygame.display.flip()

    # limit the clock to 20 frames per second
    clock.tick(60)

pygame.quit()
