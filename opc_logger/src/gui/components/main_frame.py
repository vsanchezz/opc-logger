import customtkinter as ctk
from datetime import datetime
import time

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.logging_active = False

        # Panel de control en la parte superior
        self.control_panel = ctk.CTkFrame(self, corner_radius=0, fg_color ='gray10')
        self.control_panel.pack(side = 'bottom', fill="x", padx=(0,10), pady=0)

        # Botón de conexión
        self.connect_button = ctk.CTkButton(
            self.control_panel,
            text="Connect",
            command=self.toggle_connection,
            width=120
        )
        self.connect_button.pack(side="left", padx=10, pady=10)

        # Botón de inicio de logging
        self.start_button = ctk.CTkButton(
            self.control_panel,
            text="Start Logging",
            command=self.start_logging,
            state="disabled",
            width=120
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        # Botón de detención de logging
        self.stop_button = ctk.CTkButton(
            self.control_panel,
            text="Stop Logging",
            command=self.stop_logging,
            state="disabled",
            width=120
        )
        self.stop_button.pack(side="left", padx=10, pady=10)

        # Área de visualización de datos
        self.data_frame = ctk.CTkFrame(self, corner_radius=0, fg_color ='gray10')
        self.data_frame.pack(fill="both", expand=True, padx=(0,10), pady=00)

        # Etiqueta para el área de datos
        self.data_label = ctk.CTkLabel(
            self.data_frame,
            text="Collected Data:",
            anchor="w"
        )
        self.data_label.pack(anchor="w", padx=10, pady=5)

        # Área de texto para mostrar datos
        self.data_text = ctk.CTkTextbox(
            self.data_frame,
            wrap="none",
            font=("Consolas", 12)
        )
        self.data_text.pack(fill="both", expand=True, padx=10, pady=5)

        # Callbacks para eventos
        self.on_connection_change = None
        self.on_logging_start = None
        self.on_logging_stop = None

    def set_callbacks(self, on_connection_change=None, on_logging_start=None, on_logging_stop=None):
        """Establecer callbacks para eventos"""
        self.on_connection_change = on_connection_change
        self.on_logging_start = on_logging_start
        self.on_logging_stop = on_logging_stop

    def toggle_connection(self):
        """Alternar conexión al servidor OPC"""
        if self.on_connection_change:
            self.on_connection_change()

    def update_connection_state(self, state):
        """Actualizar estado de conexión en la UI"""
        if state == "Disconnected":
            self.connect_button.configure(text="Connect", state="normal")
            self.start_button.configure(state="disabled")

            # Si estaba registrando datos, detener
            if self.logging_active:
                self.stop_logging()
        elif state == "Connecting...":
            self.connect_button.configure(state="disabled")
        else:  # Connected
            self.connect_button.configure(text="Disconnect", state="normal")
            self.start_button.configure(state="normal")

    def start_logging(self):
        """Iniciar registro de datos"""
        self.logging_active = True
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")

        # Notificar a través del callback
        if self.on_logging_start:
            self.on_logging_start()

    def stop_logging(self):
        """Detener registro de datos"""
        self.logging_active = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

        # Notificar a través del callback
        if self.on_logging_stop:
            self.on_logging_stop()

    def add_data_entry(self, message):
        """Agregar entrada al área de datos"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"

        # Insertar al principio (más reciente arriba)
        self.data_text.insert("1.0", entry)

    def clear_data(self):
        """Limpiar el área de datos"""
        self.data_text.delete("1.0", "end")