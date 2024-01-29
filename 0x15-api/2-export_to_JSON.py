#!/usr/bin/python3
"""Fetch & display TODO list progress for given employee ID using REST API."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        if user.get("id") == employee_id:
            employee = user

    tasks = []
    for task in todos:
        if task.get("userId") == employee_id:
            tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")
            })

    data = {f"{employee_id}": tasks}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
