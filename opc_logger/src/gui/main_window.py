import customtkinter as ctk

# Importar componentes
from src.gui.components.sidebar import Sidebar
from src.gui.components.status_bar import StatusBar
from src.gui.components.main_frame import MainFrame
from src.gui.components.settings_frame import SettingsFrame
from src.gui.components.title_frame import TitleFrame
from src.gui.app_controller import AppController

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración básica
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("OPC Data Logger")
        self.geometry("1000x700")
        self.minsize(800, 600)

        # Crear controlador de la aplicación
        self.controller = AppController(self)

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame principal que contiene todo
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame titulo
        self.title_frame = TitleFrame(self.main_container, fg_color = 'gray10')
        self.title_frame.pack(side="top", fill="x", padx=10, pady=10)
        
        # Barra lateral
        self.sidebar = Sidebar(
            self.main_container,
            show_frame_callback=self.controller.show_frame,
            corner_radius = 0
        )
        self.sidebar.pack(side="left", fill="y", padx=(10, 0), pady=0)

        # Contenedor para los frames de contenido
        self.content_container = ctk.CTkFrame(self.main_container)
        self.content_container.pack(side="left", fill="both", expand=True)

        # Crear frames para cada "pestaña"
        self.frames = {}

        # Frame principal
        self.frames["main"] = MainFrame(self.content_container, corner_radius = 0)
        self.frames["main"].set_callbacks(
            on_connection_change=self.controller.toggle_connection,
            on_logging_start=self.controller.start_logging,
            on_logging_stop=self.controller.stop_logging
        )

        # Frame de configuración
        self.frames["settings"] = SettingsFrame(self.content_container, corner_radius = 0)
        self.frames["settings"].set_callbacks(
            on_save_config=self.controller.save_configuration
        )

        # Mostrar el frame principal por defecto
        self.controller.show_frame("main")

        # Barra de estado en la parte inferior
        self.status_bar = StatusBar(self)
        self.status_bar.pack(fill="x", side="bottom", padx=10, pady=(0, 10))