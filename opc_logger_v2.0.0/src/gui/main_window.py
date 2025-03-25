import customtkinter as ctk
from functools import partial

# Importar componentes
from src.gui.components.side_frame          import SideFrame
from src.gui.components.status_frame        import StatusFrame
from src.gui.components.container_0_frame   import ContainerFrame
from src.gui.components.title_frame         import TitleFrame
from src.event_bus                          import EventBus
from src.gui.components.config_loader       import ConfigLoader
from src.gui.components.message_frame       import MessageFrame

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
        # echo events from event_bus_mw to event_bus
        self.setup_echoes_from_mw()

        # echo events from event_bus to event_bus_mw
        self.setup_echoes_to_mw()

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
        
        # Frame central
        self.central_frame = ctk.CTkFrame(self.main_container)
        self.central_frame.pack(side = 'top', fill ='both',expand = True)
        
        # Barra lateral
        self.sidebar = SideFrame(
            self.central_frame,
            self.event_bus_mw,
            corner_radius = 0,
            fg_color = 'transparent'
        )
        self.sidebar.pack(side="left", fill="y")

        # Contenedor para los frames de contenido
        self.container_frame = ContainerFrame(
            self.central_frame, 
            self.event_bus_mw,
            fg_color = 'transparent',
        )
        self.container_frame.pack(
            side="right", 
            fill="both", 
            expand=True,
        )
    
    # Frame inferior
        self.inferior_frame = ctk.CTkFrame(self.main_container, fg_color='white')
        self.inferior_frame.pack(side = 'top', fill = 'x')

    # Barra de estado en la parte inferior  
        self.status_frame = StatusFrame(self.inferior_frame, self.event_bus_mw, corner_radius=0, fg_color = 'transparent')
        self.status_frame.pack(fill="both", side = 'left', expand = True)
        
    # Message frame 
        self.message_frame = MessageFrame(
            self.inferior_frame, 
            self.event_bus_mw, 
            width = 500, 
            height = 30,
            fg_color = 'transparent'
            )
        self.message_frame.pack_propagate(False)
        self.message_frame.pack(side="right")
    

    # echo from event_bus_mw to event_bus
    def setup_echoes_from_mw(self):
        events_to_echo = [
            'ConfigUpdated', 
            'SaveConfiguration', 
            'Connect',
            'Disconnect',
            'StartLogging',
            'StopLogging'
            ]
        for event in events_to_echo:
            # Esto crea una nueva función que es equivalente a:
            # lambda *args: self.event_bus.publish('ConfigUpdated', *args)
            echo_func = partial(self.event_bus.publish, event)
            self.event_bus_mw.subscribe(event, echo_func)
    
    # echo from event_bus to event_bus_mw
    def setup_echoes_to_mw(self):
        events_to_echo = [
            'StatusUpdate'
            ]
        for event in events_to_echo:
            # Esto crea una nueva función que es equivalente a:
            # lambda *args: self.event_bus.publish('ConfigUpdated', *args)
            echo_func = partial(self.event_bus_mw.publish, event)
            self.event_bus.subscribe(event, echo_func)
     