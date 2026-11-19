# All actions of the program are defined here. This file is imported in main.py and executed from there.
import json

def read_tasks():
    with open("data/tasks.json", "r") as f:
        return json.load(f)

def read_hist():
    with open("data/history.json", "r") as f:
        return json.load(f)

def load_tasks(tasks):
    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f)

def load_history(history):
    with open("data/history.json", "w") as f:
        json.dump(history, f)