import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Dark Souls")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_suface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
player = pygame.image.load("graphics/Player/player_stand.png")
text_surface = test_font.render("Dark Souls: Prepare to Cry", False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_suface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (150, 50))

    pygame.display.update()
    clock.tick(60)

