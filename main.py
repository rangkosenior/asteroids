import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: # start of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit game loop
        screen.fill("black")
        pygame.display.flip()
        dt += clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()