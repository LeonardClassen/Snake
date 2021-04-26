while True:
    # import pygame to create a fancy snake game
    import pygame
    pygame.init()

    import random

    from World_class import World
    from Collectable_class import Collectable
    from Collectable_class import Coin
    from Collectable_class import Mouse
    from Collectable_class import Abdi
    from Scoreboard_class import Scoreboard
    from Snake_class import Snake
    from check_won_lost import check_won_lost


    def show_player_lost(player_lost, world, pygame):
        #pygame.mixer.Sound.play(nom_sound)
            print('Player ' + str(player_lost.name)+' lost.')
            font = pygame.font.SysFont('freescomicsans', 25)
            text = font.render('Player ' + str(player_lost.name) + ' lost.', 1, [255, 255, 255])
            world.window.blit(text, (0, 0))
            pygame.display.update()

    def check_collectable_collision(player, item):
        collision = False
        for bodypart in player.body:
            if abs(bodypart[0] - item.x) < (player.width+item.width)/2 and abs(bodypart[1] - item.y) < (player.height+item.height)/2:
                collision = True
        return collision

    # ##### init the game
    world = World()
    players = []
    collectables =[]
    scoreboard = Scoreboard(world)
    # set players
    players.clear()
    players.append(Snake('Player 1', 10*world.block_size, (world.level_size-5)*world.block_size, 1,  pygame.K_a,    pygame.K_d,     pygame.K_w,  pygame.K_s,    [255, 0, 255], world, 20))
    players.append(Snake('Player 2', 10*world.block_size, 5*world.block_size, 1, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, [255, 255, 0], world, 20))
    collectables.append(Mouse(world))
    clock_decrement_counter = 0

    # Main Loop
    run = True
    pause = False
    while run:
        pygame.time.wait(world.clocktime)

        # check if player has won/lost
        run = check_won_lost(players, world)

        # check the event which are keys pressed etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if window is closed by clicking on X
                run = False  # exit the game
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not pause:
            pause = True
        elif keys[pygame.K_SPACE] and pause:
            pause = False

        if pause:
            continue

        for player in players:
            player.move(keys)

        # After all players have calculated their next position based on keys - check collisions
        # 1. check collision with wall
        for player in players:
            if player.check_wall_collision(world):
                print(str(player.name + ' collided with wall.'))
                player.speed=0
                player.lost = True

        # 2. check collision with own body
        for player in players:
            if player.check_body_collision():
                print(str(player.name + ' collided with own body.'))
                player.speed = 0
                player.lost = True

        # 3. check collision with other bodys
        # should be checking if own body is effected
        for me in players:
            for other_player in players:
                if not (me is other_player):
                    me.check_player_collision(other_player)

        # 4. check collision with collectables
        for player in players:
            for collectable in collectables:
                if check_collectable_collision(player, collectable):
                    player.eat(collectable, collectables)

        # update collectables
        # if no coin is on the map
        if not any(isinstance(collectable, Coin) for collectable in collectables):
            if random.randint(0, 1000) < 30: # x% chance that coin will appear
                collectables.append(Coin(world))
        # if no mouse is on the map
        if not any(isinstance(collectable, Mouse) for collectable in collectables):
            collectables.append(Mouse(world))
        # if no abdi is on the map
        if not any(isinstance(collectable, Abdi) for collectable in collectables):
            if random.randint(0, 1000) < 7:  # x% chance that coin will appear
                collectables.append(Abdi(world))

        # update coins
        for collectable in collectables:
            if isinstance(collectable, Coin):
                collectable.life_time -= 1
                if collectable.life_time <= 0:
                    collectables.remove(collectable)

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

        scoreboard.update(players, world.final_score)
        scoreboard.draw(world)

        # update the screen
        pygame.display.update()

    # End of while loop / End of game
    pygame.time.wait(1)
    pygame.quit()

    # meal that will be eaten by the snake
    # class meal:
