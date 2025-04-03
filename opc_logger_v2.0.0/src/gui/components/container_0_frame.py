import customtkinter as ctk

from src.gui.components.container_1_main import ContainerMain
from src.gui.components.container_2_settings import ContainerSettings
from src.gui.components.container_3_monitor import ContainerMonitor

class ContainerFrame(ctk.CTkFrame):
    def __init__(self, master, event_bus_mw, **kwargs):
        super().__init__(master, **kwargs)

        self.event_bus_mw = event_bus_mw
        self.event_bus_mw.subscribe("MainClicked", self.showMainFrame)
        self.event_bus_mw.subscribe("SettingsClicked", self.showSettingsFrame)
        self.event_bus_mw.subscribe("MonitorClicked", self.showMonitorFrame)

        self.container_main = ContainerMain(self)
        
        self.container_settings = ContainerSettings(self)
        self.event_bus_mw.subscribe('ConfigUpdated', self.container_settings.update_config)

        self.container_monitor = ContainerMonitor(self)

        self.showMainFrame({})
    
    def showMainFrame(self,data):
        self.container_settings.pack_forget()
        self.container_monitor.pack_forget()
        
        self.container_main.pack(fill='both', expand=True)
    
    def showSettingsFrame(self,data):
        self.container_main.pack_forget()
        self.container_monitor.pack_forget()

        self.container_settings.pack(fill='both', expand=True)
    
    def showMonitorFrame(self,data):
        self.container_main.pack_forget()
        self.container_settings.pack_forget()

        self.container_monitor.pack(fill='both', expand=True)

    