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