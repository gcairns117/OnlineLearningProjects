"""
27/01/22
"""
#import pygame moduel 
import pygame

#importing local constants for direction keys, escape, etc for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#inialise pygame modules
pygame.init()

#creating the drawing window
screen = pygame.display.set_mode((800,800))     #screen size set with tuple, 800x800 pixels

# Run until the user asks to quit
running = True
while running:

    # Did user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))    # takes tuple rgb colour value

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 128, 0), (400, 400), 20)    #aruguement for where to draw, rgb value colour, where centre will be, and radius of circle. 

    #Flip the display
    pygame.display.flip()

# once loop is dont - quit
pygame.quit()