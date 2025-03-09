import os
import zipfile

def create_project_structure(base_path):
    structure = {
        "opc_logger": {
            "config": ["config.json", "mapping.json"],
            "data": {
                "logs": ["error_log.txt"],
                "backups": [],
                "production": []
            },
            "instructions": [
                "1_generate_hash.txt",
                "2_configure_opc.txt",
                "3_map_nodes.txt",
                "4_set_logging_path.txt",
                "5_enable_auto_mode.txt"
            ],
            "src": [
                "opc_client.py",
                "data_logger.py",
                "gui.py",
                "auth.py",
                "auto_mode.py",
                "error_logger.py",
                "utils.py",
                "__init__.py"
            ],
            "tests": [
                "test_opc_client.py",
                "test_data_logger.py",
                "test_auth.py",
                "test_auto_mode.py",
                "test_error_logger.py",
                "__init__.py"
            ],
        "main.py": None,
        "requirements.txt": None,
        "README.md": None
        },        
    }

    def create_items(base, items):
        for key, value in items.items():
            if isinstance(value, dict):
                folder_path = os.path.join(base, key)
                os.makedirs(folder_path, exist_ok=True)
                create_items(folder_path, value)
            elif isinstance(value, list):
                folder_path = os.path.join(base, key)
                os.makedirs(folder_path, exist_ok=True)
                for item in value:
                    file_path = os.path.join(folder_path, item)
                    with open(file_path, "w") as f:
                        f.write("")
            elif value is None:
                file_path = os.path.join(base, key)
                with open(file_path, "w") as f:
                    f.write("")

    create_items("", structure)


def zip_project(base_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_path)
                zipf.write(file_path, arcname)


# Create the project structure
base_path = "opc_logger"
create_project_structure(base_path)

# Zip the project
# zip_name = "opc_logger_project_final.zip"
# zip_project(base_path, zip_name)

zip_name