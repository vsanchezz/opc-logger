import customtkinter as ctk

class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(
            self,
            text="Data Logging",
            font=ctk.CTkFont(size=30, weight="bold")
        ).pack(pady=10)