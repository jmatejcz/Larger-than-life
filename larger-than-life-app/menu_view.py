import numpy as np
import time
import pygame
import config
import game_view
import utils
import popups


def get_menu_state():
    return np.load(config.MENU_STATE_PATH)


def project_menu(screen, state):
    to_state = get_menu_state()
    utils.transition_states(screen, state, to_state)
    utils.update_visuals(screen=screen, state=state)
    pygame.display.update()


def run():
    # initialize game window and starting grid state
    pygame.init()
    game = utils.init_game()
    screen = pygame.display.set_mode((config.CELLS_X * config.SIZE_PX, config.CELLS_Y * config.SIZE_PX))
    state = get_menu_state()
    screen.fill(config.COLORS["BACKGROUND"])
    utils.update_visuals(screen=screen, state=state)

    pygame.display.flip()
    pygame.display.update()

    # main menu loop
    while True:
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # handle keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # start the game
                    game_view.run(screen=screen, state=state, game=game)
                    project_menu(screen, state)

                elif event.key == pygame.K_l:  # load starting state from file
                    path = popups.prompt_file()
                    if utils.is_path_not_empty(path):
                        to_state = np.load(path)
                        game_view.run(screen=screen, state=state, game=game, to_state=to_state)
                        project_menu(screen, state)

                elif event.key == pygame.K_r:  # open rules selection
                    underpop_lim, overpop_lim, birth_con, neighborhood_r = popups.select_rules()
                    underpop_lim, overpop_lim, birth_con, neighborhood_r = utils.verify_rules(underpop_lim,
                                                                                              overpop_lim,
                                                                                              birth_con,
                                                                                              neighborhood_r)
                    
                    utils.update_rules(game, underpop_lim, overpop_lim, birth_con, neighborhood_r)

                elif event.key == pygame.K_p:  # open presets selection
                    path = popups.select_preset()
                    if utils.is_path_not_empty(path):
                        to_state = np.load(path)
                        game_view.run(screen=screen, state=state, game=game, to_state=to_state)
                        project_menu(screen, state)

        screen.fill(config.COLORS["BACKGROUND"])
        time.sleep(config.APP_DELAY_SEC)
