# Name: Harshalkumar Patel
# Id: 100918597
# Date: 12-06-2024 

import json

class JsonHandler:
    def read_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def write_json(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def check_key(self, data, key):
        return key in data

    def update_json(self, key, value, file_path):
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data[key] = value
            file.seek(0)
            json.dump(data, file)
            file.truncate()
