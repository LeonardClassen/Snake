import pygame
import random

class Snake():
    def __init__(self, name, x, y, len, left_key, right_key, up_key, down_key, color, world, speed):
        self.name = name
        self.x = x
        self.y = y
        self.width = world.block_size
        self.height = world.block_size
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
        self.attack_mode = False
        self.lost = False
        self.won = False
        self.boing_sound = pygame.mixer.Sound('sounds/boing_sound.wav')
        self.attack_sounds = ['sounds/abdi_attack1.ogg', 'sounds/abdi_attack2.ogg']
        self.attacks = 0

    def move(self, keys):
        # move to new position
        moves = []
        if keys[self.keys_lrud[0]] and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
            moves.append('l')
        elif keys[self.keys_lrud[1]] and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
            moves.append('r')
        elif keys[self.keys_lrud[2]] and not self.direction == 'DOWN':
            self.direction = 'UP'
            moves.append('u')
        elif keys[self.keys_lrud[3]] and not self.direction == 'UP':
            self.direction = 'DOWN'
            moves.append('d')
        else:
            pass

        # move forward
        if self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed
        elif self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed
        else:
            print('** Direction error **')
        # update body
        if self.speed > 0:
            self.body.insert(0, [self.x, self.y])
            self.body = self.body[0:self.body_length]

    def eat(self, collectable, collectables):
        collectable.sound.play()
        self.body_length += collectable.value_food
        self.score += collectable.value
        self.attacks += collectable.value_attack

        collectables.remove(collectable)

    def draw(self, window):
        for bodypart in self.body:
            pygame.draw.rect(window, self.color, (bodypart[0], bodypart[1], self.width-2, self.height-2))

    def check_wall_collision(self, world):
        if self.x > world.width-self.width*2 or self.x < 0+self.width/2 or self.y > world.height-self.height*2 or self.y < 0+self.width/2:
            return True
        else:
            return False

    def check_body_collision(self):
        for i in range(1, len(self.body)):
            bodypart = self.body[i]
            if abs(bodypart[0] - self.x) < self.width and abs(bodypart[1] - self.y) < self.height:
                return True

    # This method checks if another player crossed own body
    def check_player_collision(self, other_player):
        for bp_idx in range(0, len(self.body)):
            if abs(self.body[bp_idx][0] - other_player.x) < self.width and abs(self.body[bp_idx][1] - other_player.y) < self.height:
                # if another player corsses the head: sound
                if bp_idx == 0:
                    print(str(other_player.name) + ' crossed ' + str(self.name) + "'s head at " + str([other_player.x, other_player.y]))
                    self.boing_sound.play()
                    self.body_length = 1
                    self.body = self.body[0:self.body_length]
                    break
                else:
                    print(str(other_player.name) + ' crossed ' + str(self.name) + "'s tail at " + str([other_player.x, other_player.y]))
                    # check if crossing players
                    if other_player.attacks > 0:
                        self.body_length = bp_idx
                        self.body = self.body[0:bp_idx]
                        attack_sound = pygame.mixer.Sound(random.choice(self.attack_sounds,1))
                        attack_sound.play()
                        other_player.attacks -= 1
                        break
                    else:
                        other_player.speed = 0
                        other_player.lost = True


    def update_score(self):
        self.score = self.score + self.body_length - 1
