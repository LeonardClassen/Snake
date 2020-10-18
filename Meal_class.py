import pygame
import random


class Collectable():
    def __init__(self, world):
        self.width = 10
        self.height = 10
        self.x = round(random.randint(self.width, world.width-2*self.width), 1)
        self.y = round(random.randint(self.height, world.height-2*self.height), 1)

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))


