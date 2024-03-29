#!/usr/bin/python3
"""Import the required module"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    # Sending a GET request to the GitHub API
    response = requests.get("https://api.github.com/user", auth=auth)
    if response.status_code == 200:
        # Converting my GitHub API Response to JSON
        info = response.json()
        # Now, to print my GitHub ID
        print("{}".format(info.get("id")))
    else:
        print("None")
