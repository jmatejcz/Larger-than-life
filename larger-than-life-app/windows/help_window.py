import customtkinter


class HelpWindow:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("400x400")
        self.app.title("Rules")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Help")
        label_1.pack(pady=10, padx=10)

        label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="On starting screen:")
        label_2.pack(pady=10, padx=10)

        label_3 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="S - start")
        label_3.pack()

        label_4 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="R - rules")
        label_4.pack()

        label_5 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="P - patterns")
        label_5.pack()

        label_6 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="L - load game")
        label_6.pack()

        label_7 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT,
                                         text="While in game:")
        label_7.pack(pady=10, padx=10)

        label_8 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="S - save the game")
        label_8.pack()

        self.button_ok = customtkinter.CTkButton(master=frame_1, command=self.save_callback, text="Ok")
        self.button_ok.pack(pady=10, padx=10)

    def save_callback(self):
        self.app.destroy()

    def run(self):
        self.app.mainloop()
