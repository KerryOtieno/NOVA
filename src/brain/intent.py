class IntentEngine:

    def detect(self, message):

        text = message.lower()

        # -------------------------
        # OPEN
        # -------------------------

        if any(word in text for word in [
            "open",
            "launch",
            "start",
            "run"
        ]):

            if "vscode" in text or "visual studio code" in text:
                return ("OPEN_APP", "vscode")

            if "notepad" in text:
                return ("OPEN_APP", "notepad")

            if "calculator" in text or "calc" in text:
                return ("OPEN_APP", "calculator")

            folders = [
                "downloads",
                "documents",
                "desktop",
                "pictures",
                "music",
                "videos",
                "nova"
            ]

            for folder in folders:
                if folder in text:
                    return ("OPEN_FOLDER", folder)

        # -------------------------
        # CREATE FOLDER
        # -------------------------

        if "create folder" in text:

            folder = text.split("create folder")[-1]
            folder = folder.replace("called", "").strip()

            return ("CREATE_FOLDER", folder)

        # -------------------------
        # CREATE FILE
        # -------------------------

        if "create file" in text:

            filename = text.split("create file")[-1]
            filename = filename.replace("called", "").strip()

            return ("CREATE_FILE", filename)

        # -------------------------
        # WRITE TO FILE
        # -------------------------

        if "write" in text and "into" in text:

            content = message.split("into")[0]
            content = content.replace("Write", "")
            content = content.replace("write", "")
            content = content.strip()

            filename = message.split("into")[-1].strip()

            return (
                "WRITE_FILE",
                {
                    "filename": filename,
                    "content": content
                }
            )

        # -------------------------
        # No Intent Found
        # -------------------------

        return (None, None)