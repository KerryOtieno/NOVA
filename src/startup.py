from datetime import datetime
from memory.memory import Memory


class StartupManager:

    def __init__(self):
        self.memory = Memory()

    def greeting(self):

        hour = datetime.now().hour

        if hour < 12:
            return "Good morning"

        elif hour < 18:
            return "Good afternoon"

        return "Good evening"

    def memory_count(self):

        memories = self.memory.load()

        return len(memories)

    def banner(self):

        print("=" * 42)
        print("             NOVA AI v0.6")
        print("=" * 42)
        print()

        print("Initializing...\n")

        print("✓ Personality Loaded")
        print(f"✓ Memory Loaded ({self.memory_count()} facts)")
        print("✓ Conversation Ready")
        print("✓ AI Engine: Ollama (Gemma 3)")
        print()

        print("-" * 42)
        print(f"{self.greeting()}, Kerry.")
        print("Welcome back.\n")
        print("How can I help you today?\n")