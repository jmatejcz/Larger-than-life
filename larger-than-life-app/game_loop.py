import time

import larger_than_life as ltl_core
import numpy as np
import pygame
import config


def update_state(screen, state):
    # initialize dead grid for the next state
    # updated_state = np.zeros((state.shape[0], state.shape[1]))

    # TODO: call rust for an update
    # updated_state = ltl_core.get_next_state(state)

    # project the board
    for row, col in np.ndindex(state.shape):
        color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
        pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                         row * config.SIZE_PX,
                                         config.SIZE_PX - 1,
                                         config.SIZE_PX - 1))

    return state


def run():
    # initialize game window and starting grid state
    pygame.init()
    screen = pygame.display.set_mode((config.CELLS_X * config.SIZE_PX, config.CELLS_Y * config.SIZE_PX))
    state = np.zeros((config.CELLS_Y, config.CELLS_X))
    screen.fill(config.COLORS["BACKGROUND"])
    update_state(screen=screen, state=state)

    pygame.display.flip()
    pygame.display.update()
    running = False

    # main game loop
    while True:
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # run / pause
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update_state(screen=screen, state=state)
                    pygame.display.update()

            # based on user input, change cell state
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                state[pos[1] // config.SIZE_PX, pos[0] // config.SIZE_PX] = 1  # TODO: fix the division issue
                update_state(screen=screen, state=state)
                pygame.display.update()

        screen.fill(config.COLORS["BACKGROUND"])

        if running:
            state = update_state(screen=screen, state=state)
            pygame.display.update()

        time.sleep(config.DELAY_MS)
