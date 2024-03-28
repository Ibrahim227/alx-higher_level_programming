#!/usr/bin/python3
"""Import Required module"""
import urllib


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
pr = urllib.request.urlopen(req)
print(pr.code)
print(pr.read)
