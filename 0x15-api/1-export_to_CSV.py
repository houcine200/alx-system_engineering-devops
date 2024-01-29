#!/usr/bin/python3
"""Fetch & display TODO list progress for given employee ID using REST API."""
import csv
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
            tasks.append(task)

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)


row_list = []
for task in tasks:
    row_list.append([employee_id,
                    employee.get('username'),
                    task.get('completed'),
                    task.get('title')])

with open(f"{employee_id}.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
    writer.writerows(row_list)
