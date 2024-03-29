#!/usr/bin/python3
"""Import the required module """
import requests
import sys


if __name__ == "__main__":
    # First argument, sys.argv[1] - repo name
    # Second argument, sys.argv[2] - owner of commit
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    # Sending a request and getting my response
    response = requests.get(url)
    # Converting my GitHub API Response to a JSON dict so that I
    # can extract the id from it
    info = response.json()
    try:
        for i in range(10):
            # Now, to print my GitHub ID
            print("{}: {}".format(
                info[i].get("sha"),
                info[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
