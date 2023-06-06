import threading
import numpy as np
import time
import pygame
import config
import utils
from typing import Optional


def run(screen: pygame.surface.Surface, state: np.ndarray, game, to_state: Optional[np.ndarray]=None):
    """Main funciton to run game

    :param screen: pygame surface to display on
    :type screen: pygame.surface.Surface
    :param state: board state
    :type state: np.ndarray
    :param game: game object coming from ltl_core Rust library
    :param to_state: change actual state to this state, defaults to None
    :type to_state: Optional[np.ndarray], optional
    """
    if to_state is None:
        to_state = utils.reset_state()
    state = utils.transition_states(
        screen, from_state=state, to_state=to_state)
    utils.update_visuals(screen=screen, state=state)
    pygame.display.update()
    datetime = utils.get_date_time()

    running = False
    save_run = False

    # main game loop
    while True:
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # keyboard
            elif event.type == pygame.KEYDOWN:

                # run / pause
                if event.key == pygame.K_SPACE:
                    running = not running
                    utils.update_visuals(screen=screen, state=state)
                    pygame.display.update()

                # save
                if event.key == pygame.K_s:
                    utils.save_starting_state(state, datetime)
                    utils.save_game_rules(game.get_rules(), datetime)
                    save_run = True

                # return to menu
                elif event.key == pygame.K_ESCAPE:
                    states_history = game.get_board_state_history()
                    if save_run and len(states_history) > 0:
                        threading.Thread(target=utils.save_animation, args=(states_history, datetime)).start()
                    return

            # based on mouse input, change cell state
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                state_y = max(
                    0, min(pos[1] // config.SIZE_PX, (config.CELLS_Y - 1)))
                state_x = max(
                    0, min(pos[0] // config.SIZE_PX, (config.CELLS_X - 1)))
                current_state = state[state_y, state_x]
                state[state_y, state_x] = 0 if current_state == 1 else 1
                utils.update_visuals(screen=screen, state=state)
                pygame.display.update()

        if running:
            state = np.array(game.next_generation(state))
            utils.update_visuals(screen=screen, state=state)
            pygame.display.update()

        screen.fill(config.COLORS["BACKGROUND"])
        if running:
            time.sleep(config.GAME_DELAY_SEC)
        else:
            time.sleep(config.APP_DELAY_SEC)
