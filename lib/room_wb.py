import json
import os


def room_blocked(roomname: str, word: str = None):
    if os.path.isfile("Global/rooms/{}.json".format(roomname)):
        with open('Global/rooms/{}.json'.format(roomname), encoding='utf-8') as fp:
            data = json.load(fp)
        wordlist = data['blacklist']
        for i in wordlist:
            if i.lower() in word.lower():
                return True
        else:
            return False


def add_word_to_room(roomname: str, word: str):
    if os.path.isfile("Global/rooms/{}.json".format(roomname)):
        wordlist = room_blocked(roomname, word)
        with open("Global/rooms/{}.json".format(roomname), encoding='utf-8') as fp:
            data = json.load(fp)
        if wordlist:
            return 'The Word is allready in the Blacklist.'
        elif not wordlist:
            liste = data['blacklist']
            liste.append(word)
            with open("Global/rooms/{}.json".format(roomname), 'w+') as fp:
                json.dump(data, fp, indent=4)
            return 'The Word **{}** has been added to the Blacklist.'.format(word)


def remove_word_to_room(roomname: str, word: str):
    if os.path.isfile("Global/rooms/{}.json".format(roomname)):
        wordlist = room_blocked(roomname, word)
        with open("Global/rooms/{}.json".format(roomname), encoding='utf-8') as fp:
            data = json.load(fp)
        if not wordlist:
            return 'The Word is not in the Blacklist.'
        elif wordlist:
            liste = data['blacklist']
            liste.remove(word)
            with open("Global/rooms/{}.json".format(roomname), 'w+') as r:
                json.dump(data, r, indent=4)
            return 'The Word **{}** has been removed from the Blacklist.'.format(word)


def room_blacklist(roomname: str):
    if os.path.isfile("Global/rooms/{}.json".format(roomname)):
        with open("Global/rooms/{}.json".format(roomname), encoding='utf-8') as fp:
            data = json.load(fp)
        return data['blacklist']
