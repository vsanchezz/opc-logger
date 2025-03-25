class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_name, callback, additional_args=None):
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append((callback, additional_args))

    def publish(self, event_name, data):
        if event_name in self.subscribers:
            for callback, additional_args in self.subscribers[event_name]:
                if additional_args is not None:
                    callback(data, additional_args)
                else:
                    callback(data)