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

# items we can't pass through
all_items_list = pygame.sprite.Group()

# list of all the blocks in the game (for the dungeon)
block_list = pygame.sprite.Group()

actor_list = pygame.sprite.Group()

# bullet list (don't need this yet - maybe will make it particle list)

# create the player
player = PlayerMonster()
player.rect.x = screen_width / 2
player.rect.y = screen_width / 2

actor_list.add(player)

done = False

# clock
clock = pygame.time.Clock()

score = 0
#player.rect.y = 370 # starting position

# dungeon test
block = Block(global_vars.BLUE)

# create dungeon - need to move to a new file
def createLevel():
    startx=42   # map width
    starty=32  # map height
    themap= dMap()
    #makeMap(self,xsize,ysize,fail,b1,mrooms): the more fails - the more rooms
    themap.makeMap(startx,starty,50,10,60) # was themap.makeMap(startx,starty,11,50,60)
    for y in range(starty):
            line = ""
            map_ar = ""
            for x in range(startx):
                    block_wall = Block(global_vars.DARKGREY)
                    block_black = Block(global_vars.BLACK)
                    floor_block = Block(global_vars.BROWN)
                    open_door_block = Block(global_vars.OPEN_DOOR)
                    closed_door_block = Block(global_vars.BLACK)
                    secret_door_block = Block(global_vars.BLACK)

                    if themap.mapArr[y][x]==0: # 0 is floor
                            line += "."
                            map_ar += "0"
                            floor_block.rect.x = x * 20
                            floor_block.rect.y = y * 20
                            block_list.add(floor_block)
                            all_sprites_list.add(floor_block)
                    if themap.mapArr[y][x]==1:
                            line += " "
                            map_ar += "1"
                    if themap.mapArr[y][x]==2: # 2 is a wall
                        #block.rect = themap.mapArr[y][x]
                        block_wall.rect.x = x * 20
                        block_wall.rect.y = y * 20
                        #print('x: ', x, 'y: ', y)
                        block_list.add(block_wall)
                        all_sprites_list.add(block_wall)
                        all_items_list.add(block_wall)
                        line += "#"
                        map_ar += "2"
                    if themap.mapArr[y][x]==3: #open door
                        open_door_block.rect.x = x * 20
                        open_door_block.rect.y = y * 20
                        block_list.add(open_door_block)
                        all_sprites_list.add(open_door_block)
                    if themap.mapArr[y][x]==4: #closed door
                        line += "="
                        map_ar += "4"
                        closed_door_block.rect.x = x * 20
                        closed_door_block.rect.y = y * 20
                        block_list.add(closed_door_block)
                        all_sprites_list.add(closed_door_block)
                        all_items_list.add(closed_door_block)
                    if themap.mapArr[y][x]==5: # secret door
                        line += "="
                        map_ar += "4"
                        secret_door_block.rect.x = x * 20
                        secret_door_block.rect.y = y * 20
                        block_list.add(secret_door_block)
                        all_sprites_list.add(secret_door_block)
                        all_items_list.add(secret_door_block)


            #print('add in list')
            #print(line)
            print(map_ar)
# end dungeon

#------- main game loop --------
createLevel()
while not done:

    #print(player.rect.x)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.rect.x = 20
        player.rect.y = 20
        print('w')

    # continous key pressed
    if pressed[pygame.K_LEFT]:
        player.change_speed(-PLAYER_SPEED,0)
        global_vars.direction = global_vars.left
    if pressed[pygame.K_RIGHT]:
        player.change_speed(PLAYER_SPEED, 0)
        global_vars.direction = global_vars.right
    if pressed[pygame.K_UP]:
        player.change_speed(0, -PLAYER_SPEED)
        global_vars.direction = global_vars.up
    if pressed[pygame.K_DOWN]:
        player.change_speed(0, PLAYER_SPEED)
        global_vars.direction = global_vars.down
    if pressed[pygame.K_ESCAPE]:
        print('escape')
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print('x: ', pos[0], 'y: ', pos[1])

    # game logic
    # update all the objects (update on the sprites)
    all_sprites_list.update()
    # player needs a special update now...
    actor_list.update()
    # check for collisions
    block_hit_list = pygame.sprite.spritecollide(player, all_items_list, False)
    if(len(block_hit_list) > 0):
        for block in block_hit_list:
            #print('collide!')
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if global_vars.direction == global_vars.up:
                player.change_speed(0, PLAYER_SPEED)
            if global_vars.direction == global_vars.down:
                player.change_speed(0, -PLAYER_SPEED)
            if global_vars.direction == global_vars.right:
                player.change_speed(-PLAYER_SPEED, 0)
            if global_vars.direction == global_vars.left:
                player.change_speed(PLAYER_SPEED, 0)
            player.change_speed(0,3)
            block_hit_list.remove(block)
    #print('not collide')

    # draw one frame
    # clear the screen
    screen.fill(global_vars.GREY)

    # draw all the sprites
    all_sprites_list.draw(screen)
    actor_list.draw(screen)

    #update the screen we have drawn
    pygame.display.flip()

    # limit the clock to 20 frames per second
    clock.tick(60)

pygame.quit()
