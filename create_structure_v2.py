import os
import json

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Creado directorio: {path}")

def create_file(path, content=""):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Creado archivo: {path}")

def create_project_structure(base_path="opc_logger"):
    create_directory(base_path)

    create_file(os.path.join(base_path, "main.py"),
                "from src.gui.main_window import MainWindow\n\n"
                "def main():\n"
                "    app = MainWindow()\n"
                "    app.mainloop()\n\n"
                "if __name__ == \"__main__\":\n"
                "    main()\n")

    create_file(os.path.join(base_path, "requirements.txt"),
                "customtkinter>=5.2.0\n"
                "opcua-client>=0.8.4\n"
                "pandas>=2.0.0\n"
                "numpy>=1.24.0\n"
                "cryptography>=41.0.0\n")

    create_file(os.path.join(base_path, "README.md"),
                "# OPC Logger\n\n"
                "Aplicación para conectarse a un servidor OPC, leer variables y realizar data logging.\n\n"
                "## Características\n\n"
                "- Conexión a servidor OPC\n"
                "- Registro de datos en formato CSV/XLSX\n"
                "- Interfaz gráfica con tema oscuro\n"
                "- Modo automático para iniciar/detener la recolección de datos\n\n"
                "## Instalación\n\n"
                "```\n"
                "pip install -r requirements.txt\n"
                "```\n\n"
                "## Uso\n\n"
                "```\n"
                "python main.py\n"
                "```\n")

    create_file(os.path.join(base_path, "setup.py"),
                "from setuptools import setup, find_packages\n\n"
                "setup(\n"
                "    name=\"opc_logger\",\n"
                "    version=\"0.1\",\n"
                "    packages=find_packages(),\n"
                "    install_requires=[\n"
                "        \"customtkinter\",\n"
                "        \"opcua-client\",\n"
                "        \"pandas\",\n"
                "        \"numpy\",\n"
                "        \"cryptography\",\n"
                "    ],\n"
                ")\n")

    config_dir = os.path.join(base_path, "config")
    create_directory(config_dir)

    config_json = {
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
    create_file(os.path.join(config_dir, "config.json"), json.dumps(config_json, indent=4))

    mapping_json = {
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
    create_file(os.path.join(config_dir, "mapping.json"), json.dumps(mapping_json, indent=4))

    data_dir = os.path.join(base_path, "data")
    create_directory(data_dir)
    create_directory(os.path.join(data_dir, "logs"))
    create_directory(os.path.join(data_dir, "backups"))
    create_directory(os.path.join(data_dir, "production"))
    create_directory(os.path.join(data_dir, "production", "2025"))
    create_directory(os.path.join(data_dir, "production", "2025", "03"))

    create_file(os.path.join(data_dir, "logs", "error_log.txt"), "")

    instructions_dir = os.path.join(base_path, "instructions")
    create_directory(instructions_dir)

    create_file(os.path.join(instructions_dir, "1_generate_hash.txt"),
                "Instrucciones para generar el hash de la contraseña:\n\n"
                "1. Ejecute la aplicación\n"
                "2. Vaya a Configuración > Seguridad\n"
                "3. Ingrese la contraseña deseada y haga clic en 'Generar Hash'\n"
                "4. Copie el hash generado y péguelo en el archivo config.json\n")

    create_file(os.path.join(instructions_dir, "2_configure_opc.txt"),
                "Instrucciones para configurar el servidor OPC:\n\n"
                "1. Ejecute la aplicación\n"
                "2. Vaya a Configuración > Servidor OPC\n"
                "3. Ingrese la URL del servidor OPC\n"
                "4. Si es necesario, ingrese el nombre de usuario y contraseña\n"
                "5. Haga clic en 'Guardar'\n")

    create_file(os.path.join(instructions_dir, "3_map_nodes.txt"),
                "Instrucciones para mapear nodos OPC a nombres amigables:\n\n"
                "1. Ejecute la aplicación\n"
                "2. Vaya a Configuración > Mapeo de Nodos\n"
                "3. Haga clic en 'Explorar Servidor' para ver los nodos disponibles\n"
                "4. Seleccione los nodos que desea mapear\n"
                "5. Asigne nombres amigables, unidades y descripciones\n"
                "6. Haga clic en 'Guardar'\n")

    create_file(os.path.join(instructions_dir, "4_set_logging_path.txt"),
                "Instrucciones para configurar el path de destino:\n\n"
                "1. Ejecute la aplicación\n"
                "2. Vaya a Configuración > Logging\n"
                "3. Seleccione el formato de salida (CSV o XLSX)\n"
                "4. Seleccione el intervalo de logging en segundos\n"
                "5. Seleccione la carpeta de destino\n"
                "6. Haga clic en 'Guardar'\n")

    create_file(os.path.join(instructions_dir, "5_enable_auto_mode.txt"),
                "Instrucciones para habilitar el modo automático:\n\n"
                "1. Ejecute la aplicación\n"
                "2. Vaya a Configuración > Modo Automático\n"
                "3. Active la opción 'Habilitar modo automático'\n"
                "4. Seleccione la hora de inicio y fin\n"
                "5. Seleccione los días de la semana\n"
                "6. Haga clic en 'Guardar'\n")

    src_dir = os.path.join(base_path, "src")
    create_directory(src_dir)
    create_file(os.path.join(src_dir, "__init__.py"), "")

    opc_dir = os.path.join(src_dir, "opc")
    create_directory(opc_dir)
    create_file(os.path.join(opc_dir, "__init__.py"), "")

    create_file(os.path.join(opc_dir, "client.py"),
                "class OPCClient:\n"
                "    def __init__(self, server_url, username=None, password=None):\n"
                "        self.server_url = server_url\n"
                "        self.username = username\n"
                "        self.password = password\n"
                "        self.connection = None\n\n"
                "    def connect(self):\n"
                "        pass\n\n"
                "    def disconnect(self):\n"
                "        pass\n\n"
                "    def read_variable(self, node_id):\n"
                "        pass\n")

    create_file(os.path.join(opc_dir, "nodes.py"),
                "class OPCNode:\n"
                "    def __init__(self, node_id, display_name, unit=None, description=None):\n"
                "        self.node_id = node_id\n"
                "        self.display_name = display_name\n"
                "        self.unit = unit\n"
                "        self.description = description\n\n"
                "class NodeManager:\n"
                "    def __init__(self, opc_client):\n"
                "        self.opc_client = opc_client\n"
                "        self.nodes = []\n\n"
                "    def load_nodes_from_config(self, config_file):\n"
                "        pass\n\n"
                "    def explore_server(self):\n"
                "        pass\n")

    logging_dir = os.path.join(src_dir, "logging")
    create_directory(logging_dir)
    create_file(os.path.join(logging_dir, "__init__.py"), "")

    create_file(os.path.join(logging_dir, "data_logger.py"),
                "import os\n"
                "from datetime import datetime\n\n"
                "class DataLogger:\n"
                "    def __init__(self, output_format='csv', output_path='./data/production'):\n"
                "        self.output_format = output_format\n"
                "        self.output_path = output_path\n"
                "        self.current_file = None\n\n"
                "    def start_logging(self):\n"
                "        pass\n\n"
                "    def stop_logging(self):\n"
                "        pass\n\n"
                "    def log_data(self, data):\n"
                "        pass\n\n"
                "    def _create_file(self):\n"
                "        pass\n")

    create_file(os.path.join(logging_dir, "error_logger.py"),
                "import logging\n"
                "from datetime import datetime\n\n"
                "class ErrorLogger:\n"
                "    def __init__(self, log_file='./data/logs/error_log.txt'):\n"
                "        self.log_file = log_file\n"
                "        self._setup_logger()\n\n"
                "    def _setup_logger(self):\n"
                "        pass\n\n"
                "    def log_error(self, message, exception=None):\n"
                "        pass\n\n"
                "    def log_info(self, message):\n"
                "        pass\n")

    gui_dir = os.path.join(src_dir, "gui")
    create_directory(gui_dir)
    create_file(os.path.join(gui_dir, "__init__.py"), "")

    create_file(os.path.join(gui_dir, "main_window.py"),
                "import customtkinter as ctk\n"
                "from datetime import datetime\n"
                "from .components.status_bar import StatusBar\n"
                "from .components.control_panel import ControlPanel\n"
                "from .components.data_display import DataDisplay\n"
                "from .components.settings_tab import SettingsTab\n\n"
                "class MainWindow(ctk.CTk):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n\n"
                "        ctk.set_appearance_mode(\"dark\")\n"
                "        ctk.set_default_color_theme(\"blue\")\n\n"
                "        self.title(\"OPC Data Logger\")\n"
                "        self.geometry(\"1000x700\")\n"
                "        self.minsize(800, 600)\n\n"
                "        self.connection_state = \"Disconnected\"\n"
                "        self.logging_active = False\n\n"
                "        self.create_widgets()\n\n"
                "        self.update_clock()\n\n"
                "    def create_widgets(self):\n"
                "        pass\n\n"
                "    def update_clock(self):\n"
                "        pass\n")

    gui_components_dir = os.path.join(gui_dir, "components")
    create_directory(gui_components_dir)
    create_file(os.path.join(gui_components_dir, "__init__.py"), "")

    create_file(os.path.join(gui_components_dir, "status_bar.py"),
                "import customtkinter as ctk\n"
                "from datetime import datetime\n\n"
                "class StatusBar(ctk.CTkFrame):\n"
                "    def __init__(self, parent, controller):\n"
                "        super().__init__(parent)\n"
                "        self.controller = controller\n\n"
                "        self.status_label = ctk.CTkLabel(\n"
                "            self,\n"
                "            text=\"Status: Disconnected\",\n"
                "            text_color=\"red\",\n"
                "            font=(\"Arial\", 14, \"bold\")\n"
                "        )\n"
                "        self.status_label.pack(side=\"left\", padx=10)\n\n"
                "        self.time_label = ctk.CTkLabel(\n"
                "            self,\n"
                "            text=datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n"
                "        )\n"
                "        self.time_label.pack(side=\"right\", padx=10)\n\n"
                "    def update_time(self):\n"
                "        pass\n\n"
                "    def update_status(self, status, color):\n"
                "        pass\n")

    create_file(os.path.join(gui_components_dir, "control_panel.py"),
                "import customtkinter as ctk\n\n"
                "class ControlPanel(ctk.CTkFrame):\n"
                "    def __init__(self, parent, controller):\n"
                "        super().__init__(parent)\n"
                "        self.controller = controller\n\n"
                "        self.connect_button = ctk.CTkButton(\n"
                "            self,\n"
                "            text=\"Connect\",\n"
                "            command=self.toggle_connection,\n"
                "            width=120\n"
                "        )\n"
                "        self.connect_button.pack(side=\"left\", padx=10, pady=10)\n\n"
                "        self.start_button = ctk.CTkButton(\n"
                "            self,\n"
                "            text=\"Start Logging\",\n"
                "            command=self.start_logging,\n"
                "            state=\"disabled\",\n"
                "            width=120\n"
                "        )\n"
                "        self.start_button.pack(side=\"left\", padx=10, pady=10)\n\n"
                "        self.stop_button = ctk.CTkButton(\n"
                "            self,\n"
                "            text=\"Stop Logging\",\n"
                "            command=self.stop_logging,\n"
                "            state=\"disabled\",\n"
                "            width=120\n"
                "        )\n"
                "        self.stop_button.pack(side=\"left\", padx=10, pady=10)\n\n"
                "    def toggle_connection(self):\n"
                "        pass\n\n"
                "    def start_logging(self):\n"
                "        pass\n\n"
                "    def stop_logging(self):\n"
                "        pass\n")

    create_file(os.path.join(gui_components_dir, "data_display.py"),
                "import customtkinter as ctk\n"
                "from datetime import datetime\n\n"
                "class DataDisplay(ctk.CTkFrame):\n"
                "    def __init__(self, parent):\n"
                "        super().__init__(parent)\n\n"
                "        self.data_label = ctk.CTkLabel(\n"
                "            self,\n"
                "            text=\"Collected Data (newest at top):\",\n"
                "            anchor=\"w\"\n"
                "        )\n"
                "        self.data_label.pack(anchor=\"w\", padx=10, pady=5)\n\n"
                "        self.data_text = ctk.CTkTextbox(\n"
                "            self,\n"
                "            wrap=\"none\",\n"
                "            font=(\"Consolas\", 12)\n"
                "        )\n"
                "        self.data_text.pack(fill=\"both\", expand=True, padx=10, pady=5)\n\n"
                "    def add_data_entry(self, data):\n"
                "        pass\n\n"
                "    def clear_data(self):\n"
                "        pass\n")

    create_file(os.path.join(gui_components_dir, "settings_tab.py"),
                "import customtkinter as ctk\n\n"
                "class SettingsTab(ctk.CTkFrame):\n"
                "    def __init__(self, parent):\n"
                "        super().__init__(parent)\n\n"
                "        self.server_label = ctk.CTkLabel(\n"
                "            self,\n"
                "            text=\"OPC Server IP Address:\",\n"
                "            anchor=\"w\"\n"
                "        )\n"
                "        self.server_label.pack(anchor=\"w\", padx=10, pady=5)\n\n"
                "        self.server_entry = ctk.CTkEntry(\n"
                "            self,\n"
                "            width=300\n"
                "        )\n"
                "        self.server_entry.pack(anchor=\"w\", padx=10, pady=5)\n\n"
                "        self.variables_label = ctk.CTkLabel(\n"
                "            self,\n"
                "            text=\"Select OPC Variables to Log:\",\n"
                "            anchor=\"w\"\n"
                "        )\n"
                "        self.variables_label.pack(anchor=\"w\", padx=10, pady=5)\n\n"
                "        self.variables_container = ctk.CTkScrollableFrame(\n"
                "            self,\n"
                "            width=300,\n"
                "            height=300\n"
                "        )\n"
                "        self.variables_container.pack(fill=\"both\", expand=True, padx=10, pady=5)\n")

    gui_dialogs_dir = os.path.join(gui_dir, "dialogs")
    create_directory(gui_dialogs_dir)
    create_file(os.path.join(gui_dialogs_dir, "__init__.py"), "")

    create_file(os.path.join(gui_dialogs_dir, "connection_dialog.py"),
                "import customtkinter as ctk\n\n"
                "class ConnectionDialog(ctk.CTkToplevel):\n"
                "    def __init__(self, parent, initial_url=\"\", initial_username=\"\", initial_password=\"\"):\n"
                "        super().__init__(parent)\n\n"
                "        self.title(\"OPC Server Connection\")\n"
                "        self.geometry(\"400x300\")\n"
                "        self.resizable(False, False)\n\n"
                "        self.result = None\n\n"
                "    def _on_cancel(self):\n"
                "        pass\n\n"
                "    def _on_connect(self):\n"
                "        pass\n")

    create_file(os.path.join(gui_dialogs_dir, "settings_dialog.py"),
                "import customtkinter as ctk\n\n"
                "class SettingsDialog(ctk.CTkToplevel):\n"
                "    def __init__(self, parent, config):\n"
                "        super().__init__(parent)\n\n"
                "        self.title(\"Settings\")\n"
                "        self.geometry(\"500x400\")\n"
                "        self.resizable(False, False)\n\n"
                "        self.config = config\n"
                "        self.result = None\n\n"
                "    def _on_cancel(self):\n"
                "        pass\n\n"
                "    def _on_save(self):\n"
                "        pass\n")

    utils_dir = os.path.join(src_dir, "utils")
    create_directory(utils_dir)
    create_file(os.path.join(utils_dir, "__init__.py"), "")

    create_file(os.path.join(utils_dir, "config.py"),
                "import json\n"
                "import os\n\n"
                "class ConfigManager:\n"
                "    def __init__(self, config_file=\"./config/config.json\", mapping_file=\"./config/mapping.json\"):\n"
                "        self.config_file = config_file\n"
                "        self.mapping_file = mapping_file\n"
                "        self.config = self.load_config()\n"
                "        self.mapping = self.load_mapping()\n\n"
                "    def load_config(self):\n"
                "        pass\n\n"
                "    def save_config(self):\n"
                "        pass\n\n"
                "    def load_mapping(self):\n"
                "        pass\n\n"
                "    def save_mapping(self):\n"
                "        pass\n")

    create_file(os.path.join(utils_dir, "file_handler.py"),
                "import os\n"
                "import csv\n"
                "import pandas as pd\n"
                "from datetime import datetime\n\n"
                "class FileHandler:\n"
                "    @staticmethod\n"
                "    def ensure_directory_exists(directory):\n"
                "        pass\n\n"
                "    @staticmethod\n"
                "    def create_csv_file(path, headers):\n"
                "        pass\n\n"
                "    @staticmethod\n"
                "    def append_to_csv(path, data):\n"
                "        pass\n\n"
                "    @staticmethod\n"
                "    def create_xlsx_file(path, headers):\n"
                "        pass\n\n"
                "    @staticmethod\n"
                "    def append_to_xlsx(path, data):\n"
                "        pass\n")

    create_file(os.path.join(utils_dir, "auth.py"),
                "import hashlib\n"
                "import os\n"
                "from cryptography.fernet import Fernet\n\n"
                "class Auth:\n"
                "    @staticmethod\n"
                "    def generate_password_hash(password):\n"
                "        pass\n\n"
                "    @staticmethod\n"
                "    def verify_password(password, password_hash):\n"
                "        pass\n")

    auto_mode_dir = os.path.join(src_dir, "auto_mode")
    create_directory(auto_mode_dir)
    create_file(os.path.join(auto_mode_dir, "__init__.py"), "")

    create_file(os.path.join(auto_mode_dir, "scheduler.py"),
                "import time\n"
                "import threading\n"
                "from datetime import datetime, timedelta\n\n"
                "class Scheduler:\n"
                "    def __init__(self):\n"
                "        self.scheduled_tasks = []\n"
                "        self.running = False\n"
                "        self.thread = None\n\n"
                "    def start(self):\n"
                "        pass\n\n"
                "    def stop(self):\n"
                "        pass\n\n"
                "    def add_task(self, task, start_time, end_time, days):\n"
                "        pass\n\n"
                "    def remove_task(self, task_id):\n"
                "        pass\n\n"
                "    def _run(self):\n"
                "        pass\n")

    create_file(os.path.join(auto_mode_dir, "controller.py"),
                "from datetime import datetime\n\n"
                "class AutoModeController:\n"
                "    def __init__(self, scheduler, data_logger, opc_client):\n"
                "        self.scheduler = scheduler\n"
                "        self.data_logger = data_logger\n"
                "        self.opc_client = opc_client\n"
                "        self.enabled = False\n\n"
                "    def enable(self, start_time, end_time, days):\n"
                "        pass\n\n"
                "    def disable(self):\n"
                "        pass\n\n"
                "    def start_logging(self):\n"
                "        pass\n\n"
                "    def stop_logging(self):\n"
                "        pass\n")

    tests_dir = os.path.join(base_path, "tests")
    create_directory(tests_dir)
    create_file(os.path.join(tests_dir, "__init__.py"), "")

    opc_tests_dir = os.path.join(tests_dir, "opc")
    create_directory(opc_tests_dir)
    create_file(os.path.join(opc_tests_dir, "__init__.py"), "")
    create_file(os.path.join(opc_tests_dir, "test_client.py"), "")
    create_file(os.path.join(opc_tests_dir, "test_nodes.py"), "")

    logging_tests_dir = os.path.join(tests_dir, "logging")
    create_directory(logging_tests_dir)
    create_file(os.path.join(logging_tests_dir, "__init__.py"), "")
    create_file(os.path.join(logging_tests_dir, "test_data_logger.py"), "")
    create_file(os.path.join(logging_tests_dir, "test_error_logger.py"), "")

    gui_tests_dir = os.path.join(tests_dir, "gui")
    create_directory(gui_tests_dir)
    create_file(os.path.join(gui_tests_dir, "__init__.py"), "")
    create_file(os.path.join(gui_tests_dir, "test_main_window.py"), "")
    create_file(os.path.join(gui_tests_dir, "test_components.py"), "")

    utils_tests_dir = os.path.join(tests_dir, "utils")
    create_directory(utils_tests_dir)
    create_file(os.path.join(utils_tests_dir, "__init__.py"), "")
    create_file(os.path.join(utils_tests_dir, "test_config.py"), "")
    create_file(os.path.join(utils_tests_dir, "test_file_handler.py"), "")
    create_file(os.path.join(utils_tests_dir, "test_auth.py"), "")

    auto_mode_tests_dir = os.path.join(tests_dir, "auto_mode")
    create_directory(auto_mode_tests_dir)
    create_file(os.path.join(auto_mode_tests_dir, "__init__.py"), "")
    create_file(os.path.join(auto_mode_tests_dir, "test_scheduler.py"), "")
    create_file(os.path.join(auto_mode_tests_dir, "test_controller.py"), "")

if __name__ == "__main__":
    create_project_structure()