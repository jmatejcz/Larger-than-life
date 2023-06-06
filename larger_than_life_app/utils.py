from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import numpy as np
import time
import pygame
import config
import larger_than_life as ltl_core


def transition_states(screen: pygame.surface.Surface, from_state: np.ndarray, to_state: np.ndarray) -> np.ndarray:
    """Transitions from current board state to desired one

    :param screen: pygame surface to display on
    :type screen: pygame.surface.Surface
    :param from_state: current state
    :type from_state: np.ndarray
    :param to_state: desired state
    :type to_state: np.ndarray
    :return: new state
    :rtype: np.ndarray
    """
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


def update_visuals(screen: pygame.surface.Surface, state: np.ndarray):
    """Projects the board state onto screen

    :param screen: pygame surface to display on
    :type screen: pygame.surface.Surface
    :param state: board state to project
    :type state: np.ndarray
    """
    for row, col in np.ndindex(state.shape):
        color = config.COLORS["DEAD"] if state[row, col] == 0 else config.COLORS["ALIVE"]
        pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                         row * config.SIZE_PX,
                                         config.SIZE_PX - 1,
                                         config.SIZE_PX - 1))


def reset_state():
    """Get starting board state
    """
    return np.zeros((config.CELLS_Y, config.CELLS_X))


def get_date_time():
    """Get formmated datetime
    """
    now = datetime.now()
    return now.strftime(config.DATETIME_FORMAT)


def save_starting_state(state: np.ndarray, dt_string:str):
    """Saves the state

    :param state: board state
    :type state: np.ndarray
    :param dt_string: filename
    :type dt_string: str
    """
    np.save(f'runs/game_{dt_string}', state)


def save_animation(states: list, dt_string: str):
    """Saves the history of all states

    :param states: list of states, where every state is np.ndarray
    :type states: list
    :param dt_string: filename
    :type dt_string: str
    """
    matplotlib.use('agg')
    last_frame = min(len(states), config.MAX_ANIM_FRAMES)
    states = states[:last_frame]

    def update_plot(frame):
        plt.clf()  # Clear the previous plot
        plt.imshow(states[frame], cmap='viridis')  # Plot the current frame
        plt.title(f'Iteration: {frame + 1}')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_plot, frames=len(states), interval=60)
    ani.save('runs/game_' + dt_string + '.gif', writer='pillow')


def is_path_not_empty(path: str)-> bool:
    """Checks if path is not empty
    """
    if path is None or path == '':
        return False
    else:
        return True


def verify_rules(underpopulation_limit,
                 overpopulation_limit,
                 birth_con,
                 neighborhood_radius):
    """Verify if rules values are valid
    and convert to ints
    """
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


def init_game(underpopulation_limit: str | int = config.UNDERPOP_LIM,
              overpopulation_limit: str | int =config.OVERPOP_LIM,
              birth_con: str | int =config.BIRTH_CON,
              neighborhood_radius: str | int=config.NEIGHBORHOOD):
    """Initializes game using rust library

    :param underpopulation_limit: threshold of alive cells below which alive cell go dead, defaults to config.UNDERPOP_LIM
    :type underpopulation_limit: str | int
    :param overpopulation_limit: threshold of alive cells over which alive cell go dead, defaults to config.OVERPOP_LIM
    :type overpopulation_limit: str | int
    :param birth_con: number of alive cells which makes dead cell alive, defaults to config.BIRTH_CON
    :type birth_con: str | int
    :param neighborhood_radius: radius of neighborhood of a cell, defaults to config.NEIGHBORHOOD
    :type neighborhood_radius: str | int
    :return: game object from rust lib
    """
    return ltl_core.init_game(
        underpopulation_limit=int(underpopulation_limit),
        overpopulation_limit=int(overpopulation_limit),
        come_alive_condition=int(birth_con),
        neighborhood_range=int(neighborhood_radius),
        width=config.CELLS_Y,
        height=config.CELLS_X,
    )


