import customtkinter as ctk

class ConnectionDialog(ctk.CTkToplevel):
    def __init__(self, parent, initial_url="", initial_username="", initial_password=""):
        super().__init__(parent)

        self.title("OPC Server Connection")
        self.geometry("400x300")
        self.resizable(False, False)

        self.result = None

    def _on_cancel(self):
        pass

    def _on_connect(self):
        pass
