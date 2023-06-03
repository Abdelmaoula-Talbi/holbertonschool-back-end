#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
export the data in the json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    my_obj = {}
    response1 = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in response1.json():
        # if i.get('id') == int(argv[1]):
        my_list = []
        USERNAME = i.get('username')
        USERID = i.get('id')

        response2 = requests.get("https://jsonplaceholder.typicode.com/todos")

        for j in response2.json():
            if j.get('userId') == USERID:
                my_dict = {'username': USERNAME, 'task': j.get('title'),
                           'completed': j.get('completed')}
                my_list.append(my_dict)
        my_obj.update({USERID: my_list})
    with open('todo_all_employees.json', 'w') as file:
        json.dump(my_obj, file)
