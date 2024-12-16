import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    dt = 0

    while True: # start of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit game loop
        
        for updatable in updatables:
            updatable.update(dt)
        
        screen.fill("black")
        
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
        
        # limit fps to 60.  # dt is the amount of time that has poassed since the last frame was drawn
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()