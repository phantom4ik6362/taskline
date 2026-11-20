# This file handles file management operations, including handling corrupted file crash by itself.
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