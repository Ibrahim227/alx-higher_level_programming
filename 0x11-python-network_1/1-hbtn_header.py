#!/usr/bin/python3
"""Import urllib and sys module"""
import urllib.request
import sys


if __name__ == '__main__':
    url = str(sys.argv[1])
    m_req = urllib.request.Request(url)
    with urllib.request.urlopen(m_req) as resp:
        if "X-Request-Id" in resp.headers:
            x_id = dict(resp.headers).get("X-Request-Id")
            print(x_id)
