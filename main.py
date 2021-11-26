import pygame
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (400, 400)

win = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Cellular Automata: Game of Life")

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()
