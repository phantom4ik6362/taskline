# All actions of the program are defined here. This file is imported in main.py and executed from there.
import json
import os

def read_tasks() -> dict:
    with open("data/tasks.json", "r") as f:
        return json.load(f)

def read_hist() -> dict:
    with open("data/history.json", "r") as f:
        return json.load(f)

def load_tasks(tasks: dict):
    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f)

def load_history(history: dict):
    with open("data/history.json", "w") as f:
        json.dump(history, f)

base_dir = os.path.dirname(os.path.abspath(__file__)) # путь к файлу в котроом запускают без самого файла

tasks_path = os.path.join(base_dir, "data", "tasks.json")
history_path = os.path.join(base_dir, "data", "history.json")

os.makedirs(os.path.dirname(tasks_path), exist_ok=True)

print(base_dir, tasks_path, history_path)