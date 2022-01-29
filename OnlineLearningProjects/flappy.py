"""
PyGame Documentation - https://www.pygame.org/docs/
Icon attribution link  - <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>
PyGame Tutorial - https://www.youtube.com/watch?v=FfWpgLFMI7w&t=964s
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

# Screen dimensions defined as constants
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 480

# Creating the Screen / drawing the display window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))            # screen size set with tuple, 720x480 pixels
# Setting the Title and Icon
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
# Instantiate player
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

    # Fill the background with light blue for sky
    screen.fill((173, 216, 230))                        # takes tuple rgb colour value

    # Create a Surface, pass a tuple containing length and width
    surf = pygame.Surface((50,50))
    # Give surface colour
    surf.fill((0,0,0))
    rect = surf.get_rect()
    
    # Draw surface onto the screen
    # Placed at centre by subtracting width & height of surf from size of screen and then dividing by 2
    # Required to find centre as blit() places top left corner of surf at location given
    screen.blit(player.surf, player.rect)
    screen.blit(surf, ((SCREEN_WIDTH - surf.get_width())/2,(SCREEN_HEIGHT - player.surf.get_height())/2))

    # Flip the display - updates entire screen with everything that has been drawn since last flip
    pygame.display.flip()

# Once loop is done - quit
pygame.quit()