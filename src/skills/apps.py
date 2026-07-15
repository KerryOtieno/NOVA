import subprocess
import platform


class AppSkills:

    def open_vscode(self):

        try:
            subprocess.Popen("code")

            return "Opening Visual Studio Code."

        except Exception:

            return "I couldn't open Visual Studio Code."

    def open_notepad(self):

        try:
            subprocess.Popen("notepad")

            return "Opening Notepad."

        except Exception:

            return "I couldn't open Notepad."

    def open_calculator(self):

        try:

            if platform.system() == "Windows":
                subprocess.Popen("calc")

            return "Opening Calculator."

        except Exception:

            return "I couldn't open Calculator."