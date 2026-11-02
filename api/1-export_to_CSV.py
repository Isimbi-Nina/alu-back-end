#!/usr/bin/python3
"""Export an employee's tasks to a CSV file named USER_ID.csv."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    username = user.get("username")

    file = open(user_id + ".csv", "w")
    for todo in todos:
        line = '"{}","{}","{}","{}"\n'.format(
            user_id, username, todo.get("completed"), todo.get("title"))
        file.write(line)
    file.close()
