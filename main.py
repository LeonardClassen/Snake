# import pygame to create a fancy snake game
import pygame
pygame.init()



# import sounds
nom_sound = pygame.mixer.Sound('nom.ogg')

from World_class import World
from Collectable_class import Collectable
from Collectable_class import Coin
from Collectable_class import Supercoin
from Scoreboard_class import Scoreboard
from Snake_class import Snake


def show_player_lost(player_lost, world, pygame):
    #pygame.mixer.Sound.play(nom_sound)
        print('Player ' + str(player_lost.name)+' lost.')
        font = pygame.font.SysFont('freescomicsans', 25)
        text = font.render('Player ' + str(player_lost.name) + ' lost.', 1, [255, 255, 255])
        world.window.blit(text, (0, 0))
        pygame.display.update()


def check_collectable_collision(player, clbl):
    collision = False
    for bodypart in player.body:
        if abs(bodypart[0] - clbl.x) < (player.width+clbl.width)/2 and abs(bodypart[1] - clbl.y) < (player.height+clbl.height)/2:
            collision = True
    return collision

# ##### init the game
world = World()
players = []
collectables =[]
scoreboard = Scoreboard()
# set players
players.clear()
players.append(Snake('Player 1', 100, 100, 1, 10, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, [100, 100, 100]))
players.append(Snake('Player 2', 10, 200, 1,  10,pygame.K_a,    pygame.K_d,     pygame.K_w,  pygame.K_s,    [255, 0, 0]))
collectables.append(Coin(world))
clock_decrement_counter = 0

# ################################### Main Loop
run = True
while run:
    pygame.time.wait(world.clocktime)


    # check the event which are keys pressed etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if window is closed by clicking on X
            run = False  # exit the game

    # Check for keys getting presses & move snake
    keys = pygame.key.get_pressed()
    for player in players:
        player.move(keys)

    # After all players have calculated their next position based on keys - check collisions
    # 1. check collision with wall
    for player in players:
        if player.check_wall_collision(world):
            print(str(player.name + 'collided with wall.'))
            player.speed=0
            player.lost = True
            run = False

    # 2. check collision with own body
    for player in players:
        if player.check_body_collision():
            print(str(player.name + 'collided with own body.'))
            player.speed = 0
            player.lost = True
            run = False

    # 3. check collision with other bodys
    # should be checking if own body is effected
    for me in players:
        for other_player in players:
            if not (me is other_player):
                me.check_player_collision(other_player)

    # 4. check collision with meals
    for player in players:
        for collectable in collectables:
            if check_collectable_collision(player, collectable):
                print(str(player.name + 'ate meal.'))
                player.eat()
                collectables.remove(collectable)
                collectables.append(Coin(world))

    # Clear the world and redraw
    world.window.fill((0, 0, 0))
    world.draw()

    for player in players:
        player.draw(world.window)

    for collectable in collectables:
        collectable.draw(world.window)

    # Calculate and show new score
    for player in players:
        player.update_score()
    scoreboard.update(players)
    scoreboard.draw(world)

    # update the screen
    pygame.display.update()

# End of while loop / End of game
pygame.quit()

# meal that will be eaten by the snake
# class meal:
