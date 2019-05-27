import pygame
from config import *


class City():
    def __init__(self, number, max_cities):
        self.pos = (number * SCREENSIZE[0] // (max_cities + 1), SCREENSIZE[1] - GROUND_LEVEL)   # set position of the cities
        self.color = CITY
        self.size = 10
        self.destroyed = False

    def draw(self, screen):
        if self.destroyed != True:
            return pygame.draw.circle(screen, self.color, self.pos, self.size)
    
    def update(self):
        pass
        # check here to see if city caught in explosion

    def set_destroyed(self, status):
        self.destroyed = status

    def get_pos(self):
        return self.pos
