from datetime import datetime

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


task1 = Task("clean", "2026-11-16", 8)
task2 = Task("shower gel", "2026-12-22", 7)
task3 = Task("bugs", "2026-11-12", 10)
task4 = Task("123451234512345123451235123")
task5 = Task("A")
tasks = [task1, task2, task3, task4, task5]
# 17 symb per task
# within contract, expects max 99 tasks, and max 34 symbols oper tasks in total
def build_list(tasks):
    ### Function accepts tasks as class objects, and presents them
    ### from [0] to the last one. returns fstring object, containing all tasks
    string = f""
    index = 1
    line_width = 17
    format_str = "%Y-%m-%d"
    today_date = datetime.now().date()
    for task in tasks:
        deadline_status = "----"
        if task.deadline:
            deadline_date = datetime.strptime(task.deadline, format_str).date()
            remaining_days = deadline_date - today_date
            if remaining_days.days < 0:
                deadline_status = "ovrd"
            elif remaining_days.days in range(0, 10):
                deadline_status = f"-0{remaining_days.days}d"
            else:
                deadline_status = f"-{remaining_days.days}d"
        if task.priority:
            if int(task.priority) < 10:
                task_priority = "0" + str(task.priority)
            else:
                task_priority = str(task.priority)
        else:
            task_priority = "--"
        
        if index > 9:
            dynamic_id = index
        else:
            dynamic_id =  "0" + str(index)
        formatted_body = task.body
        if len(formatted_body) < line_width:
            padding = (line_width - 1) - len(formatted_body)
            formatted_body += " "
            formatted_body += "-" * padding
        elif len(formatted_body) > line_width:
            part1 = formatted_body[:line_width]
            part2 = formatted_body[line_width:]
            part1 += " |      |   "
            padding = line_width - len(part2)
            if len(part2) < line_width:
                part2 += " "
                part2 += "-" * (padding -1)
            else:
                part2 += "-" * padding
            
            formatted_body = part1 + "\n     " + part2
        
        string += f"({dynamic_id}) {formatted_body} | {deadline_status} | {task_priority}\n"
        index += 1
    return string




ls2 = f"""
_______TASKLINE_______

{build_list(tasks)}
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

