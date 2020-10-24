import pygame


class Scoreboard():
    def __init__(self, world):
        self.lengthScores = []
        self.text = []
        self.font = pygame.font.SysFont('freescomicsans', int(round(world.block_size*1.5,1)))

    def update(self, players, final_score):
        self.text.clear()
        for [p_idx, player] in enumerate(players):
            #shown_score = final_score - player.score
            shown_score = player.score
            self.text.append(self.font.render(player.name + ': ' + str(shown_score) + ' | '+  str(player.attacks), 1, [255, 255, 255]))

        for player in players:
            if player.score >= final_score:
                player.won = True

    def draw(self, world):
        for [text_idx, text] in enumerate(self.text):
            world.window.blit(text, (world.block_size*1.5, world.block_size*1.5 + world.block_size*1.5*text_idx))

