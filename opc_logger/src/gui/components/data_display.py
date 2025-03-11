import customtkinter as ctk
from datetime import datetime

class DataDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.data_label = ctk.CTkLabel(
            self,
            text="Collected Data (newest at top):",
            anchor="w"
        )
        self.data_label.pack(anchor="w", padx=10, pady=5)

        self.data_text = ctk.CTkTextbox(
            self,
            wrap="none",
            font=("Consolas", 12)
        )
        self.data_text.pack(fill="both", expand=True, padx=10, pady=5)

    def add_data_entry(self, data):
        pass

    def clear_data(self):
        pass
