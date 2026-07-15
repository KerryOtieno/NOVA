from ai.ollama import OllamaProvider


class AIManager:

    def __init__(self):
        self.provider = OllamaProvider()

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)