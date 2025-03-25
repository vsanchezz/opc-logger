from src.event_bus          import EventBus
from src.gui.main_window    import MainWindow
from src.opc_client         import OpcClient

class MainApp:
    def __init__(self):
        self.event_bus      = EventBus()
        self.opc_client     = OpcClient(self.event_bus)
        self.main_window    = MainWindow(self.event_bus)