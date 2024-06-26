#!/usr/bin/python3
"""Import Required module"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    if response.status == 200:
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}\n"
            "\t- utf8 content: {}".format(
                type(html),
                html,
                html.decode('utf-8')))
