#!/usr/bin/python3
""" Lists 10 commits (from the most recent to oldest) of a repository:
      - The first argument will be the repository name
      - The second argument will be the owner name """

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                  commits[a].get("sha"),
                  commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
