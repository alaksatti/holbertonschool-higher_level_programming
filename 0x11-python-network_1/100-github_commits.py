#!/usr/bin/python3

"""
Takes 2 arguments in order to ist 10 commits
(from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the Github API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    c = get('https://api.github.com/repos/' + argv[2] +
            '/' + argv[1] + '/commits')
    if c.json():
        c_num = 0
        for commits in c.json():
            if c_num < 10:
                commit = commits.get('sha')
                name = commits.get('commit').get('author').get('name')
                print(commit + ': ' + name)
                c_num += 1

    else:
        print("Not a valid JSON")
