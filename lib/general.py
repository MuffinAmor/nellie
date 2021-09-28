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
