import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite): #this is a child class of pygames sprite class
    def __init__(self,pos,group):
        super().__init__(group) # this gives this class access to the functions inside the group class

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        #general setup
        self.image = self.animations[self.status][self.frame_index] #access the dictionary
        self.rect = self.image.get_rect(center = pos) #set the position to be the center of the rect
        #self.image = pygame.Surface((32,64))
        #self.image.fill('green')
        #self.rect = self.image.get_rect(center = pos) # set the position to be the center of the rect

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)# player, (x,y) position
        self.speed = 200

    def import_assets(self):
        self.animations = {'up':[], 'down':[], 'left':[], 'right':[],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                           'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                           'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[]}

        for animation in self.animations.keys():
            full_path = '../stardew-main/character/' + animation
            self.animations[animation]=import_folder(full_path)
        print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
          self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
          self.direction.x = 0

        #print(self.direction)
    def move(self, dt):
        if self.direction.magnitude() > 0:#can't normalize vectors with length of 0
            self.direction = self.direction.normalize()#normalize the vector
        #print(self.direction)
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
      
    def update(self, dt):
        self.input()
        self.move(dt)

