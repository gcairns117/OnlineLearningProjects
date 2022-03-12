import pygame, random
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 480

# Adding Background Images - using and image for sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert_alpha()
        # Starting position randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 80, SCREEN_WIDTH + 150),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
    # Move the cloud based on constant speed & remove cloud once it has passed left edge of screen
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()