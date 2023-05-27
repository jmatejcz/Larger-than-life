import numpy as np
import time
import pygame
import config
import game_view


def reset_state():
    return np.zeros((config.CELLS_Y, config.CELLS_X))


def update_visuals(screen, state):
    # project the board
    for row, col in np.ndindex(state.shape):
        color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
        pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                         row * config.SIZE_PX,
                                         config.SIZE_PX - 1,
                                         config.SIZE_PX - 1))


def run():
    # initialize game window and starting grid state
    pygame.init()
    screen = pygame.display.set_mode((config.CELLS_X * config.SIZE_PX, config.CELLS_Y * config.SIZE_PX))
    state = reset_state()
    screen.fill(config.COLORS["BACKGROUND"])
    update_visuals(screen=screen, state=state)

    pygame.display.flip()
    pygame.display.update()

    # main menu loop
    while True:
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # play
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_view.run(screen, state)
                    state = reset_state()
                    update_visuals(screen=screen, state=state)
                    pygame.display.update()

        screen.fill(config.COLORS["BACKGROUND"])
        time.sleep(config.DELAY_MS)
