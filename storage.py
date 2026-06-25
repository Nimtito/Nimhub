import json
import os

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "nimhub_data.json")


def initialize_data_file():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_projects():
    initialize_data_file()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_projects(projects):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(projects, file, indent=4)