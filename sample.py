from datetime import datetime
import cli

# Taskline UI samples

# !!! TODO: CREATE LOGIC TO AVOID PROBLEM WITH 99+ days LEFT

class Task:
    def __init__(self, body, deadline=None, priority=None):
        self.body = body
        self.deadline = deadline
        self.priority = priority
        self.status = "todo"
    def complete(self):
        self.status = "done"
    def return_dict(self):
        return {"body": self.body, "deadline": self.deadline, "priority": self.priority, "status": self.status}


task1 = Task("clean", "2026-11-16", 8)
task2 = Task("shower gel", "2026-12-22", 7)
task3 = Task("bugs", "2028-11-12", 10)
task4 = Task("ggggggggggggggggg", "2026-11-23")
task5 = Task("A")
tasks = [task1, task2, task3, task4, task5]

ls2 = f"""
_______TASKLINE_______

{cli.build_list(tasks)}
_______________________
"""

print(ls2)


ls = f""" 
_______TASKLINE_______

(01) clean ----------- | -01d | 08
(02) shower gel ------ | -37d | 07
(03) bugs ------------ | ovrd | 10
(04) 12345123451234512 |      |   
     3451235123 ------ | ---- | --
(05) A --------------- | ---- | --

_______________________
"""

