'''MIT License

Copyright (c) 2021 MightyNiko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import json
import os
from time import time

os.chdir(r'/')

room_path = r'/home/niko/data/Nellie/rooms'


def function_room(room_name: str, action: str, unknown=None, new_data=None):
    if not os.path.isdir("rooms"):
        os.mkdir("rooms")

    if action == "create":
        if not os.path.isfile(f"rooms/{room_name}.json"):
            data = {
                'owner': unknown,
                'cid': [],
                'blacklist': [],
                'banned': [],
                'mods': [],
                'spam': 3,
                'lang': 'Not set.',
                'desc': 'Not set.',
                'topic': "None",
                'pictures': True,
                'pics': {},
                'open': False,
                'roles': {},
                'users': {},
                'log': {
                    'channel': None,
                    'save': {}
                }
            }
            with open(f"rooms/{room_name}.json", "w+") as fp:
                json.dump(data, fp, indent=4)
    else:
        if os.path.isfile(f"rooms/{room_name}.json"):
            with open(f"rooms/{room_name}.json", encoding="utf-8") as fp:
                data = json.load(fp)

            if action == 'delete':
                os.remove(f"rooms/{room_name}.json")

            elif action == "edit":
                data[unknown] = new_data
                with open(f"rooms/{room_name}.json", "w+") as fp:
                    json.dump(data, fp, indent=4)

            elif action == "request":
                return data[unknown]

            elif action == "append":
                if unknown not in data['cid']:
                    data['cid'].append(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)

            elif action == "remove":
                if unknown in data['cid']:
                    data['cid'].remove(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)

            elif action == "append_ban":
                if int(unknown) not in data['banned']:
                    data['banned'].append(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)

            elif action == "remove_ban":
                if int(unknown) in data['banned']:
                    data['banned'].remove(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)

            elif action == "append_mod":
                if int(unknown) not in data['mods']:
                    data['mods'].append(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)

            elif action == "remove_mod":
                if int(unknown) in data['mods']:
                    data['mods'].remove(int(unknown))
                    with open(f"rooms/{room_name}.json", "w+") as fp:
                        json.dump(data, fp, indent=4)
            else:
                pass


def is_connected(channel_id, stat: str):
    liste = os.listdir(room_path)
    for name in liste:
        with open(f"rooms/{name}", encoding="utf-8") as fp:
            data = json.load(fp)
        if channel_id in data[stat]:
            return name.replace(".json", "")
    else:
        return False


def is_public():
    liste = os.listdir(room_path)
    all_of_public = []
    for name in liste:
        with open(f"rooms/{name}", encoding="utf-8") as fp:
            data = json.load(fp)
        if str(data['open']) == "True":
            all_of_public.append(name)
    return all_of_public


def name_check(name: str):
    if os.path.isfile(f"rooms/{name}.json"):
        return True
    else:
        return False


def is_owner(user_id: int):
    liste = os.listdir(r'/home/niko/data/Nellie/rooms')
    for name in liste:
        with open("rooms/{}".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        if int(user_id) == data['owner']:
            return name.replace(".json", "")
    else:
        return False


def function_log(room_name: str, action: str, vari: str = None, new_data: str = None, new_data_two: str = None):
    with open(f"rooms/{room_name}.json", encoding="utf-8") as fp:
        data = json.load(fp)

    if action == "add":
        data['log'][vari] = new_data
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "add_action":
        data['log']['save'] = {
            new_data: new_data_two
        }
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "remove_action":
        del data['log']['save'][new_data]
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "request_action":
        return data['log']['save']


def function_pic(chat_room: str, action: str, token: str = None, author_id: int = None, time_float: float = None,
                 datas=None):
    with open(f"rooms/{chat_room}.json", encoding="utf-8") as fp:
        data = json.load(fp)
    if action == "add":
        data['pics'][token] = {
            'author': author_id,
            'time': time_float,
            'channel': datas
        }
        with open(f"rooms/{chat_room}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "remove":
        del datas['pics'][token]
        with open(f"rooms/{chat_room}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "request":
        return data['pics'][token]


def function_blacklist(room_name: str, action: str, word: str = None):
    with open(f"rooms/{room_name}.json", encoding='utf-8') as fp:
        data = json.load(fp)

    if action == "add":

        if word in data['blacklist']:
            return 'The Word is allready in the Blacklist.'

        else:
            data['blacklist'].append(word)
            with open(f"rooms/{room_name}.json", 'w+') as fp:
                json.dump(data, fp, indent=4)
            return f'The Word **{word}** has been added to the Blacklist.'

    elif action == "remove":

        if word not in data['blacklist']:
            return 'The Word is not in the Blacklist.'

        else:
            data['blacklist'].remove(word)
            with open(f"rooms/{room_name}.json", 'w+') as fp:
                json.dump(data, fp, indent=4)
            return f'The Word **{word}** has been removed from the Blacklist.'

    elif action == "request":
        wordlist = data['blacklist']
        for i in wordlist:
            if i.lower() in word.lower():
                return True
        else:
            return False


def function_users(room_name: str, action: str, user_id: str = None, request_data: str = None):
    with open(f"rooms/{room_name}.json", encoding="utf-8") as fp:
        data = json.load(fp)
    if user_id not in data['users']:
        data['users'][user_id] = {
            'time': "0",
            'warns': 0,
            'roles': None
        }
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)
    if action == "remove":
        del data['users'][user_id]
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "set_time":
        data['users'][user_id]['time'] = str(time())
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "request":
        return data['users'][user_id][request_data]

    elif action == "role_set":
        if request_data != data['users'][user_id]['roles']:
            data['users'][user_id]['roles'] = request_data
            with open(f"rooms/{room_name}.json", "w+") as fp:
                json.dump(data, fp, indent=4)

    elif action == "role_remove":
        if request_data != data['users'][user_id]['roles']:
            data['users'][user_id]['roles'] = None
            with open(f"rooms/{room_name}.json", "w+") as fp:
                json.dump(data, fp, indent=4)


def function_roles_room(room_name: str, action: str, role_name: str = None, new_data: str = None, data_two: str = None):
    with open(f"rooms/{room_name}.json", encoding="utf-8") as fp:
        data = json.load(fp)

    if action == "create":
        data['roles'][role_name] = {
            'color:': "0xc71515",
            'invite': None
        }
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "delete":
        del data['roles'][role_name]
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)

    elif action == "request":
        if role_name in data['roles']:
            return data['roles'][role_name]

    elif action == "edit":
        data['roles'][role_name][new_data] = data_two
        with open(f"rooms/{room_name}.json", "w+") as fp:
            json.dump(data, fp, indent=4)
