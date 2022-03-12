import pygame

# Function to display FPS on screen
def getFPS(clock):
    fps_display = "FPS: " + str(int(clock.get_fps()))
    font = pygame.font.SysFont("Arial", 12)
    text = font.render(fps_display, 1, pygame.Color("black"))
    return text