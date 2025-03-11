import customtkinter as ctk

class ControlPanel(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.connect_button = ctk.CTkButton(
            self,
            text="Connect",
            command=self.toggle_connection,
            width=120
        )
        self.connect_button.pack(side="left", padx=10, pady=10)

        self.start_button = ctk.CTkButton(
            self,
            text="Start Logging",
            command=self.start_logging,
            state="disabled",
            width=120
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = ctk.CTkButton(
            self,
            text="Stop Logging",
            command=self.stop_logging,
            state="disabled",
            width=120
        )
        self.stop_button.pack(side="left", padx=10, pady=10)

    def toggle_connection(self):
        pass

    def start_logging(self):
        pass

    def stop_logging(self):
        pass
