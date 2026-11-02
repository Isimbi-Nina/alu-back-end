#!/usr/bin/python3
"""Export the tasks of all employees to todo_all_employees.json."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = {}

    for user in users:
        tasks = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                task = {}
                task["username"] = user.get("username")
                task["task"] = todo.get("title")
                task["completed"] = todo.get("completed")
                tasks.append(task)
        data[str(user.get("id"))] = tasks

    file = open("todo_all_employees.json", "w")
    json.dump(data, file)
    file.close()

