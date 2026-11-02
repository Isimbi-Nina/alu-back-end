#!/usr/bin/python3
"""Export an employee's tasks to a JSON file named USER_ID.json."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    username = user.get("username")

    tasks = []
    for todo in todos:
        task = {}
        task["task"] = todo.get("title")
        task["completed"] = todo.get("completed")
        task["username"] = username
        tasks.append(task)

    data = {}
    data[user_id] = tasks

    file = open(user_id + ".json", "w")
    json.dump(data, file)
    file.close()

