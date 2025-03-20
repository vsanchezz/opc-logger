#from opcua import Client
import os
import json
import time

class OpcClient():
    def __init__(self, event_bus):
        
        self.event_bus = event_bus
        self.status = "Disconnected"
        self.ip = self.read_ip()

    
    def read_ip(self):
         # Definir la ruta de la carpeta y archivo de configuración
        config_folder = "config"
        config_file = os.path.join(config_folder, "config.json")

        with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        
        return config['server_ip'] + ':' + config['port']
        
    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
    def read_tags(self, tag_list):
        pass
    
    def browse_tags(self):
        pass

    def get_status(self):
        pass

    def hanle_error(self):
        pass
