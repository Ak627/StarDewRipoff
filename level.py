import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        
        #gets a reference (address) to the currently set display surface
        self.display_surface = pygame.display.get_surface()
        
        #class "group" is part of pygame's sprite support. It is a class that manages a *list* of sprites
        self.all_sprites = pygame.sprite.Group()
        
        self.setup()#call the setup function
        
    def setup(self):
        self.player = Player((640, 360), self.all_sprites)
        
    def run(self, dt):
        print("run game")
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface) #a draw function from the group class
        self.all_sprites.update(dt) #another function from the group class
