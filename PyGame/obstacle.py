import pygame, random

SCREEN_HEIGHT, SCREEN_WIDTH = 720, 480

# Define Obstacle object by extending Sripte
# The surface drawn on the screen is now an attribute of 'obstacle'
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((50, random.randint(SCREEN_HEIGHT/2+128, SCREEN_HEIGHT+128)))
        self.surf.fill((0,128,0))
        # Rect is assigned random location on the screen on the right side, 20 to 100 pixels away
        # It will be somewhere between the bottom and top of screen
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 50,
                0
                )
            )
        # Assign how fast obstacle sprite will move across the screen
        self.speed = 2

# Move the sprite based on speed 
# Remove sprite when it passes the left edge of screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        # Check if the right side of rect has moved of screen, if so call kill to remove
        if self.rect.right < 0:
            self.kill()

# Create the bottom obstacle to mirror the top obstacle
class BottomObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(BottomObstacle, self).__init__()
        self.surf = pygame.Surface((50, random.randint(SCREEN_HEIGHT/2-128, SCREEN_HEIGHT+128)))
        self.surf.fill((0,128,0))
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 200,
                SCREEN_HEIGHT
            )
        )
        self.speed = 2

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()