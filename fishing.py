import pygame
from sys import exit

import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

ocean_surface = pygame.image.load('ocean/ocean.png').convert_alpha()
ocean_surface_pos = -700
sky_surface = pygame.image.load('sky/sky.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ocean_surface, (ocean_surface_pos, 475))
    ocean_surface_pos+=1
    if ocean_surface_pos > 0: ocean_surface_pos = -700
    
    pygame.display.update()
    clock.tick(60)