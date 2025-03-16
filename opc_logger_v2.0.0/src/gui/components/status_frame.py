import customtkinter as ctk
from datetime import datetime

class StatusFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, height=30, **kwargs)

        # Indicador de estado de conexión
        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Disconnected",
            text_color="red",
            font=("Arial", 12, "bold")
        )
        self.status_label.pack(side="left", padx=10)

        # Reloj en la barra de estado
        self.time_label = ctk.CTkLabel(
            self,
            text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            font=("Arial", 12)
        )
        self.time_label.pack(side="right", padx=10)

        # Iniciar actualización del reloj
        self.update_clock()

    def update_clock(self):
        """Actualiza el reloj en la barra de estado"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.configure(text=current_time)
        self.after(1000, self.update_clock)  # Actualizar cada segundo

    def update_connection_status(self, status):
        """Actualiza el estado de conexión"""
        self.status_label.configure(text=f"Status: {status}")

        # Cambiar color según estado
        if status == "Connected":
            self.status_label.configure(text_color="green")
        elif status == "Connecting...":
            self.status_label.configure(text_color="orange")
        else:  # Disconnected
            self.status_label.configure(text_color="red")