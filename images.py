import pygame.image
import pygame
from main import window
window = pygame.display.set_mode((width, height))

def King_Kong():
    kong_image = pygame.image.load("images/gorilla.bmp")
    window.blit(kong_image, (300, 100))



