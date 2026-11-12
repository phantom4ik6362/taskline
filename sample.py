from datetime import datetime

# Taskline UI samples

# !!! REQUIRED TO ADD OVERDUE SCENERIO, DYNAMIC TRANSFORMING FROM yyyy-mm-dd TO REMAINING DAYS
# !!! AND TO WORK WITH DYNAMIC AMOUND OF DAYS LEFT + DYNAMIC LENGTH OF INDEX (1) (10) + DYNAMIC LENGTH OF DEADLINE

# !!! CREATE LOGIC TO AVOID PROBLEM WITH 99+ days LEFT
# FIX STATUS CHANGE ADDED IN LINE 40
class Task:
    def __init__(self, body, deadline=None, priority="--"):
        self.body = body
        self.deadline = deadline
        self.priority = priority
        self.status = "todo"
    def complete(self):
        self.status = "done"


task1 = Task("clean", "16-11-2026", "08")
task2 = Task("shower gel", "22-12-2026", "07")
task3 = Task("bugs", "12-11-2026", "10")
task4 = Task("123451234512345123451235123")
task5 = Task("A")
tasks = [task1, task2, task3, task4, task5]
# 17 symb per task
# within contract, expects max 99 tasks, and max 34 symbols oper tasks in total
def build_list(tasks):
    string = f""
    index = 1
    line_width = 17
    format_str = "%d-%m-%Y"
    today_date = datetime.now().date()
    for task in tasks:
        deadline_status = "----"
        if task.deadline:
            deadline_date = datetime.strptime(task.deadline, format_str).date()
            remaining_days = deadline_date - today_date
            if remaining_days.days < 0:
                task.status = "overdue"
                deadline_status = "ovrd"
            elif remaining_days.days in range(0, 10):
                deadline_status = f"-0{remaining_days.days}d"
            else:
                deadline_status = f"-{remaining_days.days}d"
        if task.priority:
            task_priority = task.priority
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

(01) clean ----------- | +04d | 08
(02) shower gel ------ | +75d | 07
(03) bugs ------------ | ---- | 10
(04) 12345123451234512 |      |   
     3451235123454444  | ---- | --
(05) Abcdfgjhiturfjgbv | ---- | --

_______________________
"""

