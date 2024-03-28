#!/usr/bin/python3
"""Import Required module"""
import urllib


req = urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
print(req.read)
