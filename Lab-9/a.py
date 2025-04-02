#Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COUNT_COIN = 0  # Coin counts 

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-8/Photo/AnimatedStreet.png")

# Screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-8/Photo/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-8/Photo/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-8/Photo/i.jpg")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = random.randint(-100, -30)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

class Extra_coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-9/i (1).webp")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = random.randint(-100, -30)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

# Creating Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
EXTRA = Extra_coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

EX = pygame.sprite.Group()
EX.add(EXTRA)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(EXTRA)

# Speed Increase Event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Display Score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Display Collected Coins
    coin_score = font_small.render("Coins: " + str(COUNT_COIN), True, BLACK)
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 100, 10))

    # Move and Redraw all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision with Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:/Users/yrysb/Desktop/Labs/Lab-8/Sound/crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    # Check for collision with Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COUNT_COIN += 1
        SPEED += 0.2
        for coin in coins:
            coin.rect.top = random.randint(-100, -30)
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), coin.rect.top)

    if pygame.sprite.spritecollideany(P1, EX):
        c = 5
        COUNT_COIN += c
        SPEED += 0.2*c  
        for coin in EX:
            coin.rect.top = random.randint(-100, -30)
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), coin.rect.top)

    pygame.display.update()
    FramePerSec.tick(FPS)