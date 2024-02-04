import pygame
from sys import exit
from sys import stdout
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 50)

# ocean
ocean_surf = pygame.image.load('ocean/ocean.png').convert_alpha()
ocean_surf_pos = -700

# sky
sky_surf = pygame.image.load('sky/sky.png').convert_alpha()
sunset_surf = pygame.image.load('sky/sunset.png').convert_alpha()
magical_surf = pygame.image.load('sky/magical.png').convert_alpha()
daysLoggedIn = 0

# rod surfaces
castrod_surf = pygame.image.load('rods/castrod.png').convert_alpha()
uncastrod_surf = pygame.image.load('rods/uncastrod.png').convert_alpha()
precastrod_surf = pygame.image.load('rods/precastrod.png').convert_alpha()
semicastrod_surf = pygame.image.load('rods/semicastrod.png').convert_alpha()
space = False
spaceHold = 0

# rewards
crate1_surf = pygame.image.load('rewards/crate1.png').convert_alpha()
crate2_surf = pygame.image.load('rewards/crate2.png').convert_alpha()
common_surf = pygame.image.load('rewards/common.png').convert_alpha()
rare_surf = pygame.image.load('rewards/rare.png').convert_alpha()
superrare_surf = pygame.image.load('rewards/superrare.png').convert_alpha()
epic_surf = pygame.image.load('rewards/epic.png').convert_alpha()
Wahoo_surf = pygame.image.load('rewards/Wahoo.png').convert_alpha()

showFish = 0
caughtFish = random.choice([crate1_surf, crate2_surf, common_surf, rare_surf, superrare_surf, epic_surf, Wahoo_surf])



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
        elif self.rect.x >= 550 and self.rect.x <= 600:
            self.rect.x-=(self.speed-1)
            if self.inWater == False and self.prevInWater == True:
                print('caught')

                
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

    if stdout == "caught":
        showFish+=1


    if timer % random.randint(300, 400) == 0:
        fishies_group.add(Fishies(random.randint(0, 6)))


    
    # blit sky
    screen.blit(sky_surf, (0, 0))

    # blit ocean
    match daysLoggedIn:
        case 5:
            screen.blit(sunset_surf, (0, 0))
        case 10:
            screen.blit(magical_surf, (0, 0))
        case _:
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



    # blit reward
    if showFish != 0:
        screen.blit(caughtFish, (0, 0))
        showFish+=1
        if showFish > 200: 
            showFish = 0
            caughtFish = random.choice([crate1_surf, crate2_surf, common_surf, rare_surf, superrare_surf, epic_surf, Wahoo_surf])
    


    # # timer for debugging
    # timer1 = int(pygame.time.get_ticks() / 1000)
    # timer_surf = font.render(f'Seconds passed: {timer1}',False,(64,64,64))
    # screen.blit(timer_surf, (600, 100))
        

    timer+=1

    pygame.display.update()
    clock.tick(60)