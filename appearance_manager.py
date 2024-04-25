import customtkinter


class AppearanceManager:
    def __init__(self, sidebar_frame: customtkinter.CTkFrame):
        self.scaling_optionemenu = None
        self.scaling_label = None
        self.sidebar_frame = sidebar_frame

    def create_scaling_widgets(self):
        # Create widgets for UI scaling
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=13, column=0, columnspan=8, padx=20, pady=(0, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            corner_radius=15,
            anchor="center",
            font=customtkinter.CTkFont(family="Arial", size=14, weight="bold"),
            values=["100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(
            row=15, column=0, columnspan=8, padx=20, pady=(0, 10)
        )
        self.scaling_optionemenu.set("100%")  # Set default display value

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    @staticmethod
    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
