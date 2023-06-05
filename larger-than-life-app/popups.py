import tkinter
import tkinter.filedialog
from windows.rules_window import RulesWindow
from windows.presets_window import PresetsWindow


def prompt_file() -> str:
    """prompt window to chose file

    :return: filename
    :rtype: str
    """
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def select_rules()->tuple:
    """Get rules from rules prompt window

    :return: tuple of ints values, representing rules
    :rtype: tuple
    """
    window = RulesWindow()
    window.run()
    underpopulation_limit = window.underpopulation_limit
    overpopulation_limit = window.overpopulation_limit
    birth_condition = window.overpopulation_limit
    neighborhood_radius = window.neighborhood_radius
    return underpopulation_limit, overpopulation_limit, birth_condition, neighborhood_radius


def select_preset() -> str:
    """Get preset from preset prompt window

    :return: preset name
    :rtype: str
    """
    window = PresetsWindow()
    window.run()
    selected_preset = window.selected_preset
    print(type(selected_preset))
    return selected_preset
