import pygame
from sys import exit

import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

ocean_surf = pygame.image.load('ocean/ocean.png').convert_alpha()
ocean_surf_pos = -700
sky_surf = pygame.image.load('sky/sky.png').convert_alpha()
castrod_surf = pygame.image.load('rods/castrod.png').convert_alpha()
uncastrod_surf = pygame.image.load('rods/uncastrod.png').convert_alpha()
space = False
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = True
        elif event.type == pygame.KEYUP:
                space = False
                

    screen.blit(sky_surf, (0, 0))
    screen.blit(ocean_surf, (ocean_surf_pos, 475))
    ocean_surf_pos+=0.5
    if ocean_surf_pos > 0: ocean_surf_pos = -700

    if space == False: screen.blit(uncastrod_surf, (400, 0))
    else: screen.blit(castrod_surf, (400, 0))


    
    pygame.display.update()
    clock.tick(60)