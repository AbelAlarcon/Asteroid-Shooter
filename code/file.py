import pygame, sys
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def display_score():
    score_text = f'Score:{pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, 'white')
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOWN_HEIGHT - 50))
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30,30), width = 5, border_radius = 5)

def laser_timer(can_shoot,duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

def meteor_update(meteor_list, speed = 300):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect .top > WINDOWN_HEIGHT:
            meteor_list.remove(meteor_tuple)

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
laser_list = []

# Lase timer
can_shoot = True
shoot_time = None

# Import text
font = pygame.font.Font('../graphics/subatomic.ttf',50)

# Load the meteor model
meteor_surfece = pygame.image.load('../graphics/meteor.png').convert_alpha()
meteor_list = []

# Meteor time
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,400)

# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

while True:
    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            # Laser
            laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
            
            # Timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
        if event.type == meteor_timer:
            # Random postion
            x_pos = randint(-100,WINDOW_WIDTH +100)
            y_pos = randint(-100,-50)
            # Creating a rect
            meteor_rect = meteor_surfece.get_rect(center = (x_pos,y_pos))
            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5,0.5),1)
            
            meteor_list.append((meteor_rect,direction))

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # -- Update --
    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot,500)

    meteor_update(meteor_list)

    #  -- Drawing --
    # Set black main surface
    display_surface.fill((0,0,0))
    # Show the background
    display_surface.blit(background_surface,(0,0))
    # Display text
    display_score()
    # Display laser
    for rect in laser_list:
        display_surface.blit(laser_surface,rect)
    # Display meteor
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surfece,meteor_tuple[0])

    # Display ship on the main surface
    display_surface.blit(ship_surface,ship_rect)


    # Draw the final frame
    pygame.display.update()