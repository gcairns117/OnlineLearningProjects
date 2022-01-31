"""
PyGame Documentation - https://www.pygame.org/docs/
Icon attribution link  - <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>
PyGame Primer Guide - https://realpython.com/pygame-a-primer/
"""

# Import pygame moduel 
from platform import python_branch
import pygame
import random

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

# Create clock object to set frame rate
clock = pygame.time.Clock()
#fps display function
def getFPS():
    fps_display = "FPS: " + str(int(clock.get_fps()))
    font = pygame.font.SysFont("Arial", 12)
    text = font.render(fps_display, 1, pygame.Color("black"))
    return text
    
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
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT/2)
            )

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

# Define Obstacle object by extending Sripte
# The surface drawn on the screen is now an attribute of 'obstacle'
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((50, 30))
        self.surf.fill((0,0,0))
        # Rect is assigned random location on the screen on the right side, 20 to 100 pixels away
        # It will be somewhere between the bottom and top of screen
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        # Assign how fast obstacle sprite will move across the screen
        self.speed = random.randint(1, 5)

# Move the sprite based on speed 
# Remove sprite when it passes the left edge of screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        # Check if the right side of rect has moved of screen, if so call kill to remove
        if self.rect.right < 0:
            self.kill()

# Instantiate player object
player = Player()

# Creating a custom event for creating a new obstacle
ADDOBSTACLE = pygame.USEREVENT + 1
# Timer calls ADDOBSTACLE event in specified milliseconds
pygame.time.set_timer(ADDOBSTACLE, 1000)

# Creating sprite groups to hold all obstacle sprites & another for all sprites
# Obstacle group to be used for collision dectection & position updates
# All sprites group to be used for rendering
obstacles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game Loop
running = True      # Bool control variable to keep game loop running
while running:      # Starts the event handler

    # Fill the background with light blue to replicate the sky
    screen.fill((173, 216, 230))        # takes tuple rgb colour value

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
        # Add new obstacle
        elif event.type == ADDOBSTACLE:
            # Create a new obstacle and add it to sprite groups
            new_obstacle = Obstacle()
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)

    
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite location based on user keypresses
    player.update(pressed_keys)
    # Update obstacle location / position
    obstacles.update()

    # blit() places top left corner of surface or at location given
    # Draw all sprites
    for i in all_sprites:
        screen.blit(i.surf, i.rect)

    #draw the getFPS function to coordinates 0,0 (top left)
    screen.blit(getFPS(), (SCREEN_WIDTH-40,0))

    # Flip the display - updates entire screen with everything that has been drawn since last flip
    pygame.display.flip()
    # Set clock tick timer to draw at 60 frames per second
    clock.tick(60)

# Once loop is done - quit
pygame.quit()