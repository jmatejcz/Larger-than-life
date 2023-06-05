import customtkinter
from enum import Enum


class PresetPaths(Enum):
    GLIDER = 'windows/presets/glider.npy'
    ONE_O_ONE = 'windows/presets/one_o_one.npy'
    ACHIM_P16 = 'windows/presets/achim_p16.npy'


def presets_window():

    selected_preset = None

    def select_glider():
        selected_preset = PresetPaths.GLIDER.value
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x250")
    app.title("Rules")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Presets:")
    label_1.pack(pady=10, padx=10)

    button_glider = customtkinter.CTkButton(master=frame_1, command=select_glider, text="Glider")
    button_glider.pack(pady=10, padx=10)

    # button_one_o_one = customtkinter.CTkButton(master=frame_1, command=select_one_o_one, text="One O' One")
    # button_one_o_one.pack(pady=10, padx=10)
    #
    # button_achim_p16 = customtkinter.CTkButton(master=frame_1, command=select_achim_p16, text="Achim's P16")
    # button_achim_p16.pack(pady=10, padx=10)

    app.mainloop()

    return selected_preset


# def select_glider(selected_preset, app):
#     selected_preset = PresetPaths.GLIDER.value
#     app.destroy()
#
#
# def select_one_o_one(selected_preset, app):
#     selected_preset = PresetPaths.ONE_O_ONE.value
#     app.destroy()
#
#
# def select_achim_p16(selected_preset, app):
#     selected_preset = PresetPaths.ACHIM_P16.value
#     app.destroy()
