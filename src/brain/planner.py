from email.mime import message

class Planner:
    """
    The Planner converts a user's goal into
    a sequence of actions Nova already knows
    how to perform.
    """

    def plan(self, message):

        text = message.lower()


        # -------------------------
        # Python Project
        # -------------------------

        if "python project" in text:

            project = text.split("called")[-1].strip()

            return [
                ("CREATE_PROJECT", project),
                ("OPEN_APP", "vscode")
            ]

        # -------------------------
        # Study Project
        # -------------------------

        if "study project" in text:

            subject = text.split("called")[-1].strip()

            return [
                ("CREATE_STUDY_PROJECT", subject)
    ]

        return []