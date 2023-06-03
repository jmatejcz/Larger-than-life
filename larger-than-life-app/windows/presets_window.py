import customtkinter
from enum import Enum


class PresetPaths(Enum):
    GLIDER = 'windows/presets/glider.npy'
    ONE_O_ONE = 'windows/presets/one_o_one.npy'
    ACHIM_P16 = 'windows/presets/achim_p16.npy'


class PresetsWindow:
    def __init__(self):
        self.selected_preset = None

        self.app = customtkinter.CTk()
        self.app.geometry("400x250")
        self.app.title("Rules")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Presets:")
        label_1.pack(pady=10, padx=10)

        self.button_glider = customtkinter.CTkButton(master=frame_1, command=self.select_glider, text="Glider")
        self.button_glider.pack(pady=10, padx=10)

        self.button_one_o_one = customtkinter.CTkButton(master=frame_1, command=self.select_one_o_one, text="One O' One")
        self.button_one_o_one.pack(pady=10, padx=10)

        self.button_achim_p16 = customtkinter.CTkButton(master=frame_1, command=self.select_achim_p16, text="Achim's P16")
        self.button_achim_p16.pack(pady=10, padx=10)

    def select_glider(self):
        self.selected_preset = PresetPaths.GLIDER.value
        self.app.destroy()

    def select_one_o_one(self):
        self.selected_preset = PresetPaths.ONE_O_ONE.value
        self.app.destroy()

    def select_achim_p16(self):
        self.selected_preset = PresetPaths.ACHIM_P16.value
        self.app.destroy()

    def run(self):
        self.app.mainloop()
