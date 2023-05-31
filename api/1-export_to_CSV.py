#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2 or len(argv) < 2:
        print("error")
    elif argv[1].isdigit() is False:
        print("argument must be an integer")

    my_dict = {}
    my_list = []
    response1 = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in response1.json():
        if i.get('id') == int(argv[1]):
            my_dict['USERNAME'] = i.get('username')

    response2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    for j in response2.json():
        if j.get('userId') == int(argv[1]):
            my_dict['USERID'] = j.get('userId')
            my_dict['COMPLETED_STATUS'] = j.get('completed')
            my_dict['TITLE'] = j.get('title')
            my_list.append(my_dict)
    fields = ['USERID', 'USERNAME', 'COMPLETED_STATUS', 'TITLE']

    with open(f'{argv[1]}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)

        writer.writerows(my_list)
