import json
import os
import sys


def create():
    if not os.path.isfile('pics'):
        try:
            os.mkdir('pics')
        except:
            pass


def add_pic(token, name, author_id: str, time: str, datas):
    try:
        create()
        if not os.path.isfile("pics/{}.json".format(token)):
            data = {
                'room': name,
                'author': author_id,
                'time': time,
                'data': datas
            }
            with open("pics/{}.json".format(token), "w+") as fp:
                json.dump(data, fp, indent=4)
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def remove_pic(token):
    if os.path.isfile("pics/{}.json".format(token)):
        os.remove("Nellie/pics/{}.json".format(token))


def request_pic_room(token: str):
    if os.path.isfile("pics/{}.json".format(token)):
        with open("pics/{}.json".format(token), encoding='utf-8') as fp:
            data = json.load(fp)
        return data['room']
    else:
        return False


def request_pic_msg(token: str):
    if os.path.isfile("pics/{}.json".format(token)):
        with open("pics/{}.json".format(token), encoding='utf-8') as fp:
            data = json.load(fp)
        return data['data']
    else:
        return False
