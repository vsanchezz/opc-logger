import customtkinter as ctk

# Importar componentes
from src.gui.components.side_frame          import SideFrame
from src.gui.components.status_frame        import StatusFrame
from src.gui.components.container_0_frame   import ContainerFrame
from src.gui.components.title_frame         import TitleFrame
from src.event_bus                          import EventBus
from src.gui.components.config_loader       import ConfigLoader

class MainWindow(ctk.CTk):
    def __init__(self, event_bus):
        super().__init__()

        # Event Bus
        self.event_bus = event_bus

        # Configuración básica
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.title("Data Logger")
        self.geometry("1000x700")
        self.minsize(800, 600)

        # Main Window event bus
        self.event_bus_mw = EventBus()

        # Crear widgets
        self.create_widgets()

        # Load configuration
        self.config_loader = ConfigLoader(self)

    def create_widgets(self):
        # Frame principal que contiene todo
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True)

        # Frame titulo
        self.title_frame = TitleFrame(self.main_container)
        self.title_frame.pack(side="top", fill="x")
        
        # Barra lateral
        self.sidebar = SideFrame(
            self.main_container,
            self.event_bus_mw,
            corner_radius = 0
        )
        self.sidebar.pack(side="left", fill="y")

        # Contenedor para los frames de contenido
        self.container_frame = ContainerFrame(
            self.main_container, 
            self.event_bus_mw,
            fg_color = 'transparent',
        )
        self.container_frame.pack(
            side="right", 
            fill="both", 
            expand=True,
        )

    # Barra de estado en la parte inferior  
        self.status_bar = StatusFrame(self)
        self.status_bar.pack(fill="x", side="bottom")