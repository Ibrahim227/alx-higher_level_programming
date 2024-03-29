#!/usr/bin/python3
"""Import requires module"""
import requests


my_url = "https://alx-intranet.hbtn.io/status"
with requests.get(my_url) as my_response:
    if my_response.status_code == 200:
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}".format(
                type(my_response.text), my_response.text))
