import json
import os
import sys

os.chdir(r'/')

def roomowner(user_id: str):
    liste = os.listdir(r'/home/niko/data/Nellie/rooms')
    for name in liste:
        with open("rooms/{}".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        owner = data['owner']
        if str(user_id) in str(owner):
            return True
    else:
        return False


def roommod(user_id: str):
    liste = os.listdir(r'/home/niko/data/Nellie/rooms')
    for name in liste:
        with open("rooms/{}".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        if int(user_id) in data['mods'] or int(user_id) == data['owner']:
            return True
    else:
        return False


def mod_right_here(room: str, user_id: str):
    liste = os.listdir(r'/home/niko/data/Nellie/rooms')
    try:
        for name in liste:
            with open("rooms/{}".format(name), encoding="utf-8") as fp:
                data = json.load(fp)
            if int(user_id) in data['mods'] or int(user_id) == data['owner']:
                if str(name.replace(".json", "")) == str(room):
                    return True
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
