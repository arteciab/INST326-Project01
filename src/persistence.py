import json
from pathlib import Path


def save_state(data: dict, file_path: str) -> None:
    path = Path(file_path)

    # Make sure parent folder exists (ex: "data/")
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_state(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"State file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
