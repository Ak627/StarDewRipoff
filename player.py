import pygame
from settings import *

class Player(pygame.sprite.Sprite): #this is a child class of pygames sprite class
    def __init__(self,pos,group):
        super().__init__(group) # this gives this class access to the functions inside the group class
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos) # set the position to be the center of the rect
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("up")
        if keys[pygame.K_DOWN]:
            print("down")
        if keys[pygame.K_RIGHT]:
            print("right")
        if keys[pygame.K_LEFT]:
            print("left")
    def update(self, dt):
        self.input()
