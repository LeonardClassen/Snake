import pygame
import random

def check_won_lost(players, world):
    winning_players = []
    loosing_list = []
    for player in players:
        if player.won:
            winning_players.append(player)
        if player.lost:
            loosing_list.append(player)

    if len(winning_players) > 0:
        win_sound = pygame.mixer.Sound('sounds/win_sound.flac')
        win_sound.play()
        world.window.fill((0, 0, 0))
        world.draw()
        font = pygame.font.SysFont('freescomicsans', 25)
        text = []
        colors = [[255, 255, 255], [0, 255, 0]]
        for k in range(1, 5):
            for color in colors:
                text.clear()
                for player in players:
                    if player.won:
                        text.append(font.render(player.name + ' won ' + '!', 1, color))
                for [text_idx, text_str] in enumerate(text):
                    world.window.blit(text_str, (world.width / 2 - 50, world.height / 2 + 25 * text_idx))
                pygame.display.update()
                pygame.time.wait(500)
        return False

    elif len(loosing_list) > 0:
        loose_sound_list = ['sounds/loose_sound1.wav', 'sounds/loose_sound2.ogg', 'sounds/loose_sound3.wav']
        loose_sound = pygame.mixer.Sound(random.choice(loose_sound_list))
        loose_sound.play()
        world.window.fill((0, 0, 0))
        world.draw()
        font = pygame.font.SysFont('freescomicsans', 25)
        text = []
        colors = [[255, 255, 255], [255, 0, 0]]
        for k in range(1, 5):
            for color in colors:
                text.clear()
                for player in players:
                    if player.lost:
                        text.append(font.render(player.name + ' lost ' + '!', 1, color))
                for [text_idx, text_str] in enumerate(text):
                    world.window.blit(text_str, (world.width / 2 - 50, world.height / 2 + 25 * text_idx))
                pygame.display.update()
                pygame.time.wait(500)

        return False

    else:
        return True