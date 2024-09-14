import json

class JsonHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)