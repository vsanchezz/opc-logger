# src/utils/config.py
import json
import os

class ConfigManager:
    def __init__(self, config_file="./config/config.json", mapping_file="./config/mapping.json"):
        self.config_file = config_file
        self.mapping_file = mapping_file
        self.config = self.load_config()
        self.mapping = self.load_mapping()

    def load_config(self):
        """Cargar configuración desde archivo JSON"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            else:
                print(f"Archivo de configuración no encontrado: {self.config_file}")
                return self._create_default_config()
        except Exception as e:
            print(f"Error al cargar configuración: {e}")
            return self._create_default_config()

    def save_config(self):
        """Guardar configuración en archivo JSON"""
        try:
            # Asegurar que el directorio existe
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)

            with open(self.config_file, 'w', encoding='utf-8') as file:
                json.dump(self.config, file, indent=4)
            return True
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
            return False

    def load_mapping(self):
        """Cargar mapeo de nodos desde archivo JSON"""
        try:
            if os.path.exists(self.mapping_file):
                with open(self.mapping_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            else:
                print(f"Archivo de mapeo no encontrado: {self.mapping_file}")
                return self._create_default_mapping()
        except Exception as e:
            print(f"Error al cargar mapeo: {e}")
            return self._create_default_mapping()

    def save_mapping(self):
        """Guardar mapeo de nodos en archivo JSON"""
        try:
            # Asegurar que el directorio existe
            os.makedirs(os.path.dirname(self.mapping_file), exist_ok=True)

            with open(self.mapping_file, 'w', encoding='utf-8') as file:
                json.dump(self.mapping, file, indent=4)
            return True
        except Exception as e:
            print(f"Error al guardar mapeo: {e}")
            return False

    def _create_default_config(self):
        """Crear configuración por defecto"""
        default_config = {
            "opc_server": {
                "url": "opc.tcp://localhost:4840",
                "username": "",
                "password": ""
            },
            "logging": {
                "interval_seconds": 60,
                "output_format": "csv",
                "output_path": "./data/production"
            },
            "auto_mode": {
                "enabled": False,
                "start_time": "08:00",
                "end_time": "17:00",
                "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            },
            "security": {
                "password_hash": ""
            }
        }
        return default_config

    def _create_default_mapping(self):
        """Crear mapeo por defecto"""
        default_mapping = {
            "nodes": [
                {
                    "node_id": "ns=2;s=Temperature",
                    "display_name": "Temperature_Zone1",
                    "unit": "°C",
                    "description": "Temperature in Zone 1"
                },
                {
                    "node_id": "ns=2;s=Pressure",
                    "display_name": "Pressure_Tank1",
                    "unit": "bar",
                    "description": "Pressure in Tank 1"
                }
            ]
        }
        return default_mapping

    def get_opc_server_url(self):
        """Obtener URL del servidor OPC"""
        return self.config["opc_server"]["url"]

    def set_opc_server_url(self, url):
        """Establecer URL del servidor OPC"""
        self.config["opc_server"]["url"] = url
        return self.save_config()

    def get_logging_interval(self):
        """Obtener intervalo de logging en segundos"""
        return self.config["logging"]["interval_seconds"]

    def get_output_format(self):
        """Obtener formato de salida (csv o xlsx)"""
        return self.config["logging"]["output_format"]

    def get_nodes(self):
        """Obtener lista de nodos configurados"""
        return self.mapping["nodes"]