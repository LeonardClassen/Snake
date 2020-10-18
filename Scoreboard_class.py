import pygame


class Scoreboard():
    def __init__(self):
        self.lengthScores = []
        self.text = []
        self.font = pygame.font.SysFont('freescomicsans', 16)

    def update(self, players):
        self.text.clear()
        for [p_idx, player] in enumerate(players):
            print(p_idx, player.name)
            self.text.append(self.font.render(player.name+ ': ' + str(player.score), 1, [255, 255, 255]))

    def draw(self, world):
        for [text_idx, text] in enumerate(self.text):
            world.window.blit(text, (20, 20 + 15*text_idx))

