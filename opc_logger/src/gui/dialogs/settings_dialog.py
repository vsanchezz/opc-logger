import customtkinter as ctk

class SettingsDialog(ctk.CTkToplevel):
    def __init__(self, parent, config):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("500x400")
        self.resizable(False, False)

        self.config = config
        self.result = None

    def _on_cancel(self):
        pass

    def _on_save(self):
        pass
