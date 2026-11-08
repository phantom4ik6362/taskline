# Taskline UI samples

class Task:
    def __init__(self, body, deadline="----", priority="--"):
        self.body = body
        self.deadline = deadline
        self.priority = priority
        self.status = "todo"
    def complete(self):
        self.status = "done"


task1 = Task("clean", "+04d", "08")
task2 = Task("shower gel", "+75d", "07")
task3 = Task("bugs", "----", "10")
task4 = Task("1234512345123451234512351234544444")
task5 = Task("A", "+03d")
tasks = [task1, task2, task3, task4, task5]
# 17 symb per task
string = f""
index = 1
line_width = 17
for task in tasks:
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
        
        formatted_body = part1 + "\n    " + part2
    
    string += f"({index}) {formatted_body} | {task.deadline} | {task.priority}\n"
    index += 1




ls2 = f"""
_______TASKLINE_______

{string}
_______________________
"""

print(ls2)


ls = f"""
_______TASKLINE_______

(1) clean ----------- | +04d | 08
(2) shower gel ------ | +75d | 07
(3) bugs ------------ | ---- | 10
(4) 12345123451234512 |      |   
    3451235123454444  | ---- | --
(5) Abcdfgjhiturfjgbv | ---- | --

_______________________
"""