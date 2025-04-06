import time
import random
from datetime import datetime
import os
import sys

# Agregar el directorio src al path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, "src"))
sys.path.append(os.path.join(project_root, "src\gui\components"))

from log_manager import LogManager  # Asegúrate de que LogManager esté en un archivo llamado log_manager.py

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

# Crear una instancia del sistema de eventos
event_emitter = EventEmitter()

# Crear una instancia de LogManager
log_manager = LogManager(event_emitter)

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

# Publicar el evento NewReading cada segundo durante 20 iteraciones
for i in range(10):
    data = generate_random_data()
    print(f"Publicando evento NewReading: {data}")
    event_emitter.publish('NewReading', data)
    time.sleep(1)  # Esperar 1 segundo

# Imprimir el log actual
print("\nLog actual:")
log_manager.print_log()

# Exportar el log a un archivo CSV
log_manager.export_to_csv('test_logs.csv')
print("\nLog exportado a 'test_logs.csv'.")