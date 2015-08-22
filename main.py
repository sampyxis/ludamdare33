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

# dungeon test
block = Block(global_vars.BLUE)

# create dungeon - need to move to a new file
def createLevel():
    startx=80   # map width
    starty=60  # map height
    themap= dMap()
    themap.makeMap(startx,starty,11,10,60) # was themap.makeMap(startx,starty,11,50,60)
    for y in range(starty):
            line = ""
            for x in range(startx):
                    block = Block(global_vars.BLUE)
                    block_black = Block(global_vars.BLACK)
                    if themap.mapArr[y][x]==0:
                            line += "."
                            block_black.rect.x = x * 20
                            block_black.rect.y = y * 20
                            block_list.add(block_black)
                            all_sprites_list.add(block_black)
                    if themap.mapArr[y][x]==1:
                            line += " "
                    if themap.mapArr[y][x]==2:
                        #block.rect = themap.mapArr[y][x]
                        block.rect.x = x * 20
                        block.rect.y = y * 20
                        #print('x: ', x, 'y: ', y)
                        block_list.add(block)
                        all_sprites_list.add(block)
                        line += "#"
                    if themap.mapArr[y][x]==3 or themap.mapArr[y][x]==4 or themap.mapArr[y][x]==5:
                            line += "="


            #print('add in list')
            print(line)
# end dungeon

#------- main game loop --------
createLevel()
while not done:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print('w')

    # continous key pressed
    if pressed[pygame.K_LEFT]:
        player.change_speed(-PLAYER_SPEED,0)
        for platform in block_list:
            platform.rect.x += 10
    elif pressed[pygame.K_RIGHT]:
        player.change_speed(PLAYER_SPEED, 0)
        for platform in block_list:
            platform.rect.x -= 10
    elif pressed[pygame.K_UP]:
        player.change_speed(0, -PLAYER_SPEED)
    elif pressed[pygame.K_DOWN]:
        player.change_speed(0, PLAYER_SPEED)
    elif pressed[pygame.K_ESCAPE]:
        print('escape')
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #



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
