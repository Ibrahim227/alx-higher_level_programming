#!/usr/bin/python3
"""Import Required module"""
import urllib.request


if __name__ == '__main__:':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        values = {type: html}
        print(f"Body response:'\t - :' {values}")
        print(html)
