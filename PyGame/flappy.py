"""
PyGame Documentation - https://www.pygame.org/docs/
PyGame Primer Guide - https://realpython.com/pygame-a-primer/
Icon attribution link  - <a href="https://www.flaticon.com/free-icons/bird" title="bird icons">Bird icons created by Freepik - Flaticon</a>
music credit - 'Flying Penguins' Streambeats (free open source music)
wingflap.mp3 - pixabay.com
chirp & game_over mp3 files - freesound.org
"""

# Import pygame moduel 
import pygame
import random
import player_char, obstacle, cloud, flap_func
# Importing local constants for direction keys, escape, etc for easier access to key coordinates
from pygame.locals import (K_ESCAPE,KEYDOWN,QUIT,)

# Inialise pygame modules - required at start of pygame file
pygame.init()
# Setup for sounds. No arguments passed, defaults used.
pygame.mixer.init()

# Screen dimensions defined as constant variables
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 480

# Creating the Screen / drawing the display window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))            # screen size set with tuple, 720x480 pixels
# Setting the Screen Title and Icon
pygame.display.set_caption("Flappy Imitation")
icon = pygame.image.load("dove.png")                                       # load in dove.png and assing it to 'icon'.
pygame.display.set_icon(icon)

# Sound
# Load music, play background music and set volume
music = pygame.mixer.music
music.load("music.wav")
music.play(loops=-1)
music.set_volume(0.5)
# Sound effects
game_over = pygame.mixer.Sound("game_over.wav")

# Create clock object to set frame rate
clock = pygame.time.Clock()

# Instantiate player object
player_character = player_char.Player_Char()

# Creating a custom event for creating a new obstacle
ADDOBSTACLE = pygame.USEREVENT + 1
# Timer calls ADDOBSTACLE event in specified milliseconds
pygame.time.set_timer(ADDOBSTACLE, 2500)

#Creating custom event for clouds
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 2000)

# Creating sprite groups to hold all obstacle sprites & another for all sprites
# Obstacle group to be used for collision dectection & position updates
# All sprites group to be used for rendering
obstacles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# New group to hold cloud sprites
clouds = pygame.sprite.Group()

# Game Loop
def main():
    running = True      # Bool control variable to keep game loop running
    while running:      # Starts the event handler

        # Fill the background with light blue to replicate the sky
        screen.fill((135, 206, 250))        # takes tuple rgb colour value

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
                # Create new obstacles and add them to sprite groups
                t_obstacle = obstacle.Obstacle()
                b_obstacle = obstacle.BottomObstacle()
                obstacles.add(t_obstacle, b_obstacle)
                all_sprites.add(t_obstacle, b_obstacle)
            # Add new cloud
            elif event.type == ADDCLOUD:
                newCloud = cloud.Cloud()
                clouds.add(newCloud)
                all_sprites.add(newCloud)
        
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite location based on user keypresses
        player_character.update(pressed_keys)
        # Update obstacle location / position
        obstacles.update()
        # Update clouds
        clouds.update()

        # blit() places top left corner of surface or at location given
        # Draw cloud sprites first before obstacles for the are in background
        for i in clouds:
            screen.blit(i.surf, i.rect)
        for i in obstacles:
            screen.blit(i.surf, i.rect)
        #blit player after everything else to enure sprite is visible
        screen.blit(player_character.surf, player_character.rect)
        
        #Check for collisions between obstacle and player
        if pygame.sprite.spritecollideany(player_character, obstacles):
            # If so, stop sounds and music, play game over sound
            music.stop()
            game_over.play(1)
            # And stop the game for 1000 milliseconds and end loop
            pygame.time.wait(1200)
            running = False

        #draw the getFPS function to coordinates 0,0 (top left)
        screen.blit(flap_func.getFPS(clock), (SCREEN_WIDTH-40,0))

        # Flip the display - updates entire screen with everything that has been drawn since last flip
        pygame.display.flip()
        # Set clock tick timer to draw at 60 frames per second
        clock.tick(60)

    # Once loop is done - quit
    pygame.quit()

if __name__ == "__main__":
    main()
