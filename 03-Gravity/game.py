import pygame
from sys import exit

pygame.init()

window_size = [800, 600]
screen = pygame.display.set_mode(window_size) # [x : left to right, y : up to down]
pygame.display.set_caption("Dark Souls")
clock = pygame.time.Clock()

player_img = pygame.image.load("graphics/Player/player_stand.png")
player_size = player_img.get_size()

player_coords = [(window_size[0] - player_size[0]) / 2, (window_size[1] - player_size[1]) / 2] # center 

moving_left = False
moving_right = False

drop = False
player_y_momentum = 0

while True:
    screen.fill((160, 240, 60))
    screen.blit(player_img, player_coords) # render image top left to bottom right

    if drop:
        if player_coords[1] >= window_size[1] - player_size[1]:
            player_y_momentum *= -1
        else:
            player_y_momentum += 0.5

        player_coords[1] += player_y_momentum

    if moving_left:
        player_coords[0] -= 4
    if moving_right:
        player_coords[0] += 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_DOWN:
                drop = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.display.update()
    clock.tick(60)

