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

# fishies (something is going to go terribly wrong)
class Fishies(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        match color:
            case 0:
                self.image = pygame.image.load('fishies/redfishies.png').convert_alpha() 
            case 1:
                self.image = pygame.image.load('fishies/orangefishies.png').convert_alpha()
            case 2:
                self.image = pygame.image.load('fishies/yellowfishies.png').convert_alpha()
            case 3:
                self.image = pygame.image.load('fishies/greenfishies.png').convert_alpha()
            case 4:
                self.image = pygame.image.load('fishies/bluefishies.png').convert_alpha()
            case 5:
                self.image = pygame.image.load('fishies/purplefishies.png').convert_alpha()
            case 6:
                self.image = pygame.image.load('fishies/pinkfishies.png').convert_alpha()

        
        y_pos = random.randint(540, 575)
        self.rect = self.image.get_rect(center = (0, y_pos))
        self.speed = random.randint(15, 30)/10
        self.inWater = False
        self.prevInWater = False

    def update(self):
        self.rect.x += self.speed

        # checks if rod is in water
        if space == True and spaceHold >= 90:
            self.inWater = True
        else:
            self.inWater = False

        self.destroy()
        self.prevInWater = self.inWater

    def destroy(self):
        if self.rect.x > 1280:
            self.kill()
        elif self.rect.x >= 525 and self.rect.x <= 625:
            self.rect.x-=(self.speed-1)
            if self.inWater == False and self.prevInWater == True:
                print("caught")
                self.kill()

fishies_group = pygame.sprite.Group()
timer = 0

        
if True:
    """
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
    """



def flip_a_coin():
    return random.randint(0, 1)


# ADD OBSTACLES
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


    if timer % random.randint(300, 400) == 0:
        fishies_group.add(Fishies(random.randint(0, 6)))


    
    # blit background
    screen.blit(sky_surf, (0, 0))
    screen.blit(ocean_surf, (ocean_surf_pos, 475))

    # blit fishies
    fishies_group.draw(screen)
    fishies_group.update()
    
    # blit ocean
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



    if True:
        """
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
        """

    # timer for debugging
    timer1 = int(pygame.time.get_ticks() / 1000)
    timer_surf = font.render(f'Seconds passed: {timer1}',False,(64,64,64))
    screen.blit(timer_surf, (600, 100))

    timer+=1

    # test, delete later
    pygame.draw.line(screen, "Red", (525, 0), (525, 720)) 
    pygame.draw.line(screen, "Red", (625, 0), (625, 720)) 
    
    pygame.display.update()
    clock.tick(60)