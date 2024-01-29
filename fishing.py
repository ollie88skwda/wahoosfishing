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
redfishies_surf = pygame.image.load('fishies/redfishies.png').convert_alpha()
redfishies_rect = redfishies_surf.get_rect(midright = (0, 350))

orangefishies_surf = pygame.image.load('fishies/orangefishies.png').convert_alpha()
orangefishies_rect = orangefishies_surf.get_rect(midright = (0, 350))

yellowfishies_surf = pygame.image.load('fishies/yellowfishies.png').convert_alpha()
yellowfishies_rect = yellowfishies_surf.get_rect(midright = (0, 350))

greenfishies_surf = pygame.image.load('fishies/greenfishies.png').convert_alpha()
greenfishies_rect = greenfishies_surf.get_rect(midright = (0, 350))

bluefishies_surf = pygame.image.load('fishies/bluefishies.png').convert_alpha()
bluefishies_rect = bluefishies_surf.get_rect(midright = (0, 350))

purplefishies_surf = pygame.image.load('fishies/purplefishies.png').convert_alpha()
purplefishies_rect = purplefishies_surf.get_rect(midright = (0, 350))

pinkfishies_surf = pygame.image.load('fishies/pinkfishies.png').convert_alpha()
pinkfishies_rect = pinkfishies_surf.get_rect(midright = (0, 350))

allFishiesSurf = [redfishies_surf, orangefishies_surf, yellowfishies_surf, greenfishies_surf, 
                  bluefishies_surf, purplefishies_surf, pinkfishies_surf]
allFishiesRect = [redfishies_rect, orangefishies_rect, yellowfishies_rect, greenfishies_rect, 
                  bluefishies_rect, purplefishies_rect, pinkfishies_rect]
leftFishiesOnScreen = []
rightFishiesOnScreen = []
fishyResetTimer = 0

# timer for debugging



def flip_a_coin():
    return random.randint(0, 1)

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
    
    # add a fishy every 5 seconds
    if fishyResetTimer % 300 == 0:
        # change the last two numbers to better randomize the y-coord spawn
        # first val is the color, second val is y-coord
        done = False
        color = random.randint(0,6)
        if flip_a_coin():
            for i in range(len(leftFishiesOnScreen)):
                if color in leftFishiesOnScreen[i]:
                    done = True
                    break
                    
            if done == False: leftFishiesOnScreen.append([color, random.randint(405, 450)])
            
        else:
            for i in range(len(rightFishiesOnScreen)):
                if color in rightFishiesOnScreen[i]:
                    done = True
                    break
                    
            if done == False: rightFishiesOnScreen.append([color, random.randint(405, 450)])

    print(leftFishiesOnScreen)
    print(rightFishiesOnScreen)
    print()
    # blits all the fishies going left
    for i in leftFishiesOnScreen:
        if allFishiesRect[i[0]].x == 0:
            allFishiesRect[i[0]].x = 1280

        allFishiesRect[i[0]].x -=1
        allFishiesRect[i[0]].y = i[1] # y val is second item in subarr
        screen.blit(allFishiesSurf[i[0]], allFishiesRect[i[0]])
        if allFishiesRect[i[0]].right < 0:
            leftFishiesOnScreen.remove(i) # IF FISH START RANDOMLY DISAPPEARING ITS BECAUSE .remove() SUCKS
    
    # blits all the fishies going right
    for i in rightFishiesOnScreen:
        # if allFishiesRect[i[0]].x != 0:
        #     allFishiesRect[i[0]].x = 0

        allFishiesRect[i[0]].x +=1
        allFishiesRect[i[0]].y = i[1] # y val is second item in subarr
        screen.blit(allFishiesSurf[i[0]], allFishiesRect[i[0]])
        if allFishiesRect[i[0]].left > 1280:
            rightFishiesOnScreen.remove(i)


    fishyResetTimer+=1

    # timer for debugging
    timer = int(pygame.time.get_ticks() / 1000)
    timer_surf = font.render(f'Seconds passed: {timer}',False,(64,64,64))
    screen.blit(timer_surf, (600, 100))
    
    pygame.display.update()
    clock.tick(60)