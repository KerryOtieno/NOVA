import json
from pathlib import Path


class Memory:

    def __init__(self):
        self.file = Path("data/memory.json")

        if not self.file.exists():
            self.file.write_text("{}")

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, key, value):

        memory = self.load()

        memory[key] = value

        self.save(memory)

    def recall(self, key):

        memory = self.load()

        return memory.get(key)