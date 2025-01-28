import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Dark Souls")
clock = pygame.time.Clock()

sky_suface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
player = pygame.image.load("graphics/Player/player_stand.png")
player_walk1 = pygame.image.load("graphics/Player/player_walk_1.png")
player_walk2 = pygame.image.load("graphics/Player/player_walk_2.png")

player_move = False
walk_flag = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_move = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_move = False
    
    screen.blit(sky_suface, (0,0))
    screen.blit(ground_surface, (0,300))

    if not player_move:
        screen.blit(player, (200,300 - player.get_height()))
    else:
        if walk_flag:
            screen.blit(player_walk1, (200,300 - player.get_height()))
        else:
            screen.blit(player_walk2, (200,300 - player.get_height()))
        walk_flag = not walk_flag
        
    pygame.display.update()
    clock.tick(60)
