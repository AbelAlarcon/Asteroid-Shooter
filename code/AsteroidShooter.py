import pygame,sys
from random import randint,uniform

pygame.init()

# -- Window --
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')




clock = pygame.time.Clock()
while True:
    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    # -- Drawing --
    display_surface.fill((0,0,0))

    pygame.display.update()