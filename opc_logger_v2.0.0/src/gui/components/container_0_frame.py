import customtkinter as ctk

from src.gui.components.container_1_main import ContainerMain

class ContainerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.ContainerMain = ContainerMain(self)
        self.ContainerMain.pack(fill='both')

    