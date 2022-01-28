"""
27/01/22
Icon attribution link  - <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>
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

# Creating the Scrren / drawing the display window
screen = pygame.display.set_mode((800,800))            # screen size set with tuple, 800x800 pixels
# Setting the Title and Icon
pygame.display.set_caption("Flappy Imitation")
icon = pygame.image.load("dove.png")                   # load in dove.png and assing it to 'icon'.
pygame.display.set_icon(icon)

# Game Loop (aka Main Loop)
running = True
while running:

    # Did user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the background with light blue for sky
    screen.fill((173, 216, 230))                        # takes tuple rgb colour value

    # Draw a solid green circle in the center
    pygame.draw.circle(screen, (0, 128, 0), (400, 400), 20)    #aruguement for where to draw, rgb value colour, where centre will be, and radius of circle. 

    # Flip the display
    pygame.display.flip()

# Once loop is done - quit
pygame.quit()