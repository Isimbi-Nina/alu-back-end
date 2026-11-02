#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    name = user.get("name")
    total = 0
    done = 0
    done_titles = []

    for todo in todos:
        total = total + 1
        if todo.get("completed") is True:
            done = done + 1
            done_titles.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for title in done_titles:
        print("\t {}".format(title))
