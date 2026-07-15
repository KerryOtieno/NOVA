class ConversationMemory:

    def __init__(self):
        self.history = []

    def add_user(self, message):
        self.history.append({
            "role": "user",
            "content": message
        })

    def add_nova(self, message):
        self.history.append({
            "role": "assistant",
            "content": message
        })

    def build_history(self):

        text = ""

        for item in self.history:
            text += f"{item['role'].title()}: {item['content']}\n"

        return text

    def clear(self):
        self.history.clear()