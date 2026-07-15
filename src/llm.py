import requests

class LLMService:
    def generate(self, prompt: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False,
            },
        )

        return response.json()["response"]