import numpy as np
import time
import pygame
import config
import tkinter
import tkinter.filedialog


def state_animation(screen, from_state, to_state):
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
        time.sleep(config.DELAY_MS)
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
