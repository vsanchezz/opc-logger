import customtkinter as ctk

from src.gui.components.container_1_main import ContainerMain
from src.gui.components.container_2_settings import ContainerSettings

class ContainerFrame(ctk.CTkFrame):
    def __init__(self, master, event_bus_mw, **kwargs):
        super().__init__(master, **kwargs)

        self.event_bus_mw = event_bus_mw
        self.event_bus_mw.subscribe("MainClicked", self.showMainFrame)
        self.event_bus_mw.subscribe("SettingsClicked", self.showSettingsFrame)


        self.ContainerMain = ContainerMain(self)
        self.ContainerSettings = ContainerSettings(self)

        self.showMainFrame({})
    
    def showMainFrame(self,data):
        self.ContainerSettings.pack_forget()
        self.ContainerMain.pack(fill='both', expand=True)
    
    def showSettingsFrame(self,data):
        self.ContainerMain.pack_forget()
        self.ContainerSettings.pack(fill='both', expand=True)
    