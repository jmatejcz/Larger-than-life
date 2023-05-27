import larger_than_life as ltl_core
import numpy as np
import time
from datetime import datetime
import pygame
import config
import utils


def calculate_next_state(state):
    # TODO: call rust for an update
    # updated_state = ltl_core.get_next_state(state)

    # stubbed game logic
    for row, col in np.ndindex(state.shape):
        r = np.random.uniform()
        if r > 0.99:
            state[row, col] = 1

    return state


def update_visuals(screen, state):
    # project the board
    for row, col in np.ndindex(state.shape):
        color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
        pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                         row * config.SIZE_PX,
                                         config.SIZE_PX - 1,
                                         config.SIZE_PX - 1))


def clear_state_animation(screen, state):
    while np.sum(state) > 0:
        for row, col in np.ndindex(state.shape):
            r = np.random.uniform()
            if r > 0.8:
                state[row, col] = 0
            color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
            pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                             row * config.SIZE_PX,
                                             config.SIZE_PX - 1,
                                             config.SIZE_PX - 1))
        pygame.display.update()
        time.sleep(config.DELAY_MS)
    return state


def run(screen, state, to_state=None):
    if to_state is None:
        to_state = utils.reset_state()
    state = utils.state_animation(screen, from_state=state, to_state=to_state)
    update_visuals(screen=screen, state=state)
    pygame.display.update()

    running = False
    # TODO: implement saving animation
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
                    update_visuals(screen=screen, state=state)
                    pygame.display.update()

                # save
                if event.key == pygame.K_s:
                    save_run = True
                    now = datetime.now()
                    dt_string = now.strftime(config.DATETIME_FORMAT)
                    np.save(f'runs/game_{dt_string}', state)

                # return to menu
                elif event.key == pygame.K_ESCAPE:
                    return

            # based on mouse input, change cell state
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                state_y = max(0, min(pos[1] // config.SIZE_PX, (config.CELLS_Y - 1)))
                state_x = max(0, min(pos[0] // config.SIZE_PX, (config.CELLS_X - 1)))
                current_state = state[state_y, state_x]
                state[state_y, state_x] = 0 if current_state == 1 else 1
                update_visuals(screen=screen, state=state)
                pygame.display.update()

        if running:
            state = calculate_next_state(state=state)
            update_visuals(screen=screen, state=state)
            pygame.display.update()

        screen.fill(config.COLORS["BACKGROUND"])
        time.sleep(config.DELAY_MS)
