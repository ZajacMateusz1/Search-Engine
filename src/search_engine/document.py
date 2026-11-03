def add_document(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Cannot find the file at the specified path:", path)
