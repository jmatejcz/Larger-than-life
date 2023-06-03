import customtkinter
from enum import Enum


class PresetPaths(Enum):
    GLIDER = 'windows/presets/glider.npy'


class PresetsWindow:
    def __init__(self):
        self.selected_preset = None

        self.app = customtkinter.CTk()
        self.app.geometry("400x180")
        self.app.title("Rules")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Presets:")
        label_1.pack(pady=10, padx=10)

        self.button_glider = customtkinter.CTkButton(master=frame_1, command=self.select_glider, text="Glider")
        self.button_glider.pack(pady=10, padx=10)

    def select_glider(self):
        self.selected_preset = PresetPaths.GLIDER.value
        self.app.destroy()

    def run(self):
        self.app.mainloop()
