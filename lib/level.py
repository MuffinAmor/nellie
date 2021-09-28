import os
import json

########################################################################################################################
def user_add_credits(user_id: int, money: int):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id]['money'] += money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id] = {}
            credit[user_id]['money'] = money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
    else:
        credit = {user_id: {}}
        credit[user_id]['money'] = money
        with open('money.json', 'w') as fp:
            json.dump(credit, fp, sort_keys=True, indent=4)


########################################################################################################################
def get_credits(user_id: int):
    if os.path.isfile('money.json'):
        with open('money.json', 'r') as fp:
            credit = json.load(fp)
        return credit[user_id]['money']
    else:
        return 0


########################################################################################################################
def user_remove_credits(user_id: int, money: int):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id]['money'] -= money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id] = {}
            credit[user_id]['money'] = 0
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
    else:
        credit = {user_id: {}}
        credit[user_id]['money'] = 0
        with open('money.json', 'w') as fp:
            json.dump(credit, fp, sort_keys=True, indent=4)
