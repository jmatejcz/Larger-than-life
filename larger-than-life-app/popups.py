import tkinter
import tkinter.filedialog
from windows.rules_selection_window import RulesWindow


def prompt_file():
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def select_rules():
    window = RulesWindow()
    window.run()
    underpopulation_limit = window.underpopulation_limit
    overpopulation_limit = window.overpopulation_limit
    birth_condition = window.overpopulation_limit
    neighborhood_radius = window.neighborhood_radius
    return underpopulation_limit, overpopulation_limit, birth_condition, neighborhood_radius
