#!/usr/bin/python3
"""Import the required module"""
import requests
import sys


if __name__ == "__main__":
    my_url = "http://0.0.0.0:5000/search_user"
    my_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    my_payload = {"q": my_letter}
    my_request = requests.post(my_url, my_payload)
    try:
        my_response = my_request.json()
        if my_response == {}:
            print("No result")
        else:
            print(
                "[{}] {}".format(
                    my_response.get("id"),
                    my_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
