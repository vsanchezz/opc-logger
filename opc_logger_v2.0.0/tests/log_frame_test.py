import time
import random
from datetime import datetime
import customtkinter as ctk

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('/Users/victor/Downloads/OneDrive_1_17-3-2025/opc_logger_v2.0.0/src/gui/components')
sys.path.append('/Users/victor/Downloads/OneDrive_1_17-3-2025/opc_logger_v2.0.0/src')

from log_manager import LogManager
from log_frame import LogFrame

# Simulador de un sistema de eventos
class EventEmitter:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        """
        Registra un callback para un evento específico.
        """
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def publish(self, event_name, data):
        """
        Emite un evento y notifica a todos los callbacks registrados.
        """
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(data)

# Función para generar datos aleatorios para el evento NewReading
def generate_random_data():
    return {
        'GVL_var_bool': random.choice([True, False]),
        'GVL_var_int': random.randint(0, 100),
        'GVL_var_real': round(random.uniform(0, 100), 2),
        'GVL_var_string': random.choice(['Hello', 'World', 'Test', 'Random']),
        'GVL_var_array': [random.choice([True, False]) for _ in range(4)],
        'timestamp': datetime.now().isoformat()
    }

# Función para simular la publicación de eventos
def simulate_events(event_emitter, log_manager):
    for _ in range(50):  # Publicar 50 eventos
        data = generate_random_data()
        event_emitter.publish('NewReading', data)
        time.sleep(0.1)  # Esperar 0.1 segundos entre eventos (10 eventos por segundo)

# Configuración de la interfaz gráfica
def main():
    # Crear el sistema de eventos
    event_emitter = EventEmitter()

    # Crear la ventana principal
    root = ctk.CTk()
    root.geometry("800x600")
    root.title("Log Viewer")

    # Crear una instancia de LogManager
    log_manager = LogManager(event_emitter)

    # Crear una instancia de LogFrame
    log_frame = LogFrame(root, event_emitter)
    log_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Simular eventos en un hilo separado
    import threading
    threading.Thread(target=simulate_events, args=(event_emitter, log_manager), daemon=True).start()

    # Ejecutar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()