from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import time
import pygame
import config
import tkinter
import tkinter.filedialog


def transition_states(screen, from_state, to_state):
    while not np.array_equal(from_state, to_state):
        for row, col in np.ndindex(from_state.shape):
            r = np.random.uniform()
            if r > 0.8:
                from_state[row, col] = to_state[row, col]
            color = config.COLORS["DEAD"] if from_state[row,
                                                        col] == 0 else config.COLORS["ALIVE"]
            pygame.draw.rect(screen, color, (col * config.SIZE_PX,
                                             row * config.SIZE_PX,
                                             config.SIZE_PX - 1,
                                             config.SIZE_PX - 1))
        pygame.display.update()
        time.sleep(config.DELAY_SEC)
    return from_state


def reset_state():
    return np.zeros((config.CELLS_Y, config.CELLS_X))


def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def save_game(states):
    now = datetime.now()
    dt_string = now.strftime(config.DATETIME_FORMAT)

    last_frame = min(len(states), config.MAX_ANIM_FRAMES)
    states = states[:last_frame]
    np.save(f'runs/game_{dt_string}', states[0])

    def update_plot(frame):
        plt.clf()  # Clear the previous plot
        plt.imshow(states[frame], cmap='viridis')  # Plot the current frame
        plt.title(f'Iteration: {frame + 1}')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_plot, frames=len(states), interval=60)
    ani.save('runs/game_' + dt_string + '.gif', writer='pillow')
