import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT)

HEIGHT, WIDTH = 720, 480

# Player object - defined by extending Sprite class
class Player_Char(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_Char, self).__init__()
        self.surf = pygame.image.load("dove.png").convert_alpha()
        self.rect = self.surf.get_rect(
            center = (WIDTH/2 - 75, HEIGHT/2)
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
    
    # Keep player within screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT