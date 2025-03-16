from src.event_bus import EventBus
from src.gui.main_window import MainWindow

class MainApp:
    def __init__(self):
        self.EventBus = EventBus()
        self.MainWindow = MainWindow()