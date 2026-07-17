from skills.apps import AppSkills
from skills.files import FileSkills


class SkillManager:

    def __init__(self):

        self.apps = AppSkills()
        self.files = FileSkills()

    def execute(self, intent, target):

        if intent == "OPEN_APP":

            if target == "vscode":
                return self.apps.open_vscode()

            if target == "notepad":
                return self.apps.open_notepad()

            if target == "calculator":
                return self.apps.open_calculator()

        elif intent == "OPEN_FOLDER":

            return self.files.open_folder(target)

        elif intent == "CREATE_FOLDER":

            return self.files.create_folder(target)

        elif intent == "CREATE_FILE":

            return self.files.create_file(target)

        elif intent == "WRITE_FILE":

            return self.files.write_file(
                target["filename"],
                target["content"]
            )

        elif intent == "CREATE_PROJECT":

             return self.files.create_python_project(target)
        
        elif intent == "CREATE_STUDY_PROJECT":

             return self.files.create_study_project(target)

        return None