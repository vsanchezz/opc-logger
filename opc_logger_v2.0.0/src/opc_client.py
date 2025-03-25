#from opcua import Client
import os
import json
import time

class OpcClient():
    def __init__(self, event_bus):
        
        self.event_bus = event_bus
        self.status = "Disconnected"
        self.ip = None
        self.logging_freq = None

        # suscribe to events
        self.event_bus.subscribe('ConfigUpdated', self.update_config)
        self.event_bus.subscribe('Connect', self.connect)
        self.event_bus.subscribe('Disconnect', self.disconnect)
        self.event_bus.subscribe('StartLogging',self.start_logging)
        self.event_bus.subscribe('StopLogging',self.stop_logging)


    
    def read_ip(self):
         # Definir la ruta de la carpeta y archivo de configuración
        config_folder = "config"
        config_file = os.path.join(config_folder, "config.json")

        with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        
        return config['server_ip'] + ':' + config['port']
        
    def connect(self, empty_data):
        self.event_bus.publish('StatusUpdate', {'status':'Connecting...'})
        self.status = 'Connecting'
        #code for opc connection

    
    def disconnect(self, empty_data):
        self.event_bus.publish('StatusUpdate', {'status':'Disconnected'})
        # code for opc disconnection
    
    def start_logging(self, empty_data):
        pass

    def stop_logging(self, empty_data):
        pass

    def read_tags(self, tag_list):
        pass
    
    def browse_tags(self):
        pass

    def get_status(self):
        pass

    def handle_error(self):
        pass

    def update_config(self,config):
        self.ip             = config['server_ip']
        self.logging_freq   = config['logging_freq']