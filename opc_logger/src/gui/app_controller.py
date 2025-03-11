import time
from datetime import datetime

class AppController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.connection_state = "Disconnected"
        self.logging_active = False
        self.current_frame = None

    def show_frame(self, frame_name):
        """Mostrar el frame seleccionado y ocultar los demás"""
        # Ocultar todos los frames
        for frame in self.main_window.frames.values():
            frame.pack_forget()

        # Mostrar el frame seleccionado
        self.main_window.frames[frame_name].pack(fill="both", expand=True)
        self.current_frame = frame_name

    def toggle_connection(self):
        """Alternar conexión al servidor OPC"""
        if self.connection_state == "Disconnected":
            # Simular conexión (aquí se conectaría al servidor OPC)
            self.connection_state = "Connecting..."
            self.main_window.status_bar.update_connection_status(self.connection_state)
            self.main_window.frames["main"].update_connection_state(self.connection_state)

            # Simular tiempo de conexión
            self.main_window.after(2000, self.complete_connection)
        else:
            # Desconectar
            self.connection_state = "Disconnected"
            self.main_window.status_bar.update_connection_status(self.connection_state)
            self.main_window.frames["main"].update_connection_state(self.connection_state)

            # Si estaba registrando datos, detener
            if self.logging_active:
                self.stop_logging()

    def complete_connection(self):
        """Completar la conexión (simulado)"""
        self.connection_state = "Connected"
        self.main_window.status_bar.update_connection_status(self.connection_state)
        self.main_window.frames["main"].update_connection_state(self.connection_state)

        # Agregar mensaje al área de datos
        self.main_window.frames["main"].add_data_entry("Connected to OPC server")

    def start_logging(self):
        """Iniciar registro de datos"""
        self.logging_active = True

        # Agregar mensaje al área de datos
        self.main_window.frames["main"].add_data_entry("Data logging started")

        # Simular recopilación de datos
        self.simulate_data_collection()

    def stop_logging(self):
        """Detener registro de datos"""
        self.logging_active = False

        # Agregar mensaje al área de datos
        self.main_window.frames["main"].add_data_entry("Data logging stopped")

    def simulate_data_collection(self):
        """Simular recopilación de datos (para demostración)"""
        if self.logging_active:
            # Generar datos simulados
            temperature = 25.0 + (time.time() % 5)
            pressure = 1013.25 + (time.time() % 10)

            # Agregar datos al área de visualización
            data_str = f"Temperature: {temperature:.2f}°C, Pressure: {pressure:.2f}hPa"
            self.main_window.frames["main"].add_data_entry(data_str)

            # Programar próxima recopilación
            self.main_window.after(5000, self.simulate_data_collection)  # Cada 5 segundos

    def save_configuration(self, server_address):
        """Guardar configuración"""
        # Aquí se guardaría la configuración en un archivo
        self.main_window.frames["main"].add_data_entry(f"Configuration saved. Server: {server_address}")