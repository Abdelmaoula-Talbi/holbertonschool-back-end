#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
export the data in the json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2 or len(argv) < 2:
        print("error")
    elif argv[1].isdigit() is False:
        print("argument must be an integer")

    my_list = []
    response1 = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in response1.json():
        if i.get('id') == int(argv[1]):
            USERNAME = i.get('username')

    response2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    for j in response2.json():
        if j.get('userId') == int(argv[1]):
            my_dict = {'task': j.get('title'), 'completed': j.get('completed'),
                       'username': USERNAME}
            my_list.append(my_dict)
    my_obj = {argv[1]: my_list}
    with open(f'{argv[1]}.json', 'w') as file:
        json.dump(my_obj, file)
