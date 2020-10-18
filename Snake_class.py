import pygame


class Snake():
    def __init__(self, name, x, y, len, speed, left_key, right_key, up_key, down_key, color):
        self.name = name
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = speed
        self.body = [[x, y]]
        self.body_length = len
        for i in range(1, self.body_length):
            self.body.append([self.x-(i*self.width), y])
        self.direction = 'RIGHT'
        self.color = color
        self.original_color = color
        self.keys_lrud = [left_key, right_key, up_key, down_key]
        self.score = 0
        self.lost = False
        self.snack_sound = pygame.mixer.Sound('snack_sound.ogg')

    def move(self, keys):
        # move to new position
        if keys[self.keys_lrud[0]] and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if keys[self.keys_lrud[1]] and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if keys[self.keys_lrud[2]] and not self.direction == 'DOWN':
            self.direction = 'UP'
        if keys[self.keys_lrud[3]] and not self.direction == 'UP':
            self.direction = 'DOWN'
        # move forward
        if self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += + self.speed
        elif self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
        # update body
        if self.speed > 0:
            self.body.insert(0, [self.x, self.y])
            self.body = self.body[0:self.body_length]

    def eat(self):
        self.body_length += 1
        self.snack_sound.play()


    def draw(self, window):
        for bodypart in self.body:
            pygame.draw.rect(window, self.color, (bodypart[0], bodypart[1], self.width, self.height))

    def check_wall_collision(self, world):
        if self.x > world.width-self.width*2 or self.x < 0+self.width/2 or self.y > world.height-self.height*2 or self.y < 0+self.width/2 :
            return True
        else:
            return False

    def check_body_collision(self):
        for i in range(1, len(self.body)):
            bodypart = self.body[i]
            if abs(bodypart[0] - self.x) < self.width and abs(bodypart[1] - self.y) < self.height:
                return True

    def check_player_collision(self, other_player):
        for bp_idx in range(0, len(self.body)):
            if abs(self.body[bp_idx][0] - other_player.x) < self.width and abs(self.body[bp_idx][1] - other_player.y) < self.height:
                if bp_idx == 0:
                    print(str(other_player.name) + 'crossed' + str(self.name) + "'s head at" + str([other_player.x, other_player.y]))
                else:
                    print(str(other_player.name) + 'crossed' + str(self.name) + "'s tail at " + str([other_player.x, other_player.y]))
                    self.body_length = bp_idx
                    self.body = self.body[0:bp_idx]
                    break

    def update_score(self):
        self.score = self.score + self.body_length
