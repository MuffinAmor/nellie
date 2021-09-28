import json
import os
import sys

os.chdir(r'/')


def create_tree():
    if not os.path.isfile("Global"):
        try:
            os.mkdir("Global")
        except:
            pass
    if not os.path.isfile("Global/rooms"):
        try:
            os.mkdir("Global/rooms")
        except:
            pass


def create_room(name: str, user_id: str):
    create_tree()
    if not os.path.isfile("Global/rooms/{}.json".format(name)):
        data = {'num': name,
                'owner': user_id,
                'cid': [],
                'mods': [],
                'banned': [],
                'blacklist': [],
                'spam': 3,
                'lang': 'Not set.',
                'desc': 'Not set.',
                'topic': "None",
                'pictures': True,
                'open': False,
                'vip': [],
                'partner': []
                }
        with open("Global/rooms/{}.json".format(name), "w+") as fp:
            json.dump(data, fp, indent=4)
        return True
    else:
        return False


def edit_special(name: str, id: int, action: str, pos: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        special = list(data[pos])
        if action == "append":
            if id in special:
                return False
            else:
                data[pos].append(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "remove":
            if not id in special:
                return False
            else:
                data[pos].remove(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "clear":
            data[pos].clear()
            with open("Global/rooms/{}.json".format(name), "w+") as fp:
                json.dump(data, fp, indent=4)
            return True
    else:
        return None


def edit_banned(name: str, id: int, action: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        banned = list(data['banned'])
        if action == "append":
            if id in banned:
                return False
            else:
                data['banned'].append(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "remove":
            if not id in banned:
                return False
            else:
                data['banned'].remove(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "clear":
            data['banned'].clear()
            with open("Global/rooms/{}.json".format(name), "w+") as fp:
                json.dump(data, fp, indent=4)
            return True
    else:
        return None


def edit_mods(name: str, id: int, action: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        mods = data['mods']
        if action == "append":
            if id in mods:
                return False
            else:
                data['mods'].append(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "remove":
            if not id in mods:
                return False
            else:
                data['mods'].remove(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "clear":
            data['mods'].clear()
            with open("Global/rooms/{}.json".format(name), "w+") as fp:
                json.dump(data, fp, indent=4)
            return True
    else:
        return None


def edit_channel(name: str, id: int, action: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        cid = list(data['cid'])
        if action == "append":
            if id in cid:
                return False
            else:
                data['cid'].append(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
                return True
        elif action == "remove":
            if not id in cid:
                return False
            else:
                data['cid'].remove(id)
                with open("Global/rooms/{}.json".format(name), "w+") as fp:
                    json.dump(data, fp, indent=4)
            return True
        elif action == "clear":
            data['cid'].clear()
            with open("Global/rooms/{}.json".format(name), "w+") as fp:
                json.dump(data, fp, indent=4)
            return True
    else:
        return None


def is_connected(id: int, stat: str):
    try:
        create_tree()
        liste = os.listdir(r'/home/niko/data/Nellie/Global/rooms')
        for name in liste:
            with open("Global/rooms/{}".format(name), encoding="utf-8") as fp:
                data = json.load(fp)
            if id in data[stat]:
                return name.replace(".json", "")
        else:
            return False
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def edit_room(name: str, stat: str, wert):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        data[stat] = wert
        with open("Global/rooms/{}.json".format(name), "w+") as fp:
            json.dump(data, fp, indent=4)
        return True
    else:
        return None


def is_owner(id: str):
    create_tree()
    liste = os.listdir(r'/home/niko/data/Nellie/Global/rooms')
    for name in liste:
        with open("Global/rooms/{}".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        if str(id) == data['owner']:
            return name.replace(".json", "")
    else:
        return False


def get_info(name: str, stat: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        with open("Global/rooms/{}.json".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        return data[stat]
    else:
        return None


def get_more_info(stat: str):
    create_tree()
    a = r"/home/niko/data/Nellie/Global/rooms/"
    liste = os.listdir(a)
    all = []
    for name in liste:
        with open("Global/rooms/{}".format(name), encoding="utf-8") as fp:
            data = json.load(fp)
        if data[stat]:
            all.append(name.replace(".json", ""))
    return all


def name_check(name: str):
    create_tree()
    a = r"/home/niko/data/Nellie/Global/rooms/"
    liste = os.listdir(a)
    all = []
    for i in liste:
        with open("Global/rooms/{}".format(i), encoding="utf-8") as fp:
            data = json.load(fp)
        if data['num'] == i.replace(".json", ""):
            all.append(i.replace(".json", ""))
    if name in all:
        return True
    else:
        return False


def del_room(name: str):
    create_tree()
    if os.path.isfile("Global/rooms/{}.json".format(name)):
        os.remove("Global/rooms/{}.json".format(name))
        return True
    else:
        return False
