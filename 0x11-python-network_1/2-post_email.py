#!/usr/bin/python3
"""Import required module"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = str(sys.argv[1])
    my_email = {"email": str(sys.argv[2])}
    send_data = urllib.parse.urlencode(my_email).encode("ascii")
    my_req = urllib.request.Request(url, send_data, method="POST")
    with urllib.request.urlopen(my_req) as resp:
        print(resp.read().decode("utf-8"))
