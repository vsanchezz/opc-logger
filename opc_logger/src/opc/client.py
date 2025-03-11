class OPCClient:
    def __init__(self, server_url, username=None, password=None):
        self.server_url = server_url
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def read_variable(self, node_id):
        pass
