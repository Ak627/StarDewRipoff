import pygame

class Timer:
    def __init__(self, duration, func = None):
        self.duration = duration
        self.func = func #code that happens once the time is done
        self.start_time = 0
        self.active = False
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
    def deactivate(self):
        self.active = False
        self.start_time = 0
    def update(self):
        current_time = pygame.time.get_ticks()
        #check if timer has run out
        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.func:# if there's something to run afterwards
                self.func() #run it!
