# Imports
import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Move the enemy downwards
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Define the Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        if size == 'small':
            self.image = pygame.transform.scale(pygame.image.load("coin.png"), (20, 20))
            self.value = 2
        elif size == 'average':
            self.image = pygame.transform.scale(pygame.image.load("coin.png"), (50, 50))
            self.value = 5  # Adjusted to +5 points for average sized coins
        elif size == 'big':
            self.image = pygame.transform.scale(pygame.image.load("coin.png"), (100, 100))
            self.value = 10  # Adjusted to +10 points for big sized coins
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Move the coin downwards
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # Move the player left or right
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  # Create a group for coins
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Adding a new User event for creating coins
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, random.randint(2000, 5000))  # Initial random interval for coin appearance

# Game Loop
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
            if SCORE >= 100:  # Check if player has reached 15 points
                SPEED += 1  # Increase speed by an additional amount
        if event.type == ADD_COIN:  # When the add coin event is triggered
            # Randomly determine the size of the coin
            coin_size = random.choice(['small', 'average', 'big'])
            new_coin = Coin(coin_size)  # Create a new coin instance
            coins.add(new_coin)  # Add the coin to the coins group
            all_sprites.add(new_coin)  # Add the coin to all sprites group
            pygame.time.set_timer(ADD_COIN, random.randint(2000, 5000))  # Reset timer for next coin appearance
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        # DISPLAYSURF.fill(RED)  # Commented out the line to change background color
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

        # Check for collision between player and coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
       SCORE += coin.value  # Add the value of the collected coin to the score


    # Show collected coins count in top right corner
    coins_text = font_small.render("Coins: " + str(SCORE), True, BLACK)
    coins_rect = coins_text.get_rect()
    coins_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coins_text, coins_rect)

    pygame.display.update()
    FramePerSec.tick(FPS)




