import json
import os
import random
import string


os.chdir(r'/')


def prefix(server_id: str):
    default_prefix = "n!"
    if os.path.isfile("prefix.json"):
        with open("prefix.json") as f:
            prefixes = json.load(f)
        try:
            return prefixes.get(server_id, default_prefix)
        except KeyError:
            return default_prefix
    else:
        prefixes = {}
        with open('prefix.json', 'w') as w:
            json.dump(prefixes, w, indent=4)
        try:
            return prefixes.get(server_id, default_prefix)
        except KeyError:
            return default_prefix


def get_token(n: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def get_news():
    if os.path.isfile("Setting/news.json"):
        with open("Setting/news.json") as fp:
            data = json.load(fp)
        return data
