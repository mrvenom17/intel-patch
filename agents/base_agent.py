class TaskAgent:
    def __init__(self, model, role="Base Agent"):
        self.model = model
        self.role = role

    def process(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")