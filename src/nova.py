from pathlib import Path

from ai.manager import AIManager
from brain.brain import Brain
from brain.intent import IntentEngine
from memory.extractor import MemoryExtractor
from memory.conversation import ConversationMemory
from skills.manager import SkillManager
from brain.planner import Planner


class Nova:
    def __init__(self):
        # Core Systems
        self.ai = AIManager()
        self.brain = Brain()
        self.intent = IntentEngine()
        self.planner = Planner()
        
        # Memory
        self.extractor = MemoryExtractor()
        self.conversation = ConversationMemory()

        # Skills
        self.skills = SkillManager()

        # Personality
        personality_path = (
            Path(__file__).parent.parent / "prompts" / "personality.md"
        )

        with open(personality_path, "r", encoding="utf-8") as file:
            self.personality = file.read()

    def chat(self, user_message):
        
        # ==========================
        # Planner
        # ==========================

        plan = self.planner.plan(user_message)

        if plan:

            last_result = None

            for intent, target in plan:

                result = self.skills.execute(intent, target)

                if result:
                   print(f"[PLAN] {result}")

                   last_result = result

            if last_result:
                return last_result
        """
        Nova's main processing pipeline.

        User
          ↓
        Intent Detection
          ↓
        Skills
          ↓
        Memory
          ↓
        Brain
          ↓
        AI
        """

        # ==========================
        # 1. Intent Detection
        # ==========================
        intent, target = self.intent.detect(user_message)

        print(f"[DEBUG] Intent: {intent}")
        print(f"[DEBUG] Target: {target}")

        if intent:
            result = self.skills.execute(intent, target)

            print(f"[DEBUG] Skill Result: {result}")

            if result:
                return result

        # ==========================
        # 2. Memory Extraction
        # ==========================
        memory_message = self.extractor.process(user_message)

        if memory_message:
            print(f"\n[Memory] {memory_message}")

        # ==========================
        # 3. Brain Responses
        # ==========================
        brain_response = self.brain.think(user_message)

        if brain_response:
            self.conversation.add_user(user_message)
            self.conversation.add_nova(brain_response)
            return brain_response

        # ==========================
        # 4. Conversation History
        # ==========================
        self.conversation.add_user(user_message)
        history = self.conversation.build_history()

        # ==========================
        # 5. Build Prompt
        # ==========================
        prompt = f"""
{self.personality}

Conversation:

{history}

Nova:
"""

        response = self.ai.generate(prompt)

        self.conversation.add_nova(response)

        return response