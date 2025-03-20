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
        self.main_window = main_window

        # Definir la ruta de la carpeta y archivo de configuración
        config_folder = "config"
        config_file = os.path.join(config_folder, "config.json")

        try:
            # Crear la carpeta config si no existe
            Path(config_folder).mkdir(exist_ok=True)

            # Verificar si existe el archivo de configuración
            if not os.path.exists(config_file):
                print(f"Archivo de configuración no encontrado. Creando uno nuevo en: {config_file}")

                # Crear el archivo con la configuración por defecto
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(DEFAULT_CONFIG, f, indent=4)
            else:
                print(f"Cargando configuración existente desde: {config_file}")

                # Cargar la configuración existente
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)       
        except Exception as e:
            print(f"Error al manejar el archivo de configuración: {str(e)}")    



        #publish ConfigUpdated y hacer que se actualice en main window y en opcClient
        self.main_window.container_frame.container_settings.freq_entry.delete(0,'end')
        self.main_window.container_frame.container_settings.freq_entry.insert(0,10)
        
