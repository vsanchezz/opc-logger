import os
import json
from pathlib import Path

DEFAULT_CONFIG = {
    'server_ip'     : '192.168.10.80',
    'port'          : '4840',
    'logging_freq'  : 1,
    'output_folder' : 'data',
    'password'      : '',
    
}

class ConfigLoader():
    def __init__(self, main_window):
        self.event_bus_mw = main_window.event_bus_mw

        # Definir la ruta de la carpeta y archivo de configuración
        self.config_folder = "config"
        self.config_file = os.path.join(self.config_folder, "config.json")

        self.config = DEFAULT_CONFIG

        try:
            # Crear la carpeta config si no existe
            Path(self.config_folder).mkdir(exist_ok=True)

            # Verificar si existe el archivo de configuración
            if not os.path.exists(self.config_file):
                print(f"Archivo de configuración no encontrado. Creando uno nuevo en: {self.config_file}")
                
                # Crear el archivo con la configuración por defecto
                with open(self.config_file, 'w', encoding='utf-8') as f:
                    json.dump(DEFAULT_CONFIG, f, indent=4)
            else:
                print(f"Cargando configuración existente desde: {self.config_file}")

                # Cargar la configuración existente
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)       
        except Exception as e:
            print(f"Error al manejar el archivo de configuración: {str(e)}")    


        self.event_bus_mw.publish("ConfigUpdated",self.config)

        self.event_bus_mw.subscribe('SaveConfiguration',self.save_configuracion)
    
    def save_configuracion(self, config):
        try:
            # Primero leemos la configuración actual
            with open(self.config_file, 'r', encoding='utf-8') as f:
                current_config = json.load(f)

            # Actualizamos los campos específicos
            current_config['server_ip'] = config['server_ip']
            current_config['logging_freq'] = config['logging_freq']

            # Escribimos la configuración actualizada al archivo
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(current_config, f, indent=4)

            print("Configuración guardada exitosamente")

            # Opcionalmente, puedes publicar un evento para notificar que la configuración se actualizó
            self.event_bus_mw.publish("ConfigUpdated", current_config)

        except Exception as e:
            print(f"Error al guardar la configuración: {str(e)}")

