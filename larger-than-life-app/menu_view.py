import numpy as np
import time
import pygame
import config
import game_view
import utils


def get_menu_state():
    return np.load(config.MENU_STATE_PATH)


def project_menu(screen, state):
    to_state = get_menu_state()
    utils.state_animation(screen, state, to_state)
    update_visuals(screen=screen, state=state)
    pygame.display.update()


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
    state = get_menu_state()
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
                if event.key == pygame.K_s:
                    game_view.run(screen, state)
                    project_menu(screen, state)

                elif event.key == pygame.K_l:
                    path = utils.prompt_file()
                    to_state = np.load(path)
                    game_view.run(screen, state, to_state)
                    project_menu(screen, state)

        screen.fill(config.COLORS["BACKGROUND"])
        time.sleep(config.DELAY_MS)
