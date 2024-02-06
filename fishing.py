import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 70)

# ocean
ocean_surf = pygame.image.load('ocean/ocean.png').convert_alpha()
ocean_surf_pos = -700

# sky
sky_surf = pygame.image.load('sky/sky.png').convert_alpha()
sunset_surf = pygame.image.load('sky/sunset.png').convert_alpha()
magical_surf = pygame.image.load('sky/magical.png').convert_alpha()
daysLoggedIn = 5

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
def resetCaughtFish():
    caughtFish = random.choice([crate1_surf, crate2_surf, common_surf, rare_surf, superrare_surf, epic_surf, Wahoo_surf])
    return caughtFish
def resetDiscounts():
    discounts = random.choice([
    "10% discount",
    "5% discount",
    "5% discount",
    "2.5% discount",
    "2.5% discount",
    "2.5% discount",
    "free chips",
    "free chips",
    "free chips",
    "25% discount one item",
    "25% discount one item",
    "25% discount one item",
    "25% discount one item",
    "25% discount one item",
    "nothing",
    "nothing",
    "nothing",
    "rare fishing rod",
    "rare fishing rod",
    "rare fishing rod",
    "epic fishing rod",
    "epic fishing rod",
    "golden fishing rod",
])
    return discounts

caughtFish = resetCaughtFish()
discounts = resetDiscounts()


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
        self.speed = random.randint(20, 30)/10
        self.inWater = False
        self.prevInWater = False
        self.caught = False
        self.caught_time = False

        
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
        elif self.rect.x >= 500 and self.rect.x <= 625: # change these numbers to make it harder to catch
            self.rect.x-=(self.speed-1)
            if self.inWater == False and self.prevInWater == True:
                print("caught")
                self.caught = True
                self.caught_time = pygame.time.get_ticks()

                
                # self.kill()
    



fishies_group = pygame.sprite.Group()
timer = 200

        
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


    if timer % random.randint(150, 350) == 0:
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
    for fish in fishies_group:
        if fish.caught:
            elapsed_time = pygame.time.get_ticks() - fish.caught_time
            if elapsed_time < 2000 and not spaceHold:
                screen.blit(caughtFish, (680, 170))
                # "YOU CAUGHT A FISH!"
                # match statements hate me sooooo
                if caughtFish == crate1_surf:
                    rarity = "crate"
                elif caughtFish == crate2_surf:
                    rarity = "crate"
                elif caughtFish == common_surf:
                    rarity = "common"
                elif caughtFish == rare_surf:
                    rarity = "rare"
                elif caughtFish == superrare_surf:
                    rarity = "super rare"
                elif caughtFish == epic_surf:
                    rarity = "epic"
                elif caughtFish == Wahoo_surf:
                    rarity = "Wahoo"
                    discounts = "Free taco"
                
                    
                reward_surf = font.render(f"You caught a {rarity}!", False, (0, 0, 0))
                reward_rect = reward_surf.get_rect(center = (640, 50))
                discount_surf = font.render(f"Here's a {discounts}", False, (0, 0, 0))
                discount_rect = discount_surf.get_rect(center = (640, 150))
                screen.blit(reward_surf, reward_rect)
                screen.blit(discount_surf, discount_rect)
            elif spaceHold:
                elapsed_time = 0
                fish.caught = False
                fishies_group.empty()
                
            else: 
                caughtFish = resetCaughtFish()
                discounts = resetDiscounts()
                fishies_group.empty()
        




    # # timer for debugging
    # timer1 = int(pygame.time.get_ticks() / 1000)
    # timer_surf = font.render(f'Seconds passed: {timer1}',False,(64,64,64))
    # screen.blit(timer_surf, (600, 100))
        

    timer+=1

    pygame.display.update()
    clock.tick(60)