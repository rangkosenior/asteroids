import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK_RGB_SEQUENCE = (0,0,0)
    while True: # start of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK_RGB_SEQUENCE) # refresh. should be called last

if __name__ == "__main__":
    main()