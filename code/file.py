import pygame, sys

# Inicialize all imported pygame modules
pygame.init()

# -- Window --
WINDOW_WIDTH, WINDOWN_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOWN_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')


# -- Assets --
# Load the background
background_surface = pygame.image.load('../graphics/background.png').convert()

# Load the ship model
ship_surface = pygame.image.load('../graphics/ship.png').convert_alpha()
x_ship,y_ship = WINDOW_WIDTH/2,WINDOWN_HEIGHT/2
ship_rect = ship_surface.get_rect(center = (x_ship,y_ship))

# Import text
font = pygame.font.Font('../graphics/subatomic.ttf',50)
text_surf = font.render('Space', True, 'white')
text_react = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOWN_HEIGHT - 50))

# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # Set black main surface
    display_surface.fill((0,0,0))
    # Show the background
    display_surface.blit(background_surface,(0,0))
    # Display ship on the main surface
    display_surface.blit(ship_surface,ship_rect)
    # Display text
    display_surface.blit(text_surf,text_react)
    
    # 3. Show the frame to the player (update the display surface)
    pygame.display.update()
