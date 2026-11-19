# Main definition of the program
import os

base_dir = os.path.dirname(os.path.abspath(__file__)) # путь к файлу в котроом запускают без самого файла

tasks_path = os.path.join(base_dir, "data", "tasks.json")
history_path = os.path.join(base_dir, "data", "history.json")

os.makedirs(os.path.dirname(tasks_path), exist_ok=True)

print(base_dir, tasks_path, history_path)