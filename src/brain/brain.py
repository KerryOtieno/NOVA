from memory.memory import Memory


class Brain:
    def __init__(self):
        self.memory = Memory()

    def think(self, message):
        text = message.lower().strip()

        # ----- Memory Questions -----

        if "what is my name" in text or "who am i" in text:
            name = self.memory.recall("name")
            if name:
                return f"Your name is {name}."

        if "favorite team" in text:
            team = self.memory.recall("favorite_team")
            if team:
                return f"Your favorite team is {team}."

        if "what do i study" in text or "what am i studying" in text:
            education = self.memory.recall("education")
            if education:
                return f"You are studying {education}."

        # Brain doesn't know the answer
        return None