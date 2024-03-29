#!/usr/bin/python3
"""Import the requires module"""
import requests
import sys


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    my_email = {"email": str(sys.argv[2])}
    with requests.post(my_url, my_email) as my_request:
        print(my_request.text)
