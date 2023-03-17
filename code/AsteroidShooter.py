import pygame,sys
from random import randint,uniform

# Ship class
class Ship(pygame.sprite.Sprite):

    def __init__(self,groups):
        super().__init__(groups) # 1. we have to init the parent class
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()# 2. We need a surface -> image
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # Timer
        self.can_shoot = True
        self.shoot_time = None
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.laser_shoot()
        self.input_position()

# Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self,groups,pos):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)


# Inicialize all imported pygame modules
pygame.init()

# -- Window --
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')

# Background
background_surf = pygame.image.load('../graphics/background.png').convert()

# Sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
# Ship sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group,(300,300))

# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

# Game loop
while True:
    # Delta time
    dt = clock.tick(120) / 1000
    
    # Events loop
    for event in pygame.event.get():
        # Close event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # -- Update --
    spaceship_group.update()
    # -- Drawing --
    # Show the background
    display_surface.blit(background_surf, (0,0))
    # Show the ship
    spaceship_group.draw(display_surface)
    # Show the laser
    laser_group.draw(display_surface)

    pygame.display.update()