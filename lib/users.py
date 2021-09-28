import json
import os
from time import time

os.chdir(r'/')

def get_warns(user_id: str):
    if not os.path.isfile("User"):
        try:
            os.mkdir("User")
        except:
            pass
    if os.path.isfile('User/warns.json'):
        with open('User/warns.json', 'r') as fp:
            users = json.load(fp)
        try:
            return users[user_id]['warns']
        except KeyError:
            users[user_id]['warns'] = 0
            with open('User/warns.json', 'w') as f:
                json.dump(users, f, indent=4)
            return users[user_id]['warns']
    elif not os.path.isfile('User/warns.json'):
        users = {}
        with open('User/warns.json', 'w') as fp:
            json.dump(users, fp, indent=4)
        return 0


def get_time(user_id: str):
    if not os.path.isfile("User"):
        try:
            os.mkdir("User")
        except:
            pass
    if os.path.isfile('User/time.json'):
        with open('User/time.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return float(users[user_id]['time'])
        else:
            users[user_id] = {'time': 6}
            with open('User/time.json', 'w') as f:
                json.dump(users, f, indent=4)
            return float(users[user_id]['time'])
    else:
        users = {user_id: {'time': 6}}
        with open('User/time.json', 'w') as f:
            json.dump(users, f, indent=4)
        return users[user_id]['time']


def set_time(user_id: str):
    with open('User/time.json', 'r') as fp:
        users = json.load(fp)
    users[user_id]['time'] = str(time())
    with open('User/time.json', 'w') as fp:
        json.dump(users, fp, indent=4)
