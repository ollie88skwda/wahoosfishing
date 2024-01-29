import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 50)

# background
ocean_surf = pygame.image.load('ocean/ocean.png').convert_alpha()
ocean_surf_pos = -700
sky_surf = pygame.image.load('sky/sky.png').convert_alpha()

# rod surfaces
castrod_surf = pygame.image.load('rods/castrod.png').convert_alpha()
uncastrod_surf = pygame.image.load('rods/uncastrod.png').convert_alpha()
precastrod_surf = pygame.image.load('rods/precastrod.png').convert_alpha()
semicastrod_surf = pygame.image.load('rods/semicastrod.png').convert_alpha()
space = False
spaceHold = 0

# fishies
redfishies = pygame.image.load('fishies/redfishies.png').convert_alpha()
orangefishies = pygame.image.load('fishies/orangefishies.png').convert_alpha()
yellowfishies = pygame.image.load('fishies/yellowfishies.png').convert_alpha()
greenfishies = pygame.image.load('fishies/greenfishies.png').convert_alpha()
bluefishies = pygame.image.load('fishies/bluefishies.png').convert_alpha()
purplefishies = pygame.image.load('fishies/purplefishies.png').convert_alpha()
pinkfishies = pygame.image.load('fishies/pinkfishies.png').convert_alpha()

allFishies = [redfishies, orangefishies, yellowfishies, greenfishies, bluefishies, purplefishies, pinkfishies]
fishyResetTimer = 0



while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = True
        elif event.type == pygame.KEYUP:
                space = False
                spaceHold = 0
                
    # blit background
    screen.blit(sky_surf, (0, 0))
    screen.blit(ocean_surf, (ocean_surf_pos, 475))
    ocean_surf_pos+=0.5
    if ocean_surf_pos > 0: ocean_surf_pos = -700

    # blit rod
    if space == False: 
        screen.blit(uncastrod_surf, (400, 0))
    elif spaceHold < 45: # change this number to make the rod cast shorter/longer
        screen.blit(precastrod_surf, (400, 0))
        spaceHold+=1
    elif spaceHold < 90: # change this number to make the semi cast animation shorter/longer
        screen.blit(semicastrod_surf, (400, 0))
        spaceHold+=1
    else: 
        screen.blit(castrod_surf, (400, 0))

    # blit fishies
    if fishyResetTimer < 300:
        fishyResetTimer+=1
    else:
        screen.blit(random.choice(allFishies), (400, 300))
        fishyResetTimer = 0



    
    pygame.display.update()
    clock.tick(60)