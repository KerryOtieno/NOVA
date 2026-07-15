from pathlib import Path

from ai.manager import AIManager
from brain.brain import Brain
from memory.extractor import MemoryExtractor
from memory.conversation import ConversationMemory
from skills.manager import SkillManager

class Nova:

    def __init__(self):
        self.ai = AIManager()
        self.brain = Brain()
        self.extractor = MemoryExtractor()
        self.conversation = ConversationMemory()
        self.skills = SkillManager()


        # Load personality
        personality_path = Path(__file__).parent.parent / "prompts" / "personality.md"

        with open(personality_path, "r", encoding="utf-8") as f:
            self.personality = f.read()

    def chat(self, user_message):

        skill = self.skills.run(user_message)

        if skill:
            return skill

        # Store memories
        memory_message = self.extractor.process(user_message)

        if memory_message:
            print(f"\n[Memory] {memory_message}")

        # Let the Brain answer first
        answer = self.brain.think(user_message)

        if answer:
            self.conversation.add_user(user_message)
            self.conversation.add_nova(answer)
            return answer

        # Conversation history
        self.conversation.add_user(user_message)
        history = self.conversation.build_history()

        # Final prompt
        prompt = f"""
{self.personality}

Conversation:

{history}

Nova:
"""

        response = self.ai.generate(prompt)

        self.conversation.add_nova(response)

        return response