from opcua import Client
from datetime import datetime
import time
import threading
from typing import Dict, Any, List


NODE_IDS = [
        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.GVL_var_bool",
        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.GVL_var_int",
        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.GVL_var_real",
        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.GVL_var_string",
        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.GVL_var_array"
    ]

class OpcClient():
    def __init__(self, event_bus):
        
        self.event_bus = event_bus
        self.status = "Disconnected"
        self.server_ip = None
        self.port = '4840'
        self.logging_freq = None
        self.is_logging = False
        self.node_ids = NODE_IDS
        self.nodes = {}

        # suscribe to events
        self.event_bus.subscribe('ConfigUpdated', self.update_config)
        self.event_bus.subscribe('SaveConfiguration', self.update_config)
        self.event_bus.subscribe('Connect', self.connect)
        self.event_bus.subscribe('Disconnect', self.disconnect)
        self.event_bus.subscribe('StartLogging',self.start_logging)
        self.event_bus.subscribe('StopLogging',self.stop_logging)

        
    def connect(self, empty_data):
        self.event_bus.publish('StatusUpdate', {'status':'Connecting...'})
        self.status = 'Connecting'

        #print(self.server_ip + ':' + self.port)
        #code for opc connection

        try:
            self.server_url = 'opc.tcp://' + self.server_ip + ':' + self.port
            print(self.server_url)
            self.client = Client(self.server_url)
            self.client.set_user('admin')
            self.client.set_password('admin')
            self.client.connect()
            self.event_bus.publish('StatusUpdate', {'status':'Connected'})

            # Inicializar los nodos después de la conexión
            for node_id in self.node_ids:
                try:
                    node = self.client.get_node(node_id)
                    name = node.get_browse_name().Name
                    self.nodes[name] = node
                    print(f"Initialized node: {name}")
                except Exception as e:
                    print(f"Error initializing node {node_id}: {e}")

            return True
        except Exception as e:
            self.event_bus.publish('StatusUpdate', {'status':'Disconnected'})
            print(f"Connection failed: {e}")
            return False

    
    def disconnect(self, empty_data):
        try:
            self.client.disconnect()            
            self.status = 'Disconnected'
            self.event_bus.publish('StatusUpdate', {'status':'Disconnected'})
            return True
        except Exception as e:
            print(f"Disconnect error: {e}")
            return False

    def update_config(self,config):
        self.server_ip      = config['server_ip']
        self.logging_freq   = int(config['logging_freq'])
    
    def read_values(self):
        try:
            readings = {}

            # Leer cada nodo
            for name, node in self.nodes.items():
                try:
                    value = node.get_value()
                    readings[name] = value
                except Exception as e:
                    print(f"Error reading {name}: {e}")
                    readings[name] = None

            # Agregar timestamp
            readings['timestamp'] = datetime.now().isoformat()
            return readings

        except Exception as e:
            print(f"Error reading values: {e}")
            return None

    def logging_loop(self):
        while self.is_logging:
            try:
                values = self.read_values()
                if values:
                    self.event_bus.publish('NewReading', values)
                    #print(values)
                time.sleep(self.logging_freq)
            except Exception as e:
                print(f"Error in logging loop: {e}")
                self.is_logging = False
                break

    def start_logging(self, empty_data):
        """
        Inicia el logging de las variables
        :param self.logging_freq: Intervalo de lectura en segundos
        """
        if not self.client:
            if not self.connect():
                return False

        if not self.is_logging:
            self.is_logging = True
            self.logging_thread = threading.Thread(
                target=self.logging_loop,
            )
            self.logging_thread.start()
            print(f"Logging started with logging_freq of {self.logging_freq} seconds")
            return True
        return False

    def stop_logging(self, empty_data):
        """Detiene el logging de variables"""
        self.is_logging = False
        if self.logging_thread:
            self.logging_thread.join()
        print("Logging stopped")