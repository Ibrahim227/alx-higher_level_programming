#!/usr/bin/python3
"""Imort the required module"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == '__main__':
    url = str(sys.argv[1])
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as resp:
            resp_r = resp.read()
            print(resp_r.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e.code))
