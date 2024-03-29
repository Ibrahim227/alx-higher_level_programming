#!/usr/bin/python3
"""import required module"""
import sys
import urllib.request
import urllib.error
import urllib.parse


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    request = urllib.request.Request(my_url)
    try:
        with urllib.request.urlopen(my_url) as my_response:
            read_response = my_response.read()
            print(read_response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
