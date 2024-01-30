#!/usr/bin/python3
"""0-gather_data_from_an_API and export data in the JSON format module"""

import csv
import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    """
    get_employee_todo_progress: for a given employee ID, returns information
    about his/her TODO list progress.
    Args:
    employee_id: the user's id
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = (
                'https://jsonplaceholder.typicode.com/'
                f'todos?userId={employee_id}'
                )
    try:
        with urllib.request.urlopen(user_url) as user_response:
            user_data = json.loads(user_response.read().decode('utf-8'))
            employee_name = user_data.get('username')

            """Make a GET request to fetch TODO list data"""
            with urllib.request.urlopen(todo_url) as todo_response:
                todo_data = json.loads(todo_response.read().decode('utf-8'))

                total_tasks = len(todo_data)
                completed_tasks = [task for task in todo_data if
                                   task['completed']]

                print(f'Employee {employee_name} is done with ', end='')
                print(f'tasks({len(completed_tasks)}/{total_tasks}):')

                """titles of completed tasks"""
                for task in completed_tasks:
                    print(f'\t{task["title"]}')

                """ all tasks that are owned by this employee """
                task_obj = []
                for data in todo_data:
                    task_obj.append(
                        {
                            "task": data.get('title'),
                            "completed": data.get('completed'),
                            "username": employee_name,
                            }
                            )
                    if not task_obj[-1]:
                        task_obj.append(', ')
                """dictionary"""
                dictionary = {
                        employee_id: task_obj
                        }
                json_object = json.dumps(dictionary)
                with open(f'{sys.argv[1]}.json', 'w') as f:
                    f.write(json_object)
    except urllib.error.HTTPError as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
