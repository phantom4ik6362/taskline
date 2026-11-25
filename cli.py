from datetime import datetime

# CLI interface elements are placed here

def build_list(tasks: list) -> str:
    ### Function accepts tasks as class objects, and presents them
    ### from [0] to the last one. returns fstring object, containing all tasks
    tasks_string = f""
    next_index = 1
    line_width = 17
    format_str = "%Y-%m-%d"
    today_date = datetime.now().date()
    
    for task in tasks:
        deadline_status = "----"
        if task.deadline: # count and sets amound of days remaining untill deadline. TODO: fix 99+ days problem
            deadline_date = datetime.strptime(task.deadline, format_str).date()
            remaining_days = deadline_date - today_date
            if remaining_days.days < 0:
                deadline_status = "ovrd"
            elif remaining_days.days in range(0, 10):
                deadline_status = f"00{remaining_days.days}d"
            elif remaining_days.days in range(100, 1000):
                deadline_status = f"{remaining_days.days}d"
            else:
                deadline_status = f"0{remaining_days.days}d"

        if task.priority: # set priority. if less than 10, adds 0 to a start
            task_priority = str(task.priority)
        else:
            task_priority = "-"

        if next_index > 9: # create a dynamic index (usable if convert to int and -1. will be original tasks list index)
            dynamic_index = next_index
        else:
            dynamic_index =  "0" + str(next_index)

        formatted_body = task.body # format task body. operates with 1-34 symbol tasks.
        if len(formatted_body) < line_width:
            padding = (line_width - 1) - len(formatted_body)
            formatted_body += " "
            formatted_body += "-" * padding
        elif len(formatted_body) > line_width:
            body_part1 = formatted_body[:line_width]
            body_part2 = formatted_body[line_width:]
            body_part1 += " |      |   "
            padding = line_width - len(body_part2)
            if len(body_part2) < line_width:
                body_part2 += " "
                body_part2 += "-" * (padding -1)
            else:
                body_part2 += "-" * padding
            formatted_body = body_part1 + "\n     " + body_part2

        tasks_string += f"({dynamic_index}) {formatted_body} | {deadline_status} | {task_priority}\n" # format final string will be returned
        next_index += 1
    return tasks_string

def build_history(tasks: list) -> str:
    history_string = f""
    next_index = 1
    line_width = 24

    for task in tasks:
        if task.priority:
            task_priority = str(task.priority)
        else:
            task_priority = "-"
        
        if next_index > 9:
            dynamic_index = next_index
        else:
            dynamic_index = "0" + str(next_index)
        
        formatted_body = task.body
        if len(formatted_body) < line_width:
            padding = (line_width - 1) - len(formatted_body)
            formatted_body += " "
            formatted_body += "-" * padding
        elif len(formatted_body) > line_width:
            body_part1 = formatted_body[:line_width]
            body_part2 = formatted_body[line_width:]
            body_part1 += " |"
            padding = line_width - len(body_part2)
            if len(body_part2) < line_width:
                body_part2 += " "
                body_part2 += "-" * (padding -1)
            else:
                body_part2 += "-" * padding
            formatted_body = body_part1 + "\n     " + body_part2

        history_string += f"({dynamic_index}) {formatted_body} | {task_priority}\n"
        next_index += 1
    return history_string