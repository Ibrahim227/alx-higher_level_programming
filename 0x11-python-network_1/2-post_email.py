#!/usr/bin/python3
"""Import required module"""
import urllib.request
import sys


if __name__ == '__main__':
    url = str(sys.argv[1])
    my_email = {"email": str(sys.argv[2])}
    send_data = urllib.parse.urlencode(url, send_data, method="POST")
    my_req = urllib.request.Request(url)
    with urllib.request.urlopen(my_req) as resp:
        print(resp.read().decode("utf-8")
