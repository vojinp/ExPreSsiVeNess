import json

class JsonParser:
    def __init__(self):
        self.data = None

    def load(self, path):
        with open(path, 'r') as json_file:
            self.data = json.load(json_file)
        return self.data
