"""
PyGame Documentation - https://www.pygame.org/docs/
Icon attribution link  - <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>
PyGame Primer Guide - https://realpython.com/pygame-a-primer/
"""

# Import pygame moduel 
import pygame

# Importing local constants for direction keys, escape, etc for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Inialise pygame modules - required at start of pygame file
pygame.init()

# Screen dimensions defined as constant variables
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 480

# Creating the Screen / drawing the display window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))            # screen size set with tuple, 720x480 pixels
# Setting the Screen Title and Icon
pygame.display.set_caption("Flappy Imitation")
icon = pygame.image.load("dove.png")                   # load in dove.png and assing it to 'icon'.
pygame.display.set_icon(icon)

# Player object - defined by extedning Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP] or pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] or pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] or pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
    
    # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Instantiate player object
player = Player()

# Game Loop
running = True      # Bool control variable to keep game loop running
while running:      # Starts the event handler

    
    # Loop through every active event
    for event in pygame.event.get():
        # Did user click the window close button? If so, stop the loop
        if event.type == QUIT:
            running = False
        # Did user press a key?
        elif event.type == KEYDOWN:
            # Did user press Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
    
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite location based on user keypresses
    player.update(pressed_keys)

    # Fill the background with light blue to replicate the sky
    screen.fill((173, 216, 230))                        # takes tuple rgb colour value
    
    # blit() places top left corner of surface or at location given
    screen.blit(player.surf, player.rect)

    # Flip the display - updates entire screen with everything that has been drawn since last flip
    pygame.display.flip()

# Once loop is done - quit
pygame.quit()