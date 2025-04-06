from src.event_bus          import EventBus
from src.gui.main_window    import MainWindow
from src.opc_client         import OpcClient
from src.log_manager        import LogManager

class MainApp:
    def __init__(self):
        self.event_bus      = EventBus()
        self.opc_client     = OpcClient(self.event_bus)
        self.main_window    = MainWindow(self.event_bus)
        self.log_manager    = LogManager(self.event_bus)
