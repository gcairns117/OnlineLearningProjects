"""
pygame module
https://realpython.com/lessons/basic-pygame-program/
"""

# Import and initailize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((600, 600))

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
    pygame.draw.circle(screen, (0, 128, 0), (300, 300), 50)    #aruguement for where to draw, rgb value colour, where centre will be, and radius of circle. 

    #Flip the display
    pygame.display.flip()

# once loop is dont - quit
pygame.quit()