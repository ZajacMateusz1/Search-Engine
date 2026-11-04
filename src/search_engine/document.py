import uuid


def add_document(path: str) -> tuple[uuid.UUID, str] | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            return (str(uuid.uuid4()), content)
    except FileNotFoundError:
        print("Cannot find the file at the specified path:", path)
