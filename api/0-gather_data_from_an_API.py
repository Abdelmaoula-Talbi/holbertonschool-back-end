#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2 or len(argv) < 2:
        print("error")
    elif argv[1].isdigit() is False:
        print("argument must be an integer")

    response1 = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in response1.json():
        if i.get('id') == int(argv[1]):
            name = i.get('name')

    response2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    total_tasks = 0
    completed_tasks = 0
    list_of_completed_tasks = []
    for j in response2.json():
        if j.get('userId') == int(argv[1]):
            if j.get('completed') is True:
                completed_tasks += 1
                list_of_completed_tasks.append(j.get('title'))
            total_tasks += 1

    print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")
    for elem in list_of_completed_tasks:
        print(f"\t {elem}")
