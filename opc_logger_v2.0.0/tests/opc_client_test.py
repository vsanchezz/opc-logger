# tests/opc_client_test.py
import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from src.opc_client import OpcClient
from src.event_bus import EventBus

print("Starting OPC client test...")
event_bus = EventBus()
opc_client = OpcClient(event_bus)
opc_client.server_ip = 'localhost'
opc_client.logging_freq = 1

print("Attempting to connect...")
connection_result = opc_client.connect({})
print(f"Connection result: {connection_result}")

opc_client.start_logging({})

print("Waiting for 5 seconds...")
time.sleep(10)

opc_client.stop_logging({})

print("Disconnecting...")
opc_client.disconnect({})
print("Test completed successfully")


''' ejemplo de respuesta del servidor 
{'GVL_var_bool': False, 'GVL_var_int': 0, 'GVL_var_real': 0.0, 'GVL_var_string': '', 'GVL_var_array': [False, False, False, False], 'timestamp': '2025-03-26T21:25:16.296532'}
'''