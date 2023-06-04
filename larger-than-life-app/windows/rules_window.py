import customtkinter


class RulesWindow:
    def __init__(self):
        self.underpopulation_limit = None
        self.overpopulation_limit = None
        self.birth_condition = None
        self.neighborhood_radius = None

        self.app = customtkinter.CTk()
        self.app.geometry("400x400")
        self.app.title("Rules")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Game rules:")
        label_1.pack(pady=10, padx=10)

        self.entry_underpop_limit = customtkinter.CTkEntry(master=frame_1, placeholder_text="Underpopulation limit")
        self.entry_underpop_limit.pack(pady=10, padx=10)

        self.entry_overpop_limit = customtkinter.CTkEntry(master=frame_1, placeholder_text="Overpopulation limit")
        self.entry_overpop_limit.pack(pady=10, padx=10)

        self.entry_birth_condition = customtkinter.CTkEntry(master=frame_1, placeholder_text="Birth condition")
        self.entry_birth_condition.pack(pady=10, padx=10)

        self.entry_neighborhood_radius = customtkinter.CTkEntry(master=frame_1, placeholder_text="Neighborhood radius")
        self.entry_neighborhood_radius.pack(pady=10, padx=10)

        self.button_set_default = customtkinter.CTkButton(master=frame_1, command=self.set_default_callback,
                                                          text="Set default")
        self.button_set_default.pack(pady=10, padx=10)

        self.button_ok = customtkinter.CTkButton(master=frame_1, command=self.save_callback, text="Save")
        self.button_ok.pack(pady=10, padx=10)

    def set_default_callback(self):
        self.entry_underpop_limit.insert(0, 2)
        self.entry_overpop_limit.insert(0, 3)
        self.entry_birth_condition.insert(0, 3)
        self.entry_neighborhood_radius.insert(0, 1)

    def save_callback(self):
        self.underpopulation_limit = self.entry_underpop_limit.get()
        self.overpopulation_limit = self.entry_overpop_limit.get()
        self.birth_condition = self.entry_birth_condition.get()
        self.neighborhood_radius = self.entry_neighborhood_radius.get()
        self.app.destroy()

    def run(self):
        self.app.mainloop()
