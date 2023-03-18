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
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

            Laser(laser_group,self.rect.midtop)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self,meteor_group,True):
            pygame.quit()
            sys.exit()

    def update(self):
        self.laser_timer()
        self.laser_shoot()
        self.input_position()
        self.meteor_collision()

# Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self,groups,pos):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 600

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self,meteor_group, True):
            self.kill()

    def update(self):
        self.pos += self.direction * self.speed *dt
        self.rect.topleft = (round(self.pos.x),round(self.pos.y))

        if self.rect.bottom < 0:
            self.kill()
        
        self.meteor_collision()

# Meteor class
class Meteor(pygame.sprite.Sprite):
    def __init__(self,groups,pos):
        super().__init__(groups)
        meteor_surf = pygame.image.load('../graphics/meteor.png').convert_alpha()
        
        # Randomizing the meteor size
        scale_factor = uniform(0.5,1.3)
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * scale_factor
        self.scaled_surf = pygame.transform.scale(meteor_surf,meteor_size)
        self.image = self.scaled_surf
        self.rect = self.image.get_rect(center = pos)


        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-1,1),1)
        self.speed = randint(200,400)

        # Rotation logic
        self.rotation = 0
        self.rotation_speed = randint(20,50)
    
    def rotate(self):
        self.rotation += self.rotation_speed * dt
        rotate_surf = pygame.transform.rotozoom(self.scaled_surf,self.rotation,1)
        self.image = rotate_surf
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def update(self):
        self.pos += self.direction * self.speed *dt
        self.rect.topleft = (round(self.pos.x),round(self.pos.y))

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
        
        self.rotate()
        

class Score:
    def __init__(self):
        self.font = pygame.font.Font('../graphics/subatomic.ttf',50)
    
    def display(self):
        text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(text, True, (255,255,255))  
        text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
        display_surface.blit(text_surf,text_rect)
        pygame.draw.rect(display_surface,(255,255,255), text_rect.inflate(30,30), width = 8, border_radius = 5)


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
meteor_group = pygame.sprite.Group()

# Ship sprite creation
ship = Ship(spaceship_group)

# Score
score = Score()


# Meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,300)

# Clock, I'll use to set a limit framerate
clock = pygame.time.Clock()

# Game loop
while True:
    # Delta time
    dt = clock.tick() / 1000
    # Events loop
    for event in pygame.event.get():
        # Close event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Meteor spawn
        if event.type == meteor_timer:
            meteor_y_pos = randint(-150,-50)
            meteor_x_pos = randint(-100,WINDOW_WIDTH + 100)
            meteor = Meteor(meteor_group,(meteor_x_pos,meteor_y_pos))

    # -- Update --
    spaceship_group.update()
    laser_group.update()
    meteor_group.update()

    # -- Drawing --
    # Show the background
    display_surface.blit(background_surf, (0,0))
    # Show Score
    score.display()
    # Show the ship
    spaceship_group.draw(display_surface)
    # Show the laser
    laser_group.draw(display_surface)
    # Show the meteor
    meteor_group.draw(display_surface)

    pygame.display.update()