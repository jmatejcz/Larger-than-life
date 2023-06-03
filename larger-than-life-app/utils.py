from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import time
import pygame
import config
import larger_than_life as ltl_core


def transition_states(screen, from_state, to_state):
    while not np.array_equal(from_state, to_state):
        for row, col in np.ndindex(from_state.shape):
            r = np.random.uniform()
            if r > 0.8:
                from_state[row, col] = to_state[row, col]
            color = config.COLORS["DEAD"] if from_state[row, col] == 0 else config.COLORS["ALIVE"]
            pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                             row * config.SIZE_PX,
                                             config.SIZE_PX - 1,
                                             config.SIZE_PX - 1))
        pygame.display.update()
        time.sleep(config.APP_DELAY_SEC)
    return from_state


def update_visuals(screen, state):
    # project the board
    for row, col in np.ndindex(state.shape):
        color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
        pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                         row * config.SIZE_PX,
                                         config.SIZE_PX - 1,
                                         config.SIZE_PX - 1))


def reset_state():
    return np.zeros((config.CELLS_Y, config.CELLS_X))


def get_date_time():
    now = datetime.now()
    return now.strftime(config.DATETIME_FORMAT)


def save_starting_state(state, dt_string):
    np.save(f'runs/game_{dt_string}', state)


def save_animation(states, dt_string):
    last_frame = min(len(states), config.MAX_ANIM_FRAMES)
    states = states[:last_frame]

    def update_plot(frame):
        plt.clf()  # Clear the previous plot
        plt.imshow(states[frame], cmap='viridis')  # Plot the current frame
        plt.title(f'Iteration: {frame + 1}')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_plot, frames=len(states), interval=60)
    ani.save('runs/game_' + dt_string + '.gif', writer='pillow')


def is_path_not_empty(path):
    if path is None or path == '':
        return False
    else:
        return True


def verify_rules(underpopulation_limit,
                 overpopulation_limit,
                 birth_con,
                 neighborhood_radius):
    if underpopulation_limit is None or not underpopulation_limit.isdigit():
        underpopulation_limit = config.UNDERPOP_LIM
    if overpopulation_limit is None or not overpopulation_limit.isdigit():
        overpopulation_limit = config.OVERPOP_LIM
    if birth_con is None or not birth_con.isdigit():
        birth_con = config.BIRTH_CON
    if neighborhood_radius is None or not neighborhood_radius.isdigit():
        neighborhood_radius = config.NEIGHBORHOOD
    return abs(int(underpopulation_limit)), \
        abs(int(overpopulation_limit)), \
        abs(int(birth_con)), \
        abs(int(neighborhood_radius))


def init_game(underpopulation_limit=config.UNDERPOP_LIM,
              overpopulation_limit=config.OVERPOP_LIM,
              birth_con=config.BIRTH_CON,
              neighborhood_radius=config.NEIGHBORHOOD):
    return ltl_core.init_game(
        underpopulation_limit=int(underpopulation_limit),
        overpopulation_limit=int(overpopulation_limit),
        come_alive_condition=int(birth_con),
        neighborhood_range=int(neighborhood_radius),
        width=config.CELLS_Y,
        height=config.CELLS_X,
    )


def update_rules(game,
                 underpopulation_limit=config.UNDERPOP_LIM,
                 overpopulation_limit=config.OVERPOP_LIM,
                 birth_con=config.BIRTH_CON,
                 neighborhood_radius=config.NEIGHBORHOOD):
    ltl_core.update_rules(game,
                          underpopulation_limit=int(underpopulation_limit),
                          overpopulation_limit=int(overpopulation_limit),
                          come_alive_condition=int(birth_con),
                          neighborhood_range=int(neighborhood_radius))
    return game
