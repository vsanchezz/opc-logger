class OPCNode:
    def __init__(self, node_id, display_name, unit=None, description=None):
        self.node_id = node_id
        self.display_name = display_name
        self.unit = unit
        self.description = description

class NodeManager:
    def __init__(self, opc_client):
        self.opc_client = opc_client
        self.nodes = []

    def load_nodes_from_config(self, config_file):
        pass

    def explore_server(self):
        pass
