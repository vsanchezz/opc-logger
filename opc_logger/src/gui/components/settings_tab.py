import customtkinter as ctk

class SettingsTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.server_label = ctk.CTkLabel(
            self,
            text="OPC Server IP Address:",
            anchor="w"
        )
        self.server_label.pack(anchor="w", padx=10, pady=5)

        self.server_entry = ctk.CTkEntry(
            self,
            width=300
        )
        self.server_entry.pack(anchor="w", padx=10, pady=5)

        self.variables_label = ctk.CTkLabel(
            self,
            text="Select OPC Variables to Log:",
            anchor="w"
        )
        self.variables_label.pack(anchor="w", padx=10, pady=5)

        self.variables_container = ctk.CTkScrollableFrame(
            self,
            width=300,
            height=300
        )
        self.variables_container.pack(fill="both", expand=True, padx=10, pady=5)
