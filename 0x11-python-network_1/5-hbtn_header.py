#!/usr/bin/python3
"""Import the requires module"""
import requests
import sys


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    with requests.get(my_url) as my_response:
        if 'X-Request-Id' in my_response.headers:
            print(my_response.headers['X-Request-Id'])
