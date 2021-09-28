import json
import os

import requests



def ban_check(id: int):
    if not os.path.isfile("Secure"):
        try:
            os.mkdir("Secure")
        except:
            pass
    if os.path.isfile('Secure/apiban.json'):
        with open('Secure/apiban.json', encoding='utf-8') as fp:
            check = json.load(fp)
        try:
            check[str(id)]
        except KeyError:
            banlist(id)
        with open('Secure/apiban.json', encoding='utf-8') as fp:
            check = json.load(fp)
        return check[str(id)]['Service']
    else:
        banlist(id)
        with open('Secure/apiban.json', encoding='utf-8') as fp:
            check = json.load(fp)
        return check[str(id)]['Service']


def recheck(id: int):
    alert = alertban(str(id))
    ksoft = ksoftban(str(id))
    if not os.path.isfile("Secure"):
        try:
            os.mkdir("Secure")
        except:
            pass
    if os.path.isfile('Secure/apiban.json'):
        with open('Secure/apiban.json', 'r') as fp:
            check = json.load(fp)
        if str(id) in check:
            del check[str(id)]
            check[id] = {}
            check[id] = {"Service": {}}
            if alert:
                check[id]['Service']['Alert'] = True
            else:
                check[id]['Service']['Alert'] = False
            if ksoft:
                check[id]['Service']['Ksoft'] = True
            else:
                check[id]['Service']['Ksoft'] = False
            with open('Secure/apiban.json', 'w') as fp:
                json.dump(check, fp, indent=4)
            return "Ok"
    else:
        check = {id: {"Service": {}}}
        if alert:
            check[id]['Service']['Alert'] = True
        else:
            check[id]['Service']['Alert'] = False
        if ksoft:
            check[id]['Service']['Ksoft'] = True
        else:
            check[id]['Service']['Ksoft'] = False
    with open('Secure/apiban.json', 'w') as fp:
        json.dump(check, fp, indent=4)
        return "Ok"


def banlist(id: int):
    alert = alertban(str(id))
    ksoft = ksoftban(str(id))
    if not os.path.isfile("Secure"):
        try:
            os.mkdir("Secure")
        except:
            pass
    if os.path.isfile('Secure/apiban.json'):
        with open('Secure/apiban.json', 'r') as fp:
            check = json.load(fp)
        if not str(id) in check:
            check[id] = {}
            check[id] = {"Service": {}}
            if alert:
                check[id]['Service']['Alert'] = True
            else:
                check[id]['Service']['Alert'] = False
            if ksoft:
                check[id]['Service']['Ksoft'] = True
            else:
                check[id]['Service']['Ksoft'] = False
            with open('Secure/apiban.json', 'w') as fp:
                json.dump(check, fp, indent=4)
            return "Ok"
    else:
        check = {id: {"Service": {}}}
        if alert:
            check[id]['Service']['Alert'] = True
        else:
            check[id]['Service']['Alert'] = False
        if ksoft:
            check[id]['Service']['Ksoft'] = True
        else:
            check[id]['Service']['Ksoft'] = False
    with open('Secure/apiban.json', 'w') as fp:
        json.dump(check, fp, indent=4)
        return "Ok"


def alertban(userid: str):
    search_term = userid
    header = {"AuthKey": "5deeef9e4d2ca"}
    r = requests.get(
        "https://api.alertbot.services/v1/?action=bancheck&userid=%s" % (search_term), headers=header)
    if r.status_code is 200:
        ban = r.json()
        try:
            banned = ban['data']['result']['banned']
        except KeyError:
            print("KeyError")
        if banned:
            return True
        elif banned is False:
            return False


def ksoftban(userid: str):
    search_term = userid
    header = {"Authorization": "f389c89e9f1dc2bd4f8792fd9fb79f5d00ba76ba"}
    r = requests.get(
        "https://api.ksoft.si/bans/check&user=%s" % (search_term), headers=header)
    if r.status_code is 200:
        ban = r.json()
        try:
            banned = ban['is_banned']
        except KeyError:
            print("KeyError")
        if banned:
            return True
        elif banned is False:
            return False
