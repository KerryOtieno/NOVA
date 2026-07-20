from fileinput import filename
from importlib.metadata import files
import os
import subprocess


class FileSkills:

    folders = {
        "downloads": "Downloads",
        "documents": "Documents",
        "desktop": "Desktop",
        "pictures": "Pictures",
        "music": "Music",
        "videos": "Videos",

    }

    def append_file(self, filename, content):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
    )

    # Search recursively
        for root, dirs, files in os.walk(documents):

            if filename in files:

                file_path = os.path.join(root, filename)

                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(content + "\n")

                return f"I've added the text to '{filename}'."

        return f"I couldn't find '{filename}'."

    def read_file(self, filename):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
    )

        for root, dirs, files in os.walk(documents):

            if filename in files:

                file_path = os.path.join(root, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if content.strip():
                return f"Contents of '{filename}':\n\n{content}"
            else:
                return f"'{filename}' is empty."

        return f"I couldn't find '{filename}'."
    

    def open_folder(self, folder):

        if folder == "nova":
            folder_path = r"C:\Users\Kerry\Documents\NOVA"

        else:

            if folder not in self.folders:
                return None

            folder_path = os.path.join(
                os.path.expanduser("~"),
                self.folders[folder]
            )

        subprocess.Popen(f'explorer "{folder_path}"')

        return f"Opening {folder.title()}."

    def create_folder(self, folder_name):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        folder_path = os.path.join(documents, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        return f"Folder '{folder_name}' created successfully."

    def create_file(self, filename):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        file_path = os.path.join(documents, filename)

        with open(file_path, "w", encoding="utf-8"):
            pass

        return f"File '{filename}' created successfully."

    def write_file(self, filename, content):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        file_path = os.path.join(documents, filename)

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content + "\n")

        return f"I've written to '{filename}'."
    
    def create_python_project(self, project_name):

        documents = os.path.join(
           os.path.expanduser("~"),
           "Documents"
    )

        project_path = os.path.join(documents, project_name)

        folders = [
           "src",
           "tests",
           "data",
           "assets"
    ]

        for folder in folders:
            os.makedirs(
              os.path.join(project_path, folder),
              exist_ok=True
        )

    # README
        with open(
            os.path.join(project_path, "README.md"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write(f"# {project_name}\n\n")
            f.write("Created by Nova.\n")

    # requirements
        with open(
            os.path.join(project_path, "requirements.txt"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write("")

    # .gitignore
        with open(
            os.path.join(project_path, ".gitignore"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write("__pycache__/\n")
            f.write(".venv/\n")
            f.write(".env\n")

    # main.py
        with open(
            os.path.join(project_path, "src", "main.py"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write('print("Hello from Nova!")\n')

        return f"Python project '{project_name}' created successfully."
    
    def create_study_project(self, subject):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
    )

        project_path = os.path.join(documents, subject)

        os.makedirs(project_path, exist_ok=True)

        files = [
            "notes.txt",
            "revision.txt",
            "questions.txt",
            "formula_sheet.txt"
    ]

        for filename in files:

            file_path = os.path.join(project_path, filename)

            with open(file_path, "w", encoding="utf-8") as file:

                file.write(f"{subject}\n")
                file.write("=" * len(subject))
                file.write("\n\n")

                if filename == "notes.txt":
                    file.write("Lecture Notes\n\n")

                elif filename == "revision.txt":
                    file.write("Revision Checklist\n\n")

                elif filename == "questions.txt":
                    file.write("Practice Questions\n\n")

                elif filename == "formula_sheet.txt":
                    file.write("Important Formulae\n\n")

        return f"Study project '{subject}' created successfully."