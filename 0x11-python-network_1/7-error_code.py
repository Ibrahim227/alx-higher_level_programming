#!/usr/bin/python3
"""Import the erquired module"""
import sys
import requests


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    with requests.get(my_url) as my_response:
        if my_response.status_code == 200:
            print(my_response.text)
        else:
            print("Error code: {}".format(my_response.status_code))
