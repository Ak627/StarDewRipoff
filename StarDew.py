import pygame
import sys
from settings import * #imports everything from the settings file we wrote
from level import Level#import the level file


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            dt = self.clock.tick()/1000#fps
            self.level.run(dt)
            pygame.display.update()
                
if __name__=='__main__':
    game = Game()
    game.run()

