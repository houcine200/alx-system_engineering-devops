#!/usr/bin/python3
"""Fetch & display TODO list progress for all employees using REST API."""
import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        all_data[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file, indent=2)
