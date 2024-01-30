#!/usr/bin/python3
"""Extended script to export data in the JSON format for all employees"""

import json
import urllib.request


def export_all_employees_todo():
    """
    export_all_employees_todo: Records all tasks from all employees
    and exports the data in the specified JSON format.
    """
    # URLs to GET
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    # GET User's information
    with urllib.request.urlopen(user_url) as user_response:
        user_data = json.loads(user_response.read().decode('utf-8'))

        employee_name_dict = {}
        for info in user_data:
            employee_id = info['id']
            employee_name = info['username']
            employee_name_dict[employee_id] = employee_name

    # GET all tasks
    with urllib.request.urlopen(todo_url) as todo_response:
        todo_data = json.loads(todo_response.read().decode('utf-8'))

    # Structure tasks in the specified format
    tasks_dict = {}
    for data in todo_data:
        user_id = data['userId']
        task_obj = {
            "username": employee_name_dict.get(user_id),
            "task": data['title'],
            "completed": data['completed'],
        }

        if user_id not in tasks_dict:
            tasks_dict[user_id] = []

        tasks_dict[user_id].append(task_obj)

    # Convert to JSON and write to file
    json_object = json.dumps(tasks_dict)
    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)


if __name__ == '__main__':
    export_all_employees_todo()
