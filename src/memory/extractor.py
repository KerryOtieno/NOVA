from memory.memory import Memory


class MemoryExtractor:

    def __init__(self):
        self.memory = Memory()

    def process(self, message):

        text = message.lower().strip()

        # -----------------------------
        # Ignore questions
        # -----------------------------
        question_words = (
            "what",
            "who",
            "where",
            "when",
            "why",
            "how",
            "do ",
            "does ",
            "did ",
            "is ",
            "are ",
            "can ",
        )

        if text.endswith("?") or text.startswith(question_words):
            return None

        #