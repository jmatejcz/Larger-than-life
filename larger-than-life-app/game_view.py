import larger_than_life as ltl_core
import threading
import numpy as np
import time
import pygame
import config
import utils


def calculate_next_state(game, state):
    state = ltl_core.get_next_gen_board(game, state)
    return np.array(state)


def run(screen, state, game, to_state=None):
    if to_state is None:
        to_state = utils.reset_state()
    state = utils.transition_states(
        screen, from_state=state, to_state=to_state)
    utils.update_visuals(screen=screen, state=state)
    pygame.display.update()
    datetime = utils.get_date_time()

    running = False
    save_run = False
    states_history = []

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
                    save_run = True

                # return to menu
                elif event.key == pygame.K_ESCAPE:
                    if save_run and len(states_history) > 0:
                        threading.Thread(target=utils.save_animation, args=(states_history, datetime)).start()
                        # utils.save_animation(states_history, datetime)
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
            states_history.append(np.copy(state))
            state = calculate_next_state(game=game, state=state)
            utils.update_visuals(screen=screen, state=state)
            pygame.display.update()

        screen.fill(config.COLORS["BACKGROUND"])
        if running:
            time.sleep(config.GAME_DELAY_SEC)
        else:
            time.sleep(config.APP_DELAY_SEC)
