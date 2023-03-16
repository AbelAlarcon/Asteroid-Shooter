import pygame, sys

# Inicialize all imported pygame modules
pygame.init()

# -- Window --
WINDOW_WIDTH, WINDOWN_HEIGHT = 1280,720
# Set display size
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOWN_HEIGHT))
# Set 'Meteor shooter' in title bar
pygame.display.set_caption('Asteroid Shooter')


# -- Assets --
# Load the background
background_surface = pygame.image.load('../graphics/background.png').convert()

# Load the ship model
# (Add .convert() to improve performance... without this we would work with .png file)
ship_surface = pygame.image.load('../graphics/ship.png').convert_alpha()
x_ship,y_ship = WINDOW_WIDTH/2,WINDOWN_HEIGHT/2
ship_rect = ship_surface.get_rect(center = (x_ship,y_ship))

# Import text font.Font(font style, size)
font = pygame.font.Font('../graphics/subatomic.ttf',50)
# Creating surface of text font.render(text,antialiasing, color) and a rectangle to handle the position
text_surf = font.render('Space', True, 'white')
text_react = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOWN_HEIGHT - 50))

# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

while True:
    # 1. Input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            ship_rect.center = event.pos
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # framerate limit
    clock.tick(60)

    # 2. Updates
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
