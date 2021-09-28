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
    header = {"AuthKey": ""}
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
    header = {"Authorization": ""}
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
