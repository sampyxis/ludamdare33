import pygame
import global_vars
from create_level import create_level

global_vars.init()

pygame.init()

screen_width = 640
screen_height = 480
done = False

screen = pygame.display.set_mode([screen_width, screen_height])

all_sprites_list = pygame.sprite.Group()
all_items_list = pygame.sprite.Group()
all_block_list = pygame.sprite.Group()
all_actor_list = pygame.sprite.Group()

clock = pygame.time.Clock()
create_level()

while not done:

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        print('escape')
        done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.update()
    all_items_list.update()
    all_block_list.update()
    all_actor_list.update()

    screen.fill(global_vars.GREY)

    all_sprites_list.draw(screen)
    all_items_list.draw(screen)
    all_block_list.draw(screen)
    all_actor_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
