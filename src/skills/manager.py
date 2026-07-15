from skills.apps import AppSkills


class SkillManager:

    def __init__(self):

        self.apps = AppSkills()

    def run(self, message):

        text = message.lower()

        if "open vscode" in text:

            return self.apps.open_vscode()

        if "open visual studio code" in text:

            return self.apps.open_vscode()

        if "open notepad" in text:

            return self.apps.open_notepad()

        if "open calculator" in text:

            return self.apps.open_calculator()

        return None