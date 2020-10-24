import pygame


class World():
    def __init__(self):
        self.run = True
        self.game_over = False
        self.clocktime = 100
        self.clocktime_increment = 0
        self.final_score = 4000
        self.block_size = 20
        self.level_size = 35
        self.level_wall = []
        self.wall_color = [200, 200, 200]
        self.width = self.level_size*self.block_size
        self.height = self.level_size*self.block_size
        self.window = pygame.display.set_mode((self.width, self.height))  # creates a "surface"
        pygame.display.set_caption('The World')
        pygame.display.update()

        '''
        # define the level
        # upper end
        for i in range(0, self.level_size):
            self.level_wall.append([i*self.block_size, 0])
        # right end
        for i in range(0, self.level_size):
            self.level_wall.append([(self.level_size-1) * self.block_size, i*self.block_size])
        # lower end
        for i in range(0, self.level_size):
            self.level_wall.append([(self.level_size-i) * self.block_size, (self.level_size-1) * self.block_size])
        # left end
        for i in range(0, self.level_size):
            self.level_wall.append([0, (self.level_size-i) * self.block_size])
        -> to slow to draw the map block by block, might be usefull for complex levels
        '''
    def draw(self):
        pygame.draw.rect(self.window, self.wall_color, (0, 0, self.block_size, self.level_size*self.block_size))
        pygame.draw.rect(self.window, self.wall_color, (0, 0, self.level_size*self.block_size, self.block_size))
        pygame.draw.rect(self.window, self.wall_color, ((self.level_size-1)*self.block_size, 0, self.block_size, self.level_size*self.block_size))
        pygame.draw.rect(self.window, self.wall_color, (0, (self.level_size-1)*self.block_size, self.level_size*self.block_size, self.block_size))

