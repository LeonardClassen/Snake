import pygame
import random


class Collectable:
    def __init__(self, world):
        self.width = world.block_size
        self.height = world.block_size
        self.x = round(random.randint(2*self.width, world.width-3*self.width), world.block_size)
        self.y = round(random.randint(2*self.height, world.height-3*self.height), world.block_size)
        self.value = 100
        self.nutrient = 1
        self.value_attack = 0
        self.value_food = 0
        self.value_score = 0

    def draw(self, window):
        if self.image:
            window.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))


class Coin(Collectable):
    def __init__(self, world):
        super().__init__(world)
        self.image = pygame.image.load('pics/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (world.block_size, world.block_size))
        self.value_score = 100
        self.sound = pygame.mixer.Sound('sounds/coin_sound.ogg')
        self.life_time = (1000/world.clocktime) * 3 # lebt 10 Sekunden


class Mouse(Collectable):
    def __init__(self, world):
        super().__init__(world)
        self.image = pygame.image.load('pics/mouse.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (world.block_size, world.block_size))
        self.value_food = 1
        self.sound = pygame.mixer.Sound('sounds/mouse_sound.ogg')


class Abdi(Collectable):
    def __init__(self, world):
        super().__init__(world)
        self.image = pygame.image.load('pics/abdi.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (world.block_size, world.block_size))
        self.value_attack = 1
        self.sound = pygame.mixer.Sound('sounds/abdi1.ogg')



