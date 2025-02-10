import json

def load_data():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
