import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True: # start of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit game loop
        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        # limit fps to 60
        dt = clock.tick(60) / 1000.0 # dt is the amount of time that has poassed since the last frame was drawn

if __name__ == "__main__":
    main()