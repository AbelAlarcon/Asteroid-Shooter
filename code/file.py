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

# Load the laser model
laser_surface = pygame.image.load('../graphics/laser.png').convert_alpha()
laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)

# Import text
font = pygame.font.Font('../graphics/subatomic.ttf',50)
text_surf = font.render('Space', True, 'white')
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOWN_HEIGHT - 50))


# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

while True:
    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # -- Update --
    laser_rect.y -= round(200 * dt)


    #  -- Drawing --
    # Set black main surface
    display_surface.fill((0,0,0))
    # Show the background
    display_surface.blit(background_surface,(0,0))
    # Display text
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30,30), width = 5, border_radius = 5)
    # Display laser
    display_surface.blit(laser_surface,laser_rect)
    # 3. Show the frame to the player (update the display surface)
    # Display ship on the main surface
    display_surface.blit(ship_surface,ship_rect)


    # Draw the final frame
    pygame.display.update()
